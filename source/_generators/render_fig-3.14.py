#!/usr/bin/env python3
"""Generate Fig 3.14 'Procedures of Sand Drain Method with Casing Pipe' redraw.
7 panels: Movement -> Penetration -> Sand supply -> Sand-pile formation.
Clean English rebuild of the Nihon Kaiko catalogue scan (minor-corrections pass).
"""
import math
from PIL import Image, ImageDraw, ImageFont

SVG = ['<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="880" viewBox="0 0 900 440">']
PNG = Image.new("RGB", (1800, 880), "white")
D = ImageDraw.Draw(PNG)
try:
    FB = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)
    FN = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 19)
except Exception:
    FB = FN = ImageFont.load_default()
rx = ry = 2.0


def line(x1, y1, x2, y2, w=1.6, col="#111", dash=None):
    dsh = f' stroke-dasharray="{dash}"' if dash else ""
    SVG.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}"{dsh}/>')
    if dash:
        sx, sy, ex, ey = x1 * rx, y1 * ry, x2 * rx, y2 * ry
        dx, dy = ex - sx, ey - sy
        L = (dx * dx + dy * dy) ** 0.5
        nx, ny = dx / L, dy / L
        on, off = map(float, dash.split(","))
        pos = 0.0
        while pos < L:
            seg = min(on, L - pos)
            D.line([(sx + nx * pos, sy + ny * pos), (sx + nx * (pos + seg), sy + ny * (pos + seg))], fill=col, width=int(w * rx))
            pos += seg + off
    else:
        D.line([(x1 * rx, y1 * ry), (x2 * rx, y2 * ry)], fill=col, width=int(w * rx))


def arrow(x1, y1, x2, y2, w=1.8, col="#222", head=9):
    line(x1, y1, x2, y2, w, col)
    ang = math.atan2(y2 - y1, x2 - x1)
    for s in (1, -1):
        a = ang + s * 2.55
        line(x2, y2, x2 + head * math.cos(a), y2 + head * math.sin(a), w, col)


def text(cx, cy, s, bold=False, size=19, color="#111"):
    SVG.append(f'<text x="{cx}" y="{cy}" font-family="Arial" font-size="{size/2}" font-weight="{"bold" if bold else "normal"}" fill="{color}" text-anchor="middle" dominant-baseline="middle">{s}</text>')
    fnt = FB if bold else FN
    D.text((cx * rx, cy * ry), s, fill=color, font=fnt, anchor="mm")


def soil(x1, x2, y1, y2, spacing=11, color="#c9c9c9"):
    for yy in range(int(y1), int(y2), spacing):
        line(x1, yy, x1 + (x2 - x1), yy - (x2 - x1), 1.0, color)


def dots(x_center, y_top, y_bot, radius=2.2, density=5, seed=5):
    import random
    rng = random.Random(seed)
    for _ in range(density * 60):
        px = x_center + (rng.random() - 0.5) * 2.2 * radius * 3
        py = y_top + (y_bot - y_top) * rng.random()
        if abs(px - x_center) <= 24:
            SVG.append(f'<circle cx="{px}" cy="{py}" r="{radius}" fill="#8f8f8f"/>')
            D.ellipse([(px - radius) * rx, (py - radius) * ry, (px + radius) * rx, (py + radius) * ry], fill="#8f8f8f")


# ---- ground (one continuous soil band) ----
soil(40, 860, 265, 430, 12)
line(40, 260, 860, 260, 3)

# panel columns
centers = [105, 220, 335, 450, 565, 680, 795]
groups = [("Movement", 0, 1), ("Penetration", 1, 3), ("Sand supply", 3, 4), ("Sand pile formation", 4, 7)]

# group headers
for name, c0, c1 in groups:
    gx = (centers[c0] + centers[c1 - 1]) / 2
    text(gx, 30, name, True, 20)

# per-panel machine state
def casing(cx, top, bottom, hammer=True):
    if hammer:
        D.rectangle([(cx - 13) * rx, (top - 24) * ry, (cx + 13) * rx, (top + 2) * ry], fill="#d8d4cc", outline="#111", width=3)
        SVG.append(f'<rect x="{cx-13}" y="{top-24}" width="26" height="26" fill="#d8d4cc" stroke="#111" stroke-width="2"/>')
    line(cx - 9, top, cx - 9, bottom, 2.2)
    line(cx + 9, top, cx + 9, bottom, 2.2)


# Panel states: (pipe_bottom, sand_inside_fill_to, pile_from, pile_to, arrow)
states = [
    dict(cx=centers[0], bottom=260, sand=None, pile=None, ar=None),              # 1 movement
    dict(cx=centers[1], bottom=330, sand=None, pile=None, ar=("d", 300, 325)),   # 2 penetration
    dict(cx=centers[2], bottom=380, sand=None, pile=None, ar=("d", 360, 375)),   # 3 full penetration
    dict(cx=centers[3], bottom=380, sand=380, pile=None, ar=None),               # 4 sand supply
    dict(cx=centers[4], bottom=330, sand=None, pile=(330, 380), ar=("u", 345, 302)),   # 5 withdraw UP
    dict(cx=centers[5], bottom=290, sand=None, pile=(290, 380), ar=("u", 305, 262)),   # 6 withdraw UP
    dict(cx=centers[6], bottom=150, sand=None, pile=(260, 380), ar=None),              # 7 complete
]

for st in states:
    cx = st["cx"]; bot = st["bottom"]
    # sand pile (in ground)
    if st["pile"]:
        dots(cx, st["pile"][0], st["pile"][1], radius=2.2, seed=int(cx))
    # sand inside pipe (panel 4)
    if st["sand"]:
        dots(cx, 250, st["sand"] - 4, radius=1.9, seed=int(cx + 1))
    # arrows
    if st["ar"]:
        kind, y0, y1 = st["ar"]
        if kind == "d":
            arrow(cx + 24, y0, cx + 24, y1, 1.6)
        else:
            arrow(cx + 24, y0, cx + 24, y1, 1.6)  # y0 > y1 -> upward (head at top)
    # casing + hammer
    if bot >= 200:
        casing(cx, 96, bot, hammer=(bot != 150))
    else:
        casing(cx, 96, 190, hammer=True)  # lifted out, still on top (panel 7 shows drain)

# callouts
text(centers[1] + 44, 120, "Vibro-hammer", False, 14, "#444")
line(centers[1] + 40, 132, centers[1] + 16, 112, 1.0, "#888")
text(centers[3] + 44, 150, "Sand", False, 14, "#444")
line(centers[3] + 40, 160, centers[3] + 16, 260, 1.0, "#888")

SVG.append("</svg>")
open("C:/Users/Owner/trading-agent/hazarika-textbook-figures/source/fig-3.14-sand-drain-casing-pipe.svg", "w").write("\n".join(SVG))
PNG.save("C:/Users/Owner/trading-agent/hazarika-textbook-figures/export/fig-3.14-sand-drain-casing-pipe.png")
print("saved fig 3.14", PNG.size)
