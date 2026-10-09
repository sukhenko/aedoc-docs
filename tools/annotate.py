"""Обробка скріншотів для довідки AEDOC: обрізка, розмиття, легка різкість, червоні рамки з номерами.

Використання:
    python3 tools/annotate.py jobs.json

jobs.json — список завдань:
[
  {
    "src": "raw/zoom-1.jpg",            # вихідний знімок (zoom з computer use)
    "out": "docs/aed/img/priklad-1.png", # куди зберегти PNG
    "crop": [0, 0, 1530, 176],           # необов'язково: x0, y0, x1, y1
    "blur": [[706, 212, 848, 243]],      # необов'язково: ІПН, шлях до ключа, ПІБ
    "boxes": [[1, [730, 86, 888, 162], "tl"]]  # номер, рамка, де номер: tl | tr | bl
  }
]
Координати — у пікселях вихідного знімка (до обрізки).
"""
import json
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RED = (220, 30, 30)
FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 17)


def badge(d, n, x, y):
    r = 13
    d.ellipse((x - r, y - r, x + r, y + r), fill=RED, outline='white', width=2)
    d.text((x, y + 1), str(n), fill='white', font=FONT, anchor='mm')


def process(job):
    im = Image.open(job['src']).convert('RGB')
    for b in job.get('blur', []):
        im.paste(im.crop(b).filter(ImageFilter.GaussianBlur(12)), tuple(b[:2]))
    im = im.filter(ImageFilter.UnsharpMask(radius=1, percent=60, threshold=3))
    d = ImageDraw.Draw(im)
    boxes = job.get('boxes', [])
    for _, box, _ in boxes:
        d.rounded_rectangle(box, radius=6, outline=RED, width=3)
    for n, (x0, y0, x1, y1), pos in boxes:
        bx = x1 if pos == 'tr' else x0
        by = y1 if pos == 'bl' else y0
        badge(d, n, min(max(bx, 14), im.width - 14), min(max(by, 14), im.height - 14))
    if job.get('crop'):
        im = im.crop(job['crop'])
    im.save(job['out'], optimize=True)
    print(job['out'], im.size)


if __name__ == '__main__':
    for j in json.load(open(sys.argv[1], encoding='utf-8')):
        process(j)
