#!/usr/bin/env python3
"""Generate Fig 1.14 'Change of soil strength by reinforcement' redraw (SVG+PNG).
Panels (a) uniaxial, (b) triaxial unreinforced [RECONSTRUCTED], (c) triaxial
reinforced + imaginary end plate; bottom Mohr-circle comparison (phi envelope,
sigma3R/sigma1R, Delta sigma3). Geometry kept consistent: r = sigma_c * sin(phi),
phi = 30 deg so both circles are tangent to the same envelope.
"""
import math
from PIL import Image, ImageDraw, ImageFont

SVG = ['<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="1280" viewBox="0 0 900 640">']
PNG = Image.new("RGB", (1800, 1280), "white")
D = ImageDraw.Draw(PNG)
try:
    F  = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 24)
    FN = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 20)
    FM = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 17)
except Exception:
    F = FN = FM = ImageFont.load_default()
rx = ry = 2.0

# ---------- primitives ----------
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


def arrow(x1, y1, x2, y2, w=2.0, col="#222", head=10, two=False):
    line(x1, y1, x2, y2, w, col)
    ang = math.atan2(y2 - y1, x2 - x1)
    for s in (1, -1):
        a = ang + s * 2.55
        line(x2, y2, x2 + head * math.cos(a), y2 + head * math.sin(a), w, col)
    if two:
        for s in (1, -1):
            a = ang + math.pi + s * 2.55
            line(x1, y1, x1 + head * math.cos(a), y1 + head * math.sin(a), w, col)


def rect(x1, y1, x2, y2, w=1.6, col="#111", fill="none", dash=None):
    dsh = f' stroke-dasharray="{dash}"' if dash else ""
    f = f' fill="{fill}"' if fill != "none" else ""
    SVG.append(f'<rect x="{x1}" y="{y1}" width="{x2-x1}" height="{y2-y1}" stroke="{col}" stroke-width="{w}"{dsh}{f}/>')
    if fill != "none":
        D.rectangle([x1 * rx, y1 * ry, x2 * rx, y2 * ry], fill=fill)
    D.rectangle([x1 * rx, y1 * ry, x2 * rx, y2 * ry], outline=col, width=int(w * rx))


def circle(cx, cy, r, fill="#888"):
    SVG.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>')
    D.ellipse([(cx - r) * rx, (cy - r) * ry, (cx + r) * rx, (cy + r) * ry], fill=fill)


def arc(cx, cy, r, col="#111", w=2.0, dash=None):
    dsh = f' stroke-dasharray="{dash}"' if dash else ""
    SVG.append(f'<path d="M {cx-r},{cy} A {r},{r} 0 0 1 {cx+r},{cy} M {cx-r},{cy} A {r},{r} 0 0 0 {cx+r},{cy}" fill="none" stroke="{col}" stroke-width="{w}"{dsh}/>')
    # upper semicircle (PIL: angles 180..360 with y-down?)
    bbox = [(cx - r) * rx, (cy - r) * ry, (cx + r) * rx, (cy + r) * ry]
    D.arc(bbox, start=180, end=360, fill=col, width=int(w * rx))
    D.arc(bbox, start=0, end=180, fill=col, width=int(w * rx))


def text(cx, cy, s, bold=False, size=20, color="#111"):
    fs = size
    SVG.append(f'<text x="{cx}" y="{cy}" font-family="Arial" font-size="{fs/2}" font-weight="{"bold" if bold else "normal"}" fill="{color}" text-anchor="middle" dominant-baseline="middle">{s}</text>')
    fnt = F if bold else FN
    D.text((cx * rx, cy * ry), s, fill=color, font=fnt, anchor="mm")


def soil_fill(x1, y1, x2, y2, seed=1, n=26, rmax=3.4):
    import random
    rng = random.Random(seed)
    for _ in range(n):
        px = x1 + (x2 - x1) * rng.random()
        py = y1 + (y2 - y1) * rng.random()
        circle(px, py, 1.2 + rmax * rng.random(), "#b9b3a8")


# ---------- layout ----------
text(160, 26, "(a) Uniaxial compression", True, 28)
text(440, 26, "(b) Triaxial compression", True, 28)
text(700, 26, "(c) Triaxial + reinforcement", True, 28)

# soil element squares (filled with light texture)
def element(cx, cy, size):
    rect(cx - size / 2, cy - size / 2, cx + size / 2, cy + size / 2, 2, fill="#f5f2ec")
    soil_fill(cx - size / 2 + 3, cy - size / 2 + 3, cx + size / 2 - 3, cy + size / 2 - 3, seed=int(cx))

# (a) uniaxial
element(160, 140, 92)
arrow(160, 70, 160, 90, 2.4)         # top sigma1
arrow(160, 210, 160, 190, 2.4)       # bottom sigma1
text(160, 58, "σ₁", True)
text(160, 224, "σ₁", True)

# (b) triaxial unreinforced  [RECONSTRUCTED]
element(440, 150, 92)
arrow(440, 82, 440, 102, 2.4)
arrow(440, 218, 440, 198, 2.4)
arrow(382, 150, 402, 150, 2.4)       # sigma3 left
arrow(498, 150, 478, 150, 2.4)       # sigma3 right
# dashed deformed shape (compressed + bulging)
rect(394, 130, 486, 196, 1.6, "#8a8a8a", dash="6,4")
text(440, 58, "σ₁", True)
text(440, 232, "σ₁", True)
text(368, 150, "σ₃", True)
text(512, 150, "σ₃", True)
text(512, 238, "σ₁ > σ₃", False, 22)
text(622, 112, "Deformed shape", False, size=15, color="#666")
line(610, 118, 496, 150, 1.1, "#888")

# (c) reinforced
element(700, 150, 92)
arrow(700, 82, 700, 102, 2.4)
arrow(700, 218, 700, 198, 2.4)
arrow(642, 150, 662, 150, 2.4)
arrow(758, 150, 738, 150, 2.4)
rect(654, 132, 746, 196, 1.6, "#8a8a8a", dash="6,4")
# reinforcement layers (2 horizontal)
line(656, 143, 744, 143, 2.6, "#333")
line(656, 165, 744, 165, 2.6, "#333")
# tensile arrows on reinforcement
arrow(662, 143, 674, 143, 1.4, "#666", head=6)
arrow(738, 143, 726, 143, 1.4, "#666", head=6)
arrow(662, 165, 674, 165, 1.4, "#666", head=6)
arrow(738, 165, 726, 165, 1.4, "#666", head=6)
text(700, 58, "σ₁", True)
text(700, 232, "σ₁", True)
text(628, 150, "σ₃", True)
text(772, 150, "σ₃", True)
text(700, 238, "σ₁ > σ₃", False, 22)
text(700, 112, "Reinforcement", True, size=15, color="#333")

# imaginary end plate (small inset below c)
line(652, 288, 748, 288, 1.5, "#555", "5,4")
rect(648, 278, 658, 298, 2, "#333")
rect(742, 278, 752, 298, 2, "#333")
arrow(670, 288, 688, 288, 1.3, "#666", head=5)
arrow(730, 288, 712, 288, 1.3, "#666", head=5)
text(700, 268, "Imaginary end plate", False, size=14, color="#555")

# ---------- Mohr diagram (bottom) ----------
# phi = 30deg, r = sigma_c * sin(phi) -> both circles tangent to same envelope
text(120, 330, "Failure envelopes", True, 26)
ox, oy, unit = 170.0, 560.0, 90.0  # origin, sigma scale (1 unit stress = 90px)

# axes
arrow(170, 340, 170, 560, 1.8)      # tau axis
arrow(170, 560, 830, 560, 1.8)      # sigma axis
# envelope from origin at 30 deg
ex = 660
ey = oy - (ex - ox) * math.tan(math.radians(30))
line(ox, oy, ex, ey, 2.0, "#c00")
text(560, ey - 14, "φ", True, size=22, color="#c00")

# inner (unreinforced): sigma_c=2.0, r=1.0 -> sigma3=1.0 sigma1=3.0
c1 = ox + 2.0 * unit
r1 = 1.0 * unit
arc(c1, oy, r1, "#222", 2.0)
# outer (reinforced): sigma_c=4.0, r=2.0 -> sigma3R=2.0 sigma1R=6.0
c2 = ox + 4.0 * unit
r2 = 2.0 * unit
arc(c2, oy, r2, "#347", 2.0)

# axis ticks/labels
text(ox + 1.0 * unit, oy + 20, "σ₃", False, size=20)
text(ox + 3.0 * unit, oy + 20, "σ₁", False, size=20)
text(ox + 2.0 * unit, oy + 20, "σ₃ᵣ", False, size=20, color="#347")
text(ox + 6.0 * unit, oy + 20, "σ₁ᵣ", False, size=20, color="#347")
text(ox + 1.0 * unit, oy + 42, "Δσ₃", True, size=19, color="#347")
# small delta line under axis
line(ox + 1.0 * unit, oy + 34, ox + 2.0 * unit, oy + 34, 1.4, "#347")
line(ox + 1.0 * unit, oy + 30, ox + 1.0 * unit, oy + 38, 1.0, "#347")
line(ox + 2.0 * unit, oy + 30, ox + 2.0 * unit, oy + 38, 1.0, "#347")

text(148, 322, "τ", True, size=24)
text(830, 556, "σ", True, size=24)
text(236, 338, "unreinforced", False, size=14, color="#555")
text(540, 250, "reinforced", False, size=14, color="#347")

SVG.append("</svg>")
open("C:/Users/Owner/trading-agent/hazarika-textbook-figures/source/fig-1.14-soil-strength-reinforcement.svg", "w").write("\n".join(SVG))
PNG.save("C:/Users/Owner/trading-agent/hazarika-textbook-figures/export/fig-1.14-soil-strength-reinforcement.png")
print("saved fig 1.14", PNG.size)
