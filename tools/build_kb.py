"""Збирає базу знань для ІІ в один файл aedoc-kb.md.

    python tools/build_kb.py                 # з кореня репозиторію aedoc-docs
    python tools/build_kb.py <repo> <out.md>

Частина 1 — статті сайту з docs/ (у порядку меню mkdocs.yml, з посиланнями на dovidka).
Частина 2 — питання-відповіді з kb/ цього репозиторію (публічний репозиторій, на сайті не показуються).
Частина 3 — закрите з приватного репозиторію aedoc-kb.
    Шукається поруч: ../aedoc-kb, або шлях у змінній середовища AEDOC_KB_PRIVATE.
    Немає — збирається без нього.
"""
import os, re, sys, html, posixpath, datetime
from urllib.parse import urljoin
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "aedoc-kb.md"
DOCS, KB = ROOT / "docs", ROOT / "kb"
PRIVATE = Path(os.environ.get("AEDOC_KB_PRIVATE") or ROOT.parent / "aedoc-kb")
SITE = "https://dovidka.aedoc.com.ua/"


def url_of(rel):
    rel = rel[:-3]
    if rel == "index":
        return SITE
    if rel.endswith("/index"):
        rel = rel[:-6]
    return SITE + rel + "/"


def front_matter(text):
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        k, sep, v = line.partition(":")
        if sep and v.strip():
            meta[k.strip()] = v.strip()
    return meta, text[m.end():]


def convert(text, rel=None):
    """HTML/Markdown сайту → чистий текст для ІІ. rel=None — файл із kb/ (без адреси на сайті)."""
    def abs_link(href):
        if rel is None or re.match(r"^[a-z]+:|^#", href):
            return href
        path, _, anchor = href.partition("#")
        if path.endswith(".md"):
            u = url_of(posixpath.normpath(posixpath.join(posixpath.dirname(rel), path)))
            return u + ("#" + anchor if anchor else "")
        return urljoin(url_of(rel), href)

    def svg(m):
        words = [html.unescape(re.sub(r"<[^>]+>", "", t)).strip()
                 for t in re.findall(r"<text[^>]*>(.*?)</text>", m.group(0), re.S)]
        words = [w for w in words if w]
        return "\n[Схема: " + " · ".join(words) + "]\n" if words else ""

    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"<svg.*?</svg>", svg, text, flags=re.S)
    text = re.sub(r'<img[^>]*alt="([^"]*)"[^>]*>', lambda m: f"[Скриншот: {html.unescape(m.group(1))}]", text)
    text = re.sub(r"<img[^>]*>", "", text)
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", lambda m: f"[Скриншот: {m.group(1)}]" if m.group(1) else "", text)
    text = re.sub(r'<iframe[^>]*src="([^"]*)"[^>]*>.*?</iframe>', r"[Відео: \1]", text, flags=re.S)
    text = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
                  lambda m: f"[{m.group(2)}]({abs_link(m.group(1))})", text, flags=re.S)
    text = re.sub(r"<br\s*/?>", "\n", text)
    text = re.sub(r"</(span|small)>", " ", text)
    text = re.sub(r"</(p|div|li|tr|h\d)>", "\n", text)
    text = re.sub(r"<li[^>]*>", "- ", text)
    text = re.sub(r"<(strong|b)>(.*?)</\1>", r"**\2**", text, flags=re.S)
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = re.sub(r"\]\(([^)\s]+)\)", lambda m: "](" + abs_link(m.group(1)) + ")", text)
    text = re.sub(r"\s*\{\s*[:.#][^}]*\}", "", text)  # attr_list
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"(?<=\S)  +(?=\S)", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ---------- частина 1: статті сайту ----------
nav = []
for line in (ROOT / "mkdocs.yml").read_text(encoding="utf-8").splitlines():
    m = re.search(r"([\w/\-]+\.md)\s*$", line)
    if m and m.group(1) not in nav:
        nav.append(m.group(1))
all_docs = sorted(str(p.relative_to(DOCS)).replace("\\", "/") for p in DOCS.rglob("*.md"))
order = [r for r in nav if r in all_docs] + [r for r in all_docs if r not in nav]

site_parts = []
for rel in order:
    _, src = front_matter((DOCS / rel).read_text(encoding="utf-8"))
    body = convert(src, rel)
    if not body.startswith("# "):
        body = f"# {rel}\n\n" + body
    title, _, rest = body.partition("\n")
    site_parts.append(f"{title}\n\nДжерело: {url_of(rel)}\n{rest}")

# ---------- частини 2 і 3: kb/ і приватний aedoc-kb ----------
def collect(folder, label):
    parts = []
    if not folder.exists():
        return parts
    for path in sorted(folder.rglob("*.md")):
        rel = str(path.relative_to(folder)).replace("\\", "/")
        if path.name.startswith("_") or path.name.lower() == "readme.md" or rel.startswith("."):
            continue  # шаблони, чернетки, README
        meta, src = front_matter(path.read_text(encoding="utf-8"))
        body = convert(src)
        title = meta.get("тема") or path.stem
        info = " · ".join(f"{k}: {v}" for k, v in meta.items() if k != "тема")
        head = f"# {title}\n\nДжерело: {label} ({rel}), посилання клієнту не давати"
        if info:
            head += f"\n{info}"
        parts.append(f"{head}\n\n{body}")
    return parts

kb_parts = collect(KB, "kb")
private_parts = collect(PRIVATE, "закрите, aedoc-kb")

today = datetime.date.today().strftime("%d.%m.%Y")
out = [
    "# База знань AEDOC\n\n"
    f"Зібрано {today}. Статей сайту: {len(site_parts)}, питань-відповідей: {len(kb_parts)}, "
    f"закритих матеріалів: {len(private_parts)}.\n"
    "Кожен матеріал починається із заголовка `# ` і рядка `Джерело:`.\n"
    "Для статей сайту `Джерело` — адреса сторінки, її можна давати клієнту.\n"
    "Розділи 2 і 3 на сайті не опубліковані: посилань на них клієнту не давати.\n"
    "Скриншоти замінено їхнім описом у форматі [Скриншот: …].",
    "# РОЗДІЛ 1. Статті довідки dovidka.aedoc.com.ua",
    *site_parts,
]
if kb_parts:
    out += ["# РОЗДІЛ 2. Питання-відповіді", *kb_parts]
if private_parts:
    out += ["# РОЗДІЛ 3. Закриті матеріали (відомі помилки, обходи, внутрішнє)", *private_parts]

OUT.write_text("\n\n---\n\n".join(out) + "\n", encoding="utf-8")
print(f"{OUT}: сайт {len(site_parts)}, kb/ {len(kb_parts)}, aedoc-kb {len(private_parts)}"
      f"{'' if PRIVATE.exists() else ' (приватний репозиторій не знайдено: ' + str(PRIVATE) + ')'}, "
      f"{len(OUT.read_text(encoding='utf-8'))} символів")
