#!/usr/bin/env python3
"""Render Fig 3.16 (mandrel wick-driving machine) to a high-res PNG with PIL,
mirroring source/fig-3.16-mandrel-machine.svg geometry (viewBox 500x760)."""
from PIL import Image, ImageDraw

S = 2.2
W, H = int(500 * S), int(760 * S)
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def pt(x, y):
    return (x * S, y * S)


def line(x1, y1, x2, y2, width, fill="#111", dash=None):
    if dash:
        # manual dashed segment
        sx, sy = pt(x1, y1)
        ex, ey = pt(x2, y2)
        dx, dy = ex - sx, ey - sy
        length = (dx * dx + dy * dy) ** 0.5
        if length == 0:
            return
        nx, ny = dx / length, dy / length
        on, off = dash
        pos = 0.0
        while pos < length:
            seg = min(on, length - pos)
            d.line(
                [(sx + nx * pos, sy + ny * pos), (sx + nx * (pos + seg), sy + ny * (pos + seg))],
                fill=fill, width=int(width * S),
            )
            pos += seg + off
    else:
        d.line([pt(x1, y1), pt(x2, y2)], fill=fill, width=int(width * S))


def rect(x, y, w, h, fill=None, outline="#111", r=None, width=2):
    d.rounded_rectangle(
        [pt(x, y), pt(x + w, y + h)],
        radius=int((r or 0) * S),
        fill=fill, outline=outline, width=int(width * S),
    )


def circle(cx, cy, rad, fill=None, outline="#111", width=2):
    d.ellipse(
        [pt(cx - rad, cy - rad), pt(cx + rad, cy + rad)],
        fill=fill, outline=outline, width=int(width * S),
    )


def hatch(x0, x1, y0, y1, spacing, width=1, color="#c0c0c0"):
    step = spacing * S
    yy = y0 * S
    while yy < y1 * S:
        d.line([(x0 * S, yy), (x1 * S, yy - (x1 - x0) * S)], fill=color, width=int(width * S))
        yy += step


# ── Soil band (soft ground below surface) ──
hatch(25, 475, 520, 760, 12, 1, "#c9c9c9")
hatch(120, 230, 520, 760, 8, 1, "#b5b5b5")
hatch(270, 380, 520, 760, 8, 1, "#b5b5b5")

# ── Ground surface ──
line(25, 520, 475, 520, 3)

# ── Hollow mandrel pipe ──
line(238, 200, 238, 690, 3)
line(262, 200, 262, 690, 3)
line(238, 690, 262, 690, 3)

# ── Wick drain (dashed) ──
line(250, 205, 250, 688, 1.4, "#333", dash=(int(8 * S), int(5 * S)))

# ── Driving head atop mandrel ──
rect(231, 185, 38, 22, fill="#e8e8e8", width=2)

# ── Crawler tracks ──
rect(140, 448, 72, 72, fill="#2e2e2e", r=30, width=2)
rect(288, 448, 72, 72, fill="#2e2e2e", r=30, width=2)
circle(160, 484, 16, fill="#111", outline="#111")
circle(192, 484, 16, fill="#111", outline="#111")
circle(308, 484, 16, fill="#111", outline="#111")
circle(340, 484, 16, fill="#111", outline="#111")

# ── Base frame ──
line(150, 452, 350, 452, 5)

# ── Hull / cab ──
d.polygon(
    [
        pt(176, 300), pt(324, 300), pt(334, 330), pt(334, 438),
        pt(166, 438), pt(166, 330),
    ],
    fill="#f4f4f4", outline="#111", width=int(2 * S),
)
# cab window
d.polygon(
    [pt(192, 312), pt(250, 312), pt(258, 336), pt(250, 384), pt(192, 384), pt(184, 336)],
    fill="#dfebf5", outline="#111", width=int(1.2 * S),
)
# mandrel passage hint inside hull (dashed)
line(250, 336, 250, 438, 1.2, dash=(int(3 * S), int(4 * S)))

# ── Mast (tower) right of centre ──
line(262, 40, 262, 300, 3)
line(280, 40, 280, 300, 3)
line(258, 70, 284, 70, 1.2)
line(258, 140, 284, 140, 1.2)
line(258, 210, 284, 210, 1.2)

# ── Diagonal support boom ──
line(271, 48, 100, 206, 6)

# ── Pulleys ──
circle(271, 30, 9, width=2.5)
circle(100, 206, 11, width=2.5)

# ── Rigging ──
line(271, 30, 100, 206, 1.4, "#444")
line(262, 33, 250, 185, 1.4, "#444")
line(262, 200, 250, 200, 1.2, "#444")

# ── Surface/fill marks near tracks ──
for sx in (148, 156, 164, 296, 304, 312):
    line(sx, 520, sx + 8, 506, 1.2)

# ── Labels (small tags, English) ──
from PIL import ImageFont
try:
    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", size=int(11.5 * S))
except Exception:
    font = ImageFont.load_default()
FSZ = 11.5 * S


def tag(cx, cy, text):  # cx,cy = text anchor centre in viewBox units
    w = font.getbbox(text)[2] - font.getbbox(text)[0]
    tx, ty = pt(cx, cy)
    rw, rh = w + 8, FSZ + 6
    d.rounded_rectangle(
        [tx - rw / 2, ty - rh / 2, tx + rw / 2, ty + rh / 2],
        radius=2, fill="white", outline="#999999", width=1,
    )
    d.text((tx, ty), text, fill="#111111", font=font, anchor="mm")


tag(307, 26, "Pulley")
tag(307, 66, "Mast")
tag(112, 108, "Boom")
tag(315, 188, "Driving head")
tag(297, 328, "Mandrel")
tag(303, 636, "Wick drain")
tag(122, 456, "Crawler")
tag(400, 510, "Ground line")
tag(396, 640, "Soft ground")

img.save("C:/Users/Owner/trading-agent/hazarika-textbook-figures/export/fig-3.16-mandrel-machine.png")
print("saved", img.size)
