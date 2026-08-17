#!/usr/bin/env python3
"""Generate Fig 3.16 v2 'Mandrel-type Machine for Wick Driving' (SVG+PNG).

v2 improvements over v1:
- Uses figkit Canvas for consistent primitives + tag() labels
- Proper soil rendering with soil("clay") preset
- Better machine rendering: detailed crawler tracks, cab, mast
- Sand drain shown with graded grains inside mandrel
- All labels use tag() for readability over hatching
- Consistent palette, better proportions
"""
import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from figkit import Canvas

c = Canvas(500, 760)

INK = "#1a1a1a"
GREY = "#666"
DARK = "#2e2e2e"

# ---------- soil band (soft ground below surface) ----------
c.soil(25, 520, 475, 760, "clay", seed=1)
# ---------- ground surface ----------
c.line(25, 520, 475, 520, w=3, color=INK)

# ---------- hollow mandrel pipe (double-wall) ----------
c.line(238, 200, 238, 690, w=3, color=INK)
c.line(262, 200, 262, 690, w=3, color=INK)
c.line(238, 690, 262, 690, w=3, color=INK)  # bottom cap

# ---------- wick drain inside mandrel (dashed) ----------
c.line(250, 205, 250, 688, w=1.4, color="#333", dash="8,5")
# graded grains along the wick drain
c.grains(244, 210, 256, 680, n=15, r_min=1.0, r_max=2.0,
         color="#666", seed=16, grade=True)

# ---------- driving head atop mandrel ----------
c.rect(231, 185, 269, 207, w=2, fill="#e8e8e8", color=INK)
# detail lines on driving head
c.line(235, 192, 265, 192, w=1.0, color=GREY)
c.line(235, 200, 265, 200, w=1.0, color=GREY)

# ---------- crawler tracks (continuous track shape) ----------
# left track
c.rect(140, 448, 212, 520, w=2, fill=DARK, color=INK)
# track wheels
for wx in (152, 170, 188, 200):
    c.circle(wx, 484, 10, fill="#111", stroke=INK, sw=1.5)
# track surface marks
for sx in range(144, 210, 6):
    c.line(sx, 520, sx + 3, 514, w=1.0, color="#444")

# right track
c.rect(288, 448, 360, 520, w=2, fill=DARK, color=INK)
for wx in (300, 318, 336, 348):
    c.circle(wx, 484, 10, fill="#111", stroke=INK, sw=1.5)
for sx in range(292, 358, 6):
    c.line(sx, 520, sx + 3, 514, w=1.0, color="#444")

# ---------- base frame ----------
c.line(150, 452, 350, 452, w=5, color=INK)

# ---------- hull / cab ----------
c.polygon([
    (176, 300), (324, 300), (334, 330), (334, 438),
    (166, 438), (166, 330),
], fill="#f4f4f4", outline=INK, w=2)

# cab window
c.polygon([
    (192, 312), (250, 312), (258, 336), (250, 384),
    (192, 384), (184, 336),
], fill="#dfebf5", outline=INK, w=1.5)

# mandrel passage (dashed inside hull)
c.line(250, 336, 250, 438, w=1.2, color=GREY, dash="3,4")

# ---------- mast (tower) ----------
c.line(262, 40, 262, 300, w=3, color=INK)
c.line(280, 40, 280, 300, w=3, color=INK)
# cross-bracing
c.line(258, 70, 284, 70, w=1.2, color=GREY)
c.line(258, 140, 284, 140, w=1.2, color=GREY)
c.line(258, 210, 284, 210, w=1.2, color=GREY)
# diagonal bracing
c.line(262, 70, 280, 140, w=1.0, color="#aaa")
c.line(280, 70, 262, 140, w=1.0, color="#aaa")
c.line(262, 140, 280, 210, w=1.0, color="#aaa")
c.line(280, 140, 262, 210, w=1.0, color="#aaa")

# ---------- diagonal support boom ----------
c.line(271, 48, 100, 206, w=6, color=INK)
# boom detail (interior line)
c.line(271, 52, 104, 204, w=1.5, color="#888")

# ---------- pulleys ----------
c.circle(271, 30, 9, fill="#eee", stroke=INK, sw=2.5)
c.circle(271, 30, 3, fill=INK)
c.circle(100, 206, 11, fill="#eee", stroke=INK, sw=2.5)
c.circle(100, 206, 3, fill=INK)

# ---------- rigging (cables) ----------
c.line(271, 30, 100, 206, w=1.4, color="#444")
c.line(262, 33, 250, 185, w=1.4, color="#444")
c.line(262, 200, 250, 200, w=1.2, color="#444")

# ---------- surface/fill marks near tracks ----------
for sx in (148, 156, 164, 296, 304, 312):
    c.line(sx, 520, sx + 8, 506, w=1.2, color="#888")

# ---------- labels (tag for readability) ----------
c.tag(307, 26, "Pulley", size=13)
c.tag(307, 66, "Mast", size=13)
c.tag(112, 108, "Boom", size=13)
c.tag(315, 188, "Driving head", size=13)
c.tag(297, 328, "Mandrel", size=13)
c.tag(303, 636, "Wick drain", size=13)
c.tag(122, 456, "Crawler", size=13)
c.tag(400, 510, "Ground line", size=13)
c.tag(396, 640, "Soft ground", size=13)

# ---------- save ----------
repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
c.save(f"{repo}/source/fig-3.16-mandrel-machine.svg",
       f"{repo}/export/fig-3.16-mandrel-machine.png")
print("saved fig 3.16 v2")
