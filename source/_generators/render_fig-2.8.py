#!/usr/bin/env python3
"""Generate Fig 2.8 'Loose sand and Vibration' redraw (SVG + PNG from one geometry).
3 panels: loose saturated -> liquefied during vibration -> re-settled densified."""
import math, random
from PIL import Image, ImageDraw, ImageFont

SVG = [r"""<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="680" viewBox="0 0 900 340">"""]
PNG = Image.new("RGB", (1800, 680), "white")
D = ImageDraw.Draw(PNG)
try:
    F = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)
    FN = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 19)
except Exception:
    F = FN = ImageFont.load_default()
S = 2.0  # px per unit
TEXT = []  # (cx, cy, text, bold, anchor)

# ---------------- helpers ----------------
def circle(x, y, r, fill="#333"):
    SVG.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>')
    D.ellipse([(x*rx, y*ry), (x*rx + 2*r*rx, y*ry + 2*r*ry)], fill=fill)
rx, ry = S, S

def line(x1, y1, x2, y2, w=1.5, col="#111", dash=None):
    dsh = f' stroke-dasharray="{dash}"' if dash else ""
    SVG.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}"{dsh}/>')
    if dash:
        sx, sy = x1 * rx, y1 * ry
        ex, ey = x2 * rx, y2 * ry
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

def rect(x1, y1, x2, y2, w=1.5, fill="none", col="#111", dash=None):
    dsh = f' stroke-dasharray="{dash}"' if dash else ""
    f = f' fill="{fill}"' if fill != "none" else ""
    SVG.append(f'<rect x="{x1}" y="{y1}" width="{x2-x1}" height="{y2-y1}" stroke="{col}" stroke-width="{w}"{dsh}{f}/>')
    if fill != "none":
        D.rectangle([x1*rx, y1*ry, x2*rx, y2*ry], fill=fill)
    D.rectangle([x1*rx, y1*ry, x2*rx, y2*ry], outline=col, width=int(w*rx))

def arrow(x1, y1, x2, y2, w=1.5, col="#111", dash=None, head=8):
    line(x1, y1, x2, y2, w, col, dash)
    ang = math.atan2(y2-y1, x2-x1)
    for s in (1, -1):
        a = ang + s * 2.6
        hx = x2 + head*math.cos(a)
        hy = y2 + head*math.sin(a)
        line(x2, y2, hx, hy, 1.5, col)

def cur(d1, stroke, col, dash=None):
    dsh = f' stroke-dasharray="{dash}"' if dash else ""
    pts = " ".join(f"{x},{y}" for x, y in d1)
    SVG.append(f'<path d="M {pts}" fill="none" stroke="{col}" stroke-width="{stroke}"{dsh}/>')
    if dash:
        on, off = map(float, dash.split(","))
        for i in range(len(d1) - 1):
            sx, sy = d1[i][0] * rx, d1[i][1] * ry
            ex, ey = d1[i + 1][0] * rx, d1[i + 1][1] * ry
            dx, dy = ex - sx, ey - sy
            L = (dx * dx + dy * dy) ** 0.5
            if L == 0:
                continue
            nx, ny = dx / L, dy / L
            pos = 0.0
            while pos < L:
                seg = min(on, L - pos)
                D.line([(sx + nx * pos, sy + ny * pos), (sx + nx * (pos + seg), sy + ny * (pos + seg))], fill=col, width=int(stroke * rx))
                pos += seg + off
    else:
        D.line([(x * rx, y * ry) for x, y in d1], fill=col, width=int(stroke * rx))

def text(cx, cy, s, bold=True, size_px=22, fill="#111"):
    SVG.append(f'<text x="{cx}" y="{cy}" font-family="Arial" font-size="{size_px/2}" font-weight="{"bold" if bold else "normal"}" fill="{fill}" text-anchor="middle" dominant-baseline="middle">{s}</text>')
    fnt = F if bold else FN
    D.text((cx*rx, cy*ry), s, fill=fill, font=fnt, anchor="mm")

# ---------------- geometry ----------------
PANELS = [(22, 286), (318, 582), (614, 878)]
Y1, Y2 = 40, 300  # soil box top/bottom
loose = [(60,180),(92,150),(126,190),(150,150),(184,180),(210,150),(244,180),(78,232),(118,225),(156,235),(200,228),(232,235),(120,280),(180,272),(238,278)]  # sparse, tall
liq = [(60,190),(100,205),(140,180),(180,210),(215,190),(250,205),(80,150),(118,150),(155,158),(198,150),(238,158),(60,262),(96,265),(140,258),(180,262),(222,260),(250,262)]  # scattered in water
def dense_rows(x0, x1, ytop, r=11, cols=5):
    pts = []
    y = ytop
    while y + 2*r <= Y2 - 8:
        n = cols if len(pts) == 0 else (cols if True else cols)
        row = [(x0 + i*(x1-x0)/(n-1), y) for i in range(n)]
        pts += row
        y += 2*r - 6
    return pts
dense = dense_rows(PANELS[2][0]+30, PANELS[2][1]-30, 200)  # shorter layer

# ---------------- draw ----------------
# title watermark none

# Panel boxes
for (px0, px1) in PANELS:
    rect(px0, Y1, px1, Y2, 2)

# --- Panel 1: loose & saturated ---
for (x, y) in loose:
    circle(x, y, 10, "#4a4a4a")
text(154, 24, "① Loose & saturated sand  (before vibration)", True, 21)
text(70, 130, "Pore water", False, 17)
arrow(96, 132, 112, 172, 1.2, "#222")
text(226, 250, "Sand particle", False, 17)
arrow(216, 240, 200, 196, 1.2, "#222")

# --- Panel 2: during vibration (liquefied/muddy) ---
liq_rel = [(60,190),(100,205),(140,180),(180,210),(215,190),(250,205),
           (80,150),(118,150),(155,158),(198,150),(238,158),
           (60,262),(96,265),(140,258),(180,262),(222,260),(250,262)]
for (x, y) in [(x2 + PANELS[1][0], y2) for (x2, y2) in liq_rel]:
    circle(x, y, 9, "#6a6a6a")
# wavy water lines (inside panel 2)
for wx in (336 + 62 * i for i in range(4)):
    for dy in (170, 182, 194):
        line(wx, dy + 8, wx + 22, dy + 6, 1.4, "#5b9bd5")
text(450, 24, "② During vibration — grains lose contact", True, 21)
text(450, 326, "silt/water mixture behaves like a slurry", False, 15, "#555")

# --- Panel 3: re-settled densified ---
for (x, y) in dense:
    circle(x, y, 11, "#333333")
# original surface dashed line + settlement arrows
line(PANELS[2][0]+10, 150, PANELS[2][1]-10, 150, 1.5, "#888", "7,5")
for sx in (PANELS[2][0]+70, 746, PANELS[2][1]-70):
    arrow(sx, 168, sx, 192, 1.6, "#444")
# sand boils (upward dashed with end dots)
for bx in (PANELS[2][0]+40, PANELS[2][1]-55):
    cur([(bx, 196), (bx+8, 165), (bx+4, 140)], 1.5, "#2e75b6", "6,4")
    circle(bx+4, 136, 3, "#2e75b6")
text(746, 24, "③ After vibration — re-settled & densified", True, 21)
text(746, 326, "settlement  ·  sand boils (pore water expelled)", False, 15, "#555")

# leading click?
SVG.append("</svg>")
open(src := "C:/Users/Owner/trading-agent/hazarika-textbook-figures/source/fig-2.8-loose-sand-vibration.svg", "w").write("".join(SVG))
PNG.save(exp := "C:/Users/Owner/trading-agent/hazarika-textbook-figures/export/fig-2.8-loose-sand-vibration.png")
print("saved:", src, PNG.size)
