#!/usr/bin/env python3
"""Generate Fig 3.14 v2 'Procedures of Sand Drain Method with Casing Pipe' (SVG+PNG).

v2 improvements over v1:
- Uses figkit Canvas: soil(), grains(), tag(), arc()
- Proper soil rendering with soil("clay") preset for the ground
- Sand pile shown with graded grains (not uniform dots)
- Better casing pipe rendering (double-wall with visible thickness)
- Cleaner arrows with consistent direction
- Tag labels for callouts (readable over hatching)
- 7 panels with clear group headers
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_v2 import Canvas

c = Canvas(900, 440)

# ---------- ground (one continuous soil band) ----------
INK = "#1a1a1a"
c.soil(40, 265, 860, 430, "clay", seed=1)
c.line(40, 260, 860, 260, w=3, color=INK)

# ---------- panel columns ----------
centers = [105, 220, 335, 450, 565, 680, 795]
groups = [("Movement", 0, 1), ("Penetration", 1, 3),
          ("Sand supply", 3, 4), ("Sand pile formation", 4, 7)]

# group headers
for name, c0, c1 in groups:
    gx = (centers[c0] + centers[c1 - 1]) / 2
    c.text(gx, 30, name, bold=True, size=20)

# ---------- casing pipe helper ----------
def casing(cx, top, bottom, hammer=True):
    if hammer:
        c.rect(cx-14, top-24, cx+14, top+2, w=2, fill="#d8d4cc")
    # double-wall pipe
    c.line(cx-9, top, cx-9, bottom, w=2.2, color=INK)
    c.line(cx+9, top, cx+9, bottom, w=2.2, color=INK)
    # pipe bottom cap (when in ground)
    if bottom < 430:
        c.line(cx-9, bottom, cx+9, bottom, w=2.2, color=INK)

# ---------- sand pile helper (graded grains) ----------
def sand_pile(cx, y_top, y_bot, seed=5):
    c.grains(cx-10, y_top, cx+10, y_bot, n=20, r_min=1.5, r_max=2.8,
             color="#8f8f8f", seed=seed, grade=True)

# ---------- sand inside pipe ----------
def sand_in_pipe(cx, y_top, y_bot, seed=7):
    c.grains(cx-7, y_top, cx+7, y_bot, n=12, r_min=1.2, r_max=2.0,
             color="#9a9a8e", seed=seed, grade=True)

# ---------- panel states ----------
states = [
    dict(cx=centers[0], bottom=260, sand=None, pile=None, ar=None),
    dict(cx=centers[1], bottom=330, sand=None, pile=None, ar=("d", 300, 325)),
    dict(cx=centers[2], bottom=380, sand=None, pile=None, ar=("d", 360, 375)),
    dict(cx=centers[3], bottom=380, sand=380, pile=None, ar=None),
    dict(cx=centers[4], bottom=330, sand=None, pile=(330, 380), ar=("u", 345, 302)),
    dict(cx=centers[5], bottom=290, sand=None, pile=(290, 380), ar=("u", 305, 262)),
    dict(cx=centers[6], bottom=150, sand=None, pile=(260, 380), ar=None),
]

for st in states:
    cx = st["cx"]
    bot = st["bottom"]
    # sand pile (in ground)
    if st["pile"]:
        sand_pile(cx, st["pile"][0], st["pile"][1], seed=int(cx))
    # sand inside pipe
    if st["sand"]:
        sand_in_pipe(cx, 250, st["sand"] - 4, seed=int(cx + 1))
    # arrows
    if st["ar"]:
        kind, y0, y1 = st["ar"]
        c.arrow(cx + 24, y0, cx + 24, y1, head=8, w=1.6, color="#222")
    # casing + hammer
    if bot >= 200:
        casing(cx, 96, bot, hammer=(bot != 150))
    else:
        casing(cx, 96, 190, hammer=True)

# ---------- callouts ----------
c.tag(centers[1] + 44, 120, "Vibro-hammer", size=13, color="#444")
c.line(centers[1] + 40, 132, centers[1] + 16, 112, w=1.0, color="#888")
c.tag(centers[3] + 44, 150, "Sand", size=13, color="#444")
c.line(centers[3] + 40, 160, centers[3] + 16, 260, w=1.0, color="#888")
c.tag(centers[6] + 40, 350, "Sand drain", size=13, color="#444")
c.line(centers[6] + 35, 358, centers[6] + 10, 320, w=1.0, color="#888")

# ---------- save ----------
repo = "C:/Users/Owner/trading-agent/hazarika-textbook-figures"
c.save(f"{repo}/v2/source/fig-3.14-sand-drain-casing-pipe.svg",
       f"{repo}/v2/export/fig-3.14-sand-drain-casing-pipe.png")
print("saved fig 3.14 v2")
