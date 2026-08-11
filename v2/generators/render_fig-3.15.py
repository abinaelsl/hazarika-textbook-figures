#!/usr/bin/env python3
"""Generate Fig 3.15 v2 'Prefabricated Typical Wick Drain' (JGS 2006) (SVG+PNG).

v2 improvements over v1:
- Uses figkit Canvas for consistent primitives
- Better wick drain cross-section rendering (more detailed cores)
- Proper table with clear structure/cross-section columns
- Geotextile filter shown as textured bands, not just lines
- Consistent spacing and typography
- Ladder / corrugated / cell / nonwoven patterns more distinct
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from figkit_v2 import Canvas

c = Canvas(900, 620)

INK = "#1a1a1a"
GREY = "#444"
LIGHT = "#ccc"

# ---------- table grid ----------
c.rect(120, 70, 880, 590, w=2, color=INK)
c.line(120, 100, 880, 100, w=2, color=INK)  # header separator
c.line(300, 100, 300, 590, w=2, color=INK)  # left col separator
c.line(120, 430, 880, 430, w=2, color=INK)  # composite/single divider

# ---------- headers ----------
c.text(210, 85, "Structure", bold=True, size=21)
c.text(590, 85, "Cross-section of Wick Type Drains", bold=True, size=21)

# ---------- left column group labels ----------
c.text(210, 130, "Composite", bold=True, size=20)
c.text(210, 152, "structure", bold=True, size=20)
c.text(210, 500, "Single", bold=True, size=20)
c.text(210, 522, "structure", bold=True, size=20)

# ---------- wick drain cross-section renderer ----------
def wick_core(x1, x2, cy, pattern):
    """Draw a wick drain cross-section: outer geotextile filter + core pattern."""
    # geotextile filter (top + bottom, textured)
    for yy in (cy - 22, cy + 22):
        c.line(x1, yy, x2, yy, w=2.2, color="#222")
        # texture marks on filter
        for mx in range(int(x1), int(x2), 8):
            c.line(mx, yy - 2, mx, yy + 2, w=0.8, color="#666")

    if pattern == "ladder":
        # two rails + rungs
        c.line(x1, cy - 12, x2, cy - 12, w=1.5, color=GREY)
        c.line(x1, cy + 12, x2, cy + 12, w=1.5, color=GREY)
        for k in range(7):
            lx = x1 + (x2 - x1) * (k + 0.5) / 7
            c.line(lx, cy - 12, lx, cy + 12, w=1.3, color=GREY)
    elif pattern == "corrugated":
        # zigzag wave
        n = 14
        pts = []
        for i in range(n + 1):
            xv = x1 + (x2 - x1) * i / n
            yv = cy - 12 if i % 2 == 0 else cy + 12
            pts.append((xv, yv))
        c.polyline(pts, w=1.5, color=GREY)
        # second corrugation layer
        pts2 = []
        for i in range(n + 1):
            xv = x1 + (x2 - x1) * i / n
            yv = cy - 6 if i % 2 == 0 else cy + 6
            pts2.append((xv, yv))
        c.polyline(pts2, w=1.2, color="#888")
    elif pattern == "cell":
        # three rectangular cells with internal channels
        wcell = (x2 - x1) / 3
        for ci in range(3):
            cx0 = x1 + ci * wcell
            c.rect(cx0 + 3, cy - 14, cx0 + wcell - 3, cy + 14, w=1.4, color=GREY)
            # internal channel line
            c.line(cx0 + 6, cy, cx0 + wcell - 6, cy, w=1.0, color="#888")
    elif pattern == "nonwoven":
        # fabric: dense dashed fill
        for yy in range(int(cy - 14), int(cy + 15), 5):
            c.line(x1, yy, x2, yy, w=1.2, color="#888", dash="3,3")
        # fiber strands (random short lines)
        import random
        rng = random.Random(42)
        for _ in range(20):
            fx = x1 + rng.random() * (x2 - x1)
            fy = cy - 12 + rng.random() * 24
            ang = rng.uniform(0, math.pi)
            c.line(fx, fy, fx + 6 * math.cos(ang), fy + 6 * math.sin(ang),
                   w=1.0, color="#aaa")

# ---------- composite rows ----------
import math
for i, (yy, name, pat) in enumerate([
    (175, "Ladder-type core", "ladder"),
    (295, "Corrugated core", "corrugated"),
    (405, "Cell-type core", "cell"),
], 1):
    c.line(300, yy + 70, 880, yy + 70, w=1.2, color=LIGHT)
    c.text(385, yy + 8, name, size=19)
    wick_core(420, 840, yy + 8, pat)

# ---------- single row ----------
c.text(385, 505, "Non-woven fabric (flat core)", size=19)
wick_core(420, 840, 505, "nonwoven")

# ---------- save ----------
repo = "C:/Users/Owner/trading-agent/hazarika-textbook-figures"
c.save(f"{repo}/v2/source/fig-3.15-wick-drain-cross-sections.svg",
       f"{repo}/v2/export/fig-3.15-wick-drain-cross-sections.png")
print("saved fig 3.15 v2")
