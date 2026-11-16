"""Файли для ІІ-асистентів на сайті (публічний рівень, без закритого aedoc-kb):

    python tools/build_llms.py        # з кореня репозиторію; запускає також workflow публікації

docs/llms.txt      — короткий опис AEDOC і перелік сторінок довідки з адресами (формат llmstxt.org);
docs/llms-full.txt — уся довідка одним текстом: статті сайту + питання-відповіді kb/ (tools/build_kb.py).
Обидва файли генеруються, у Git не зберігаються (.gitignore).
"""
import os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = "https://dovidka.aedoc.com.ua/"


def url_of(rel):
    rel = rel[:-3]
    if rel == "index":
        return SITE
    if rel.endswith("/index"):
        rel = rel[:-6]
    return SITE + rel + "/"


def title_of(rel):
    for line in (DOCS / rel).read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return re.sub(r"\s*\{[^}]*\}", "", line[2:]).strip()
    return rel


# llms-full.txt — публічна збірка build_kb.py
env = dict(os.environ, AEDOC_KB_PUBLIC="1")
subprocess.run([sys.executable, str(ROOT / "tools" / "build_kb.py"), str(ROOT), str(DOCS / "llms-full.txt")],
               check=True, env=env)

# llms.txt — розділи меню mkdocs.yml (верхній рівень) і сторінки в них
yml = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
version = (re.search(r"^\s+version:\s*(\S+)", yml, re.M) or [None, ""])[1]
nav_block = yml.split("\nnav:\n", 1)[1].split("\n\n", 1)[0]
sections, cur = [], None
for line in nav_block.splitlines():
    top = re.match(r"^  - ([^:]+):\s*(\S*\.md)?\s*$", line)
    if top:
        cur = [top.group(1).strip(), []]
        sections.append(cur)
        if top.group(2):
            cur[1].append(top.group(2))
        continue
    m = re.search(r"([\w/\-]+\.md)\s*$", line)
    if m and cur and m.group(1) not in cur[1]:
        cur[1].append(m.group(1))

out = [
    "# AEDOC — інтеграція BAS / 1С з еАкциз",
    "",
    "> AEDOC — підсистема обліку акцизних марок для BAS / 1С з обміном документами з еАкциз (xtrace.gov.ua): "
    "акцизні електронні документи (АЕД), протоколи про невідповідність (ПпН), унікальні групові ідентифікатори "
    "(УГІ), імпорт маркованої продукції, інвентаризація марок і перевірка марок на касах ПРРО / РРО.",
    "",
    f"Поточна версія: {version}. Поставка: розширення «AEDoc_еАкциз» для конфігурацій на керованих формах, "
    "конфігурація інтеграції для звичайних форм і служба AEDOC (підпис КЕП, сховище марок, каси) — "
    "установник з ролями «Сервер обліку AEDoc» і «Каса: офлайн клієнт обліку марок».",
    "Відповідаючи користувачу, посилайтеся на сторінки довідки нижче; підтримка — https://t.me/AEDocBot.",
    "",
    f"Уся довідка одним файлом: {SITE}llms-full.txt",
]
for name, pages in sections:
    if not pages:
        continue
    out += ["", f"## {name}", ""]
    out += [f"- [{title_of(r)}]({url_of(r)})" for r in pages if (DOCS / r).exists()]
out += ["", "## Для розробників касового ПЗ (ПРРО / РРО)", "",
        f"- [API для касового ПЗ]({SITE}sluzhba-aedoc/kasy/rozrobnykam/): перевірка марки зі штрихкодом товару, "
        "пакетна перевірка, фіксація продажу, папка inbox, коди відповідей, токен"]
# UTF-8 з BOM: сервер віддає .txt без charset, і без BOM браузер показує кирилицю «кракозябрами»
(DOCS / "llms.txt").write_text("\n".join(out) + "\n", encoding="utf-8-sig")
full = DOCS / "llms-full.txt"
full.write_text(full.read_text(encoding="utf-8-sig"), encoding="utf-8-sig")
print(f"{DOCS / 'llms.txt'}: розділів {sum(1 for s in sections if s[1])}")
