"""Збирає базу знань для ІІ в один файл aedoc-kb.md.

    python tools/build_kb.py                 # з кореня репозиторію aedoc-docs
    python tools/build_kb.py <repo> <out.md>

Частина 1 — статті сайту з docs/ (у порядку меню mkdocs.yml, з посиланнями на dovidka).
Частина 2 — внутрішні матеріали з kb/ (не публікуються на сайті).
"""
import re, sys, html, posixpath, datetime
from urllib.parse import urljoin
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "aedoc-kb.md"
DOCS, KB = ROOT / "docs", ROOT / "kb"
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

# ---------- частина 2: kb/ ----------
kb_parts = []
if KB.exists():
    for path in sorted(KB.rglob("*.md")):
        rel = str(path.relative_to(ROOT)).replace("\\", "/")
        if path.name.startswith("_"):  # шаблони і чернетки
            continue
        meta, src = front_matter(path.read_text(encoding="utf-8"))
        body = convert(src)
        title = meta.get("тема") or path.stem
        info = " · ".join(f"{k}: {v}" for k, v in meta.items() if k != "тема")
        head = f"# {title}\n\nДжерело: внутрішнє ({rel}), посилання клієнту не давати"
        if info:
            head += f"\n{info}"
        kb_parts.append(f"{head}\n\n{body}")

today = datetime.date.today().strftime("%d.%m.%Y")
out = [
    "# База знань AEDOC\n\n"
    f"Зібрано {today}. Статей сайту: {len(site_parts)}, внутрішніх матеріалів: {len(kb_parts)}.\n"
    "Кожен матеріал починається із заголовка `# ` і рядка `Джерело:`.\n"
    "Для статей сайту `Джерело` — адреса сторінки, її можна давати клієнту.\n"
    "Внутрішні матеріали (розділ 2) не публікуються: посилань на них клієнту не давати.\n"
    "Скриншоти замінено їхнім описом у форматі [Скриншот: …].",
    "# РОЗДІЛ 1. Статті довідки dovidka.aedoc.com.ua",
    *site_parts,
]
if kb_parts:
    out += ["# РОЗДІЛ 2. Внутрішні матеріали (питання-відповіді, відомі помилки)", *kb_parts]

OUT.write_text("\n\n---\n\n".join(out) + "\n", encoding="utf-8")
print(f"{OUT}: статей сайту {len(site_parts)}, з kb/ {len(kb_parts)}, {len(OUT.read_text(encoding='utf-8'))} символів")
