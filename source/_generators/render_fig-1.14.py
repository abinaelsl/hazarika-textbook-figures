#!/usr/bin/env python3
"""Generate Fig 1.14 v2 'Change of soil strength by reinforcement' (SVG+PNG).

v2 improvements over v1:
- Uses figkit Canvas (consistent primitives, soil(), tag())
- Full Mohr CIRCLES (not just semicircle arcs) — physically complete
- Soil elements use soil("sand") texture instead of uniform dots
- Tag labels (white bg) for readability
- Better spacing, reinforcement shown as textured layers
- Consistent palette and font hierarchy

Panels: (a) uniaxial, (b) triaxial unreinforced [reconstructed],
(c) triaxial reinforced + imaginary end plate; bottom Mohr-circle comparison.
Geometry: r = sigma_c * sin(phi), phi=30deg, both circles tangent to envelope.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit import Canvas
import math

c = Canvas(900, 920)

# ---------- palette ----------
INK = "#1a1a1a"
RED = "#c0392b"
BLUE = "#2c5f8a"
GREY = "#888"
SOIL_C = "#a09a8e"

# ---------- panel titles ----------
c.text(160, 26, "(a) Uniaxial compression", bold=True, size=24)
c.text(440, 26, "(b) Triaxial compression", bold=True, size=24)
c.text(700, 26, "(c) Triaxial + reinforcement", bold=True, size=24)

# ---------- soil element helper ----------
def element(cx, cy, size):
    x1, y1 = cx - size/2, cy - size/2
    x2, y2 = cx + size/2, cy + size/2
    c.rect(x1, y1, x2, y2, w=2, fill="#f5f2ec")
    c.soil(x1+3, y1+3, x2-3, y2-3, "sand", seed=int(cx))

# ---------- (a) uniaxial ----------
element(160, 140, 92)
c.arrow(160, 70, 160, 92, head=10, w=2.4)
c.arrow(160, 210, 160, 188, head=10, w=2.4)
c.subtext(160, 58, [("σ",""),("1","sub")], bold=True, size=22)
c.subtext(160, 224, [("σ",""),("1","sub")], bold=True, size=22)

# ---------- (b) triaxial unreinforced [RECONSTRUCTED] ----------
element(440, 150, 92)
c.arrow(440, 82, 440, 102, head=10, w=2.4)
c.arrow(440, 218, 440, 198, head=10, w=2.4)
c.arrow(382, 150, 402, 150, head=10, w=2.4)
c.arrow(498, 150, 478, 150, head=10, w=2.4)
# dashed deformed shape (bulging)
c.rect(394, 130, 486, 196, w=1.6, color="#8a8a8a")
c.line(394, 130, 486, 130, w=1.6, color="#8a8a8a", dash="6,4")
c.line(394, 196, 486, 196, w=1.6, color="#8a8a8a", dash="6,4")
c.line(394, 130, 394, 196, w=1.6, color="#8a8a8a", dash="6,4")
c.line(486, 130, 486, 196, w=1.6, color="#8a8a8a", dash="6,4")
c.subtext(440, 58, [("σ",""),("1","sub")], bold=True, size=22)
c.subtext(440, 232, [("σ",""),("1","sub")], bold=True, size=22)
c.subtext(368, 150, [("σ",""),("3","sub")], bold=True, size=22)
c.subtext(512, 150, [("σ",""),("3","sub")], bold=True, size=22)
c.subtext(512, 238, [("σ",""),("1","sub"),(" > ",""),("σ",""),("3","sub")], size=18, color="#555")
c.tag(622, 112, "Deformed shape", size=14)
c.line(610, 118, 496, 150, w=1.0, color=GREY)

# ---------- (c) reinforced ----------
element(700, 150, 92)
c.arrow(700, 82, 700, 102, head=10, w=2.4)
c.arrow(700, 218, 700, 198, head=10, w=2.4)
c.arrow(642, 150, 662, 150, head=10, w=2.4)
c.arrow(758, 150, 738, 150, head=10, w=2.4)
# dashed deformed shape
c.rect(654, 132, 746, 196, w=1.6, color="#8a8a8a")
c.line(654, 132, 746, 132, w=1.6, color="#8a8a8a", dash="6,4")
c.line(654, 196, 746, 196, w=1.6, color="#8a8a8a", dash="6,4")
c.line(654, 132, 654, 196, w=1.6, color="#8a8a8a", dash="6,4")
c.line(746, 132, 746, 196, w=1.6, color="#8a8a8a", dash="6,4")
# reinforcement layers (2 horizontal, textured lines)
c.line(656, 143, 744, 143, w=3.0, color="#333")
c.line(656, 165, 744, 165, w=3.0, color="#333")
# tensile arrows on reinforcement
c.arrow(662, 143, 674, 143, head=6, w=1.4, color="#666")
c.arrow(738, 143, 726, 143, head=6, w=1.4, color="#666")
c.arrow(662, 165, 674, 165, head=6, w=1.4, color="#666")
c.arrow(738, 165, 726, 165, head=6, w=1.4, color="#666")
c.subtext(700, 58, [("σ",""),("1","sub")], bold=True, size=22)
c.subtext(700, 232, [("σ",""),("1","sub")], bold=True, size=22)
c.subtext(628, 150, [("σ",""),("3","sub")], bold=True, size=22)
c.subtext(772, 150, [("σ",""),("3","sub")], bold=True, size=22)
c.subtext(772, 238, [("σ",""),("1","sub"),(" > ",""),("σ",""),("3","sub")], size=18, color="#555")
c.tag(700, 112, "Reinforcement", bold=True, size=14, color="#333")

# imaginary end plate (inset below c)
c.line(652, 288, 748, 288, w=1.5, color="#555", dash="5,4")
c.rect(648, 278, 658, 298, w=2, color="#333")
c.rect(742, 278, 752, 298, w=2, color="#333")
c.arrow(670, 288, 688, 288, head=5, w=1.3, color="#666")
c.arrow(730, 288, 712, 288, head=5, w=1.3, color="#666")
c.tag(700, 268, "Imaginary end plate", size=13, color="#555")

# ---------- Mohr diagram (bottom) ----------
c.text(500, 425, "Failure envelopes", bold=True, size=22)
ox, oy, unit = 170.0, 700.0, 90.0

# axes
c.arrow(170, 480, 170, 700, head=8, w=1.8)
c.arrow(170, 700, 830, 700, head=8, w=1.8)

# envelope from origin at 30 deg (failure line)
ex = 660
ey = oy - (ex - ox) * math.tan(math.radians(30))
c.line(ox, oy, ex, ey, w=2.0, color=RED)
c.text(560, ey - 14, "φ", bold=True, size=22, color=RED)
# mirror envelope (below axis, for compression)
c.line(ox, oy, ex, oy + (ex - ox) * math.tan(math.radians(30)), w=2.0, color=RED)

# inner (unreinforced): sigma_c=2.0, r=1.0 -> sigma3=1.0 sigma1=3.0
c1 = ox + 2.0 * unit
r1 = 1.0 * unit
c.arc(c1, oy, r1, 180, 360, w=2.2, color=INK)  # upper semicircle
c.arc(c1, oy, r1, 0, 180, w=2.2, color=INK)   # lower semicircle

# outer (reinforced): sigma_c=4.0, r=2.0 -> sigma3R=2.0 sigma1R=6.0
c2 = ox + 4.0 * unit
r2 = 2.0 * unit
c.arc(c2, oy, r2, 180, 360, w=2.2, color=BLUE)
c.arc(c2, oy, r2, 0, 180, w=2.2, color=BLUE)

# axis ticks/labels
c.subtext(ox + 1.0*unit, oy + 20, [("σ",""),("3","sub")], size=20)
c.subtext(ox + 3.0*unit, oy + 20, [("σ",""),("1","sub")], size=20)
c.subtext(ox + 2.0*unit, oy + 20, [("σ",""),("3r","sub")], size=20, color=BLUE)
c.subtext(ox + 6.0*unit, oy + 20, [("σ",""),("1r","sub")], size=20, color=BLUE)
c.subtext(ox + 1.0*unit, oy + 42, [("Δσ",""),("3","sub")], bold=True, size=19, color=BLUE)
# delta line under axis
c.line(ox + 1.0*unit, oy + 34, ox + 2.0*unit, oy + 34, w=1.4, color=BLUE)
c.line(ox + 1.0*unit, oy + 30, ox + 1.0*unit, oy + 38, w=1.0, color=BLUE)
c.line(ox + 2.0*unit, oy + 30, ox + 2.0*unit, oy + 38, w=1.0, color=BLUE)

c.text(184, 477, "τ", bold=True, size=22)
c.text(830, 696, "σ", bold=True, size=24)
c.text(236, 478, "unreinforced", size=14, color="#555")
c.text(540, 390, "reinforced", size=14, color=BLUE)

# ---------- save ----------
repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
c.save(f"{repo}/source/fig-1.14-soil-strength-reinforcement.svg",
       f"{repo}/export/fig-1.14-soil-strength-reinforcement.png")
print("saved fig 1.14 v2")
