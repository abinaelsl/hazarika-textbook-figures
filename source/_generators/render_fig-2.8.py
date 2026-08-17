#!/usr/bin/env python3
"""Generate Fig 2.8 v2 'Loose sand and Vibration' (SVG+PNG).

v2 improvements over v1:
- Uses figkit Canvas: soil(), grains(), wavy(), tag()
- Graded particles (varied radii, depth-graded) instead of uniform circles
- Proper wavy water lines (cosine) instead of short dashes
- Displacement vectors during vibration (small arrows showing grain movement)
- Dense vs loose packing visibly differs between panels
- Better panel borders, consistent labels with tag()
"""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(__file__))
from figkit import Canvas

c = Canvas(900, 340)

# ---------- panels ----------
PANELS = [(22, 286), (318, 582), (614, 878)]
Y1, Y2 = 40, 300
for (px0, px1) in PANELS:
    c.rect(px0, Y1, px1, Y2, w=2)

# ---------- panel titles ----------
c.badge_title(154, 13, 1, "Loose & saturated sand", bold=True, size=16)
c.text(154, 31, "(before vibration)", size=13, color="#555")
c.badge_title(450, 13, 2, "During vibration —", bold=True, size=16)
c.text(450, 31, "grains lose contact", size=13, color="#555")
c.badge_title(746, 13, 3, "After vibration —", bold=True, size=16)
c.text(746, 31, "re-settled & densified", size=13, color="#555")

# ---------- Panel 1: loose & saturated ----------
# loose packing: fewer, larger, well-spaced grains (seeded, graded)
p1 = PANELS[0]
c.grains(p1[0]+8, Y1+10, p1[1]-8, Y2-10, n=35, r_min=4.0, r_max=7.0,
         color="#4a4a4a", seed=11, grade=True)
# pore water label + arrow
c.tag(70, 60, "Pore water", size=14)
c.arrow(96, 72, 112, 110, head=6, w=1.2, color="#222")
# sand particle label + arrow
c.tag(226, 250, "Sand particle", size=14)
c.arrow(216, 238, 200, 200, head=6, w=1.2, color="#222")
# subtle water indication (wavy line in pore space)
c.wavy(p1[0]+15, 120, p1[1]-15, amp=3, period=40, w=1.0, color="#b8d4f0")

# ---------- Panel 2: during vibration (liquefied) ----------
p2 = PANELS[1]
# grains scattered in water (suspended, more dispersed)
c.grains(p2[0]+8, Y1+10, p2[1]-8, Y2-10, n=40, r_min=3.0, r_max=5.5,
         color="#6a6a6a", seed=22, grade=False)
# wavy water lines (pore water under vibration)
for dy in (100, 140, 180, 220, 260):
    c.wavy(p2[0]+10, dy, p2[1]-10, amp=4, period=30, w=1.2, color="#5b9bd5")
# displacement vectors (small arrows showing grain movement)
rng = random.Random(33)
for _ in range(8):
    gx = p2[0] + 20 + rng.random() * (p2[1] - p2[0] - 40)
    gy = Y1 + 30 + rng.random() * (Y2 - Y1 - 60)
    dx = rng.uniform(-12, 12)
    dy = rng.uniform(-12, 12)
    c.arrow(gx, gy, gx+dx, gy+dy, head=4, w=1.0, color="#3a6ea5")
c.text(450, 326, "silt/water mixture behaves like a slurry", size=13, color="#555")

# ---------- Panel 3: re-settled densified ----------
p3 = PANELS[2]
# dense packing: many small, tightly packed grains
c.grains(p3[0]+8, Y1+10, p3[1]-8, Y2-10, n=220, r_min=2.6, r_max=3.8,
         color="#333333", seed=44, grade=True)
# original surface dashed line
c.line(p3[0]+10, 150, p3[1]-10, 150, w=1.5, color="#888", dash="7,5")
c.tag(p3[0]+60, 142, "original surface", size=12, color="#666")
# settlement arrows (downward)
for sx in (p3[0]+70, 746, p3[1]-70):
    c.arrow(sx, 168, sx, 192, head=7, w=1.6, color="#444")
c.tag(p3[0]+95, 180, "settlement", size=12, color="#444")
# sand boils (upward dashed curves with end dots)
for bx in (p3[0]+40, p3[1]-55):
    pts = [(bx, 196), (bx+8, 165), (bx+4, 140)]
    c.polyline(pts, w=1.5, color="#2e75b6", dash="6,4")
    c.circle(bx+4, 136, 3, fill="#2e75b6")
c.tag(p3[1]-80, 120, "sand boil", size=12, color="#2e75b6")
c.text(746, 326, "settlement  ·  sand boils (pore water expelled)", size=13, color="#555")

# ---------- save ----------
repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
c.save(f"{repo}/source/fig-2.8-loose-sand-vibration.svg",
       f"{repo}/export/fig-2.8-loose-sand-vibration.png")
print("saved fig 2.8 v2")
