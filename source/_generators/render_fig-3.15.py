#!/usr/bin/env python3
"""Generate Fig 3.15 'Prefabricated Typical Wick Drain' (JGS 2006) redraw.
Clean table of wick-drain cross-sections: Composite (ladder/corrugated/cell
cores) vs Single (non-woven fabric), each between geotextile filter lines.
Minor-corrections pass: tidy layout, consistent English labels.
"""
import math
from PIL import Image, ImageDraw, ImageFont

SVG = ['<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="1240" viewBox="0 0 900 620">']
PNG = Image.new("RGB", (1800, 1240), "white")
D = ImageDraw.Draw(PNG)
try:
    FB = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 24)
    FN = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 20)
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


def rect(x1, y1, x2, y2, w=1.6, col="#111"):
    SVG.append(f'<rect x="{x1}" y="{y1}" width="{x2-x1}" height="{y2-y1}" stroke="{col}" stroke-width="{w}" fill="none"/>')
    D.rectangle([x1 * rx, y1 * ry, x2 * rx, y2 * ry], outline=col, width=int(w * rx))


def text(cx, cy, s, bold=False, size=20, color="#111", anchor="mm"):
    SVG.append(f'<text x="{cx}" y="{cy}" font-family="Arial" font-size="{size/2}" font-weight="{"bold" if bold else "normal"}" fill="{color}" text-anchor="{anchor}" dominant-baseline="middle">{s}</text>')
    fnt = FB if bold else FN
    D.text((cx * rx, cy * ry), s, fill=color, font=fnt, anchor="mm")


def horizontal_core(x1, x2, cy, pattern):
    """Draw a wick drain cross-section: outer geotextile filter lines + core pattern."""
    line(x1, cy - 22, x2, cy - 22, 2.2, "#222")          # filter (top)
    line(x1, cy + 22, x2, cy + 22, 2.2, "#222")          # filter (bottom)
    if pattern == "ladder":
        line(x1, cy - 12, x2, cy - 12, 1.3, "#444")
        line(x1, cy + 12, x2, cy + 12, 1.3, "#444")
        for k in range(5):
            lx = x1 + (x2 - x1) * (k + 0.5) / 5
            line(lx, cy - 12, lx, cy + 12, 1.2, "#444")
    elif pattern == "corrugated":
        n = 10
        pts = []
        for i in range(n + 1):
            xv = x1 + (x2 - x1) * i / n
            yv = cy - 12 if i % 2 == 0 else cy + 12
            pts.append((xv, yv))
        for i in range(len(pts) - 1):
            line(*pts[i], *pts[i + 1], 1.4, "#444")
    elif pattern == "cell":
        # three rectangular cells side by side
        wcell = (x2 - x1) / 3
        for c in range(3):
            cx0 = x1 + c * wcell
            rect(cx0 + 3, cy - 14, cx0 + wcell - 3, cy + 14, 1.4, "#444")
    elif pattern == "nonwoven":
        # dashed fill to imply fabric
        for yy in range(int(cy - 12), int(cy + 13), 6):
            line(x1, yy, x2, yy, 1.2, "#888", "3,4")


# ---- grid ----
# table borders
rect(120, 70, 880, 590, 2)
# header separator + left col separator
line(120, 100, 880, 100, 2)
line(300, 100, 300, 590, 2)
# composite / single divider
line(120, 430, 880, 430, 2)

# headers
text(210, 85, "Structure", True, 21)
text(590, 85, "Cross-section of Wick Type Drains", True, 21)

# left column group labels
text(210, 130, "Composite", True, 20)
text(210, 152, "structure", True, 20)
text(210, 500, "Single", True, 20)
text(210, 522, "structure", True, 20)

# composite rows (with separators)
for i, (yy, name) in enumerate([(175, "Ladder-type core"), (295, "Corrugated core"), (405, "Cell-type core")], 1):
    line(300, yy + 70, 880, yy + 70, 1.2, "#ccc")
    text(385, yy + 8, name, False, 20)
    horizontal_core(420, 840, yy + 8, ["ladder", "corrugated", "cell"][i - 1])

# single row
text(385, 505, "Non-woven fabric (flat core)", False, 20)
horizontal_core(420, 840, 505, "nonwoven")

SVG.append("</svg>")
open("C:/Users/Owner/trading-agent/hazarika-textbook-figures/source/fig-3.15-wick-drain-cross-sections.svg", "w").write("\n".join(SVG))
PNG.save("C:/Users/Owner/trading-agent/hazarika-textbook-figures/export/fig-3.15-wick-drain-cross-sections.png")
print("saved fig 3.15", PNG.size)
