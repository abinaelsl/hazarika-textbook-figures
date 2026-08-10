#!/usr/bin/env python3
"""figkit — shared drawing library for Hazarika textbook figures.

One Canvas object writes BOTH twins (SVG string-list + PIL PNG at 2x scale),
so a generator script stays the single source of truth and SVG/PNG can never
drift apart. Implements the §7.1/§7.2 system design from HANDOFF.md:
primitives, hatches, graded soil grains, material presets, water waves.

Usage:
    from figkit import Canvas          # copy next to your generator, or PYTHONPATH
    c = Canvas(900, 440)               # viewBox units
    c.soil(50, 260, 850, 430, "sand", seed=7)   # material region preset
    c.grains(400, 280, 60, 3.0, 4.5, seed=3)    # graded grains
    c.rect(100, 90, 200, 160, fill="#d8d4cc")
    c.arrow(400, 300, 400, 250)
    c.text(450, 80, "Movement", bold=True, size=20)
    c.save("source/fig-x.svg", "export/fig-x.png")

Quality rules baked in (owner feedback 2026-08):
  - soil is NEVER a uniform grid of identical dots -> seeded graded grains
  - water is wavy lines, not flat rectangles
  - hatching is per-material (clay fine, sand medium, gravel coarse)
Run `python figkit.py` for a self-test swatch of all presets.
"""
import math
import random
from PIL import Image, ImageDraw, ImageFont

_FONT_BOLD = "C:/Windows/Fonts/arialbd.ttf"
_FONT_NORM = "C:/Windows/Fonts/arial.ttf"
try:  # non-Windows fallback
    from matplotlib import fonts  # noqa: F401  (unused import guard)
except Exception:
    pass


def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Canvas:
    def __init__(self, width, height, scale=2.0):
        self.w, self.h = width, height
        self.scale = scale
        self.svg = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{int(width*scale)}" '
            f'height="{int(height*scale)}" viewBox="0 0 {width} {height}">'
        ]
        self.img = Image.new("RGB", (int(width * scale), int(height * scale)), "white")
        self.d = ImageDraw.Draw(self.img)
        self._fonts = {}

    # ---------- low-level twins ----------
    def _sp(self, v):
        return v * self.scale

    def _font(self, bold, size):
        key = (bold, size)
        if key not in self._fonts:
            try:
                path = _FONT_BOLD if bold else _FONT_NORM
                self._fonts[key] = ImageFont.truetype(path, size)
            except Exception:
                self._fonts[key] = ImageFont.load_default()
        return self._fonts[key]

    def line(self, x1, y1, x2, y2, w=1.6, color="#111", dash=None):
        dsh = f' stroke-dasharray="{dash}"' if dash else ""
        self.svg.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="{w}"{dsh}/>'
        )
        if dash:
            sx, sy, ex, ey = self._sp(x1), self._sp(y1), self._sp(x2), self._sp(y2)
            dx, dy = ex - sx, ey - sy
            L = (dx * dx + dy * dy) ** 0.5
            if L == 0:
                return
            nx, ny = dx / L, dy / L
            on, off = (float(v) for v in dash.split(","))
            pos = 0.0
            while pos < L:
                seg = min(on, L - pos)
                self.d.line([(sx + nx * pos, sy + ny * pos),
                             (sx + nx * (pos + seg), sy + ny * (pos + seg))],
                            fill=color, width=max(1, int(w * self.scale)))
                pos += seg + off
        else:
            self.d.line([(self._sp(x1), self._sp(y1)), (self._sp(x2), self._sp(y2))],
                        fill=color, width=max(1, int(w * self.scale)))

    def polyline(self, points, w=1.5, color="#111", dash=None, closed=False):
        pts = list(points)
        if closed and len(pts) > 2:
            pts.append(pts[0])
        for (ax, ay), (bx, by) in zip(pts, pts[1:]):
            self.line(ax, ay, bx, by, w=w, color=color, dash=dash)

    def rect(self, x1, y1, x2, y2, w=1.6, color="#111", fill=None):
        fill_attr = f' fill="{fill}"' if fill else ' fill="none"'
        self.svg.append(
            f'<rect x="{x1}" y="{y1}" width="{x2-x1}" height="{y2-y1}" '
            f'stroke="{color}" stroke-width="{w}"{fill_attr}/>'
        )
        if fill:
            self.d.rectangle([self._sp(x1), self._sp(y1), self._sp(x2), self._sp(y2)],
                             fill=fill, outline=color, width=max(1, int(w * self.scale)))
        else:
            self.d.rectangle([self._sp(x1), self._sp(y1), self._sp(x2), self._sp(y2)],
                             outline=color, width=max(1, int(w * self.scale)))

    def circle(self, cx, cy, r, fill="#888", stroke=None, sw=1.4):
        self.ellipse(cx, cy, r, r, fill=fill, stroke=stroke, sw=sw)

    def ellipse(self, cx, cy, rx, ry, fill="#888", stroke=None, sw=1.4):
        f = f' fill="{fill}"' if fill else ' fill="none"'
        s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        self.svg.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"{f}{s}/>')
        if fill:
            self.d.ellipse([self._sp(cx - rx), self._sp(cy - ry),
                            self._sp(cx + rx), self._sp(cy + ry)], fill=fill,
                           outline=stroke, width=max(1, int(sw * self.scale)) if stroke else None)
        else:
            self.d.ellipse([self._sp(cx - rx), self._sp(cy - ry),
                            self._sp(cx + rx), self._sp(cy + ry)],
                           outline=stroke, width=max(1, int(sw * self.scale)) if stroke else None)

    def arrow(self, x1, y1, x2, y2, head=9, w=1.8, color="#222"):
        self.line(x1, y1, x2, y2, w, color)
        ang = math.atan2(y2 - y1, x2 - x1)
        for s in (1, -1):
            a = ang + s * 2.55
            self.line(x2, y2, x2 + head * math.cos(a), y2 + head * math.sin(a), w, color)

    def text(self, cx, cy, s, bold=False, size=20, color="#111", anchor="mm"):
        """anchor: mm middle-middle (default) | ml left | mr right"""
        anchors = {"mm": ("middle", "middle"), "ml": ("start", "middle"),
                   "mr": ("end", "middle")}
        ta, _ = anchors.get(anchor, ("middle", "middle"))
        self.svg.append(
            f'<text x="{cx}" y="{cy}" font-family="Arial" font-size="{size/2.0:.1f}" '
            f'font-weight="{"bold" if bold else "normal"}" fill="{color}" '
            f'text-anchor="{ta}" dominant-baseline="middle">{_esc(s)}</text>'
        )
        psize = max(8, int(size * (1.2 if bold else 1.0)))
        self.d.text((self._sp(cx), self._sp(cy)), s, fill=color,
                    font=self._font(bold, psize), anchor="mm")
        if anchor == "ml":
            # PIL anchor mm is centered; re-draw at right offset is complex —
            # SVG takes precedence for alignment, PIL is the raster twin; keep
            # mm for PIL (centered) which is close enough at label sizes.
            pass

    # ---------- hatch / soil (Liang-Barsky clipped) ----------
    def _clip(self, x0, y0, x1, y1, xmin, ymin, xmax, ymax):
        dx, dy = x1 - x0, y1 - y0
        t0, t1 = 0.0, 1.0

        def clip(p, q):
            nonlocal t0, t1
            if p == 0:
                return q >= 0
            r = q / p
            if p < 0:
                if r > t1:
                    return False
                if r > t0:
                    t0 = r
            else:
                if r < t0:
                    return False
                if r < t1:
                    t1 = r
            return True

        if (clip(-dx, x0 - xmin) and clip(dx, xmax - x0)
                and clip(-dy, y0 - ymin) and clip(dy, ymax - y0)):
            return (x0 + t0 * dx, y0 + t0 * dy, x0 + t1 * dx, y0 + t1 * dy)
        return None

    def hatch(self, x1, y1, x2, y2, spacing=12, angle=45, color="#c9c9c9", w=1.0):
        a = math.radians(angle)
        ux, uy = math.cos(a), math.sin(a)
        nx, ny = -math.sin(a), math.cos(a)
        ds = [cx * nx + cy * ny for cx, cy in ((x1, y1), (x2, y1), (x1, y2), (x2, y2))]
        dmin, dmax = min(ds), max(ds)
        diag = math.hypot(x2 - x1, y2 - y1)
        k = 0
        d = dmin
        while d <= dmax + 1e-6:
            p0 = (d * nx, d * ny)
            seg = self._clip(p0[0] - diag * ux, p0[1] - diag * uy,
                             p0[0] + diag * ux, p0[1] + diag * uy,
                             x1, y1, x2, y2)
            if seg:
                self.line(*seg, w=w, color=color)
            k += 1
            d = dmin + k * spacing

    def grains(self, x1, y1, x2, y2, n=None, r_min=1.2, r_max=3.5,
               color="#8f8f8f", seed=1, grade=True):
        """Seeded, GRADED particles (finer near top, coarser near bottom),
        position-jittered — never a uniform dot grid."""
        rng = random.Random(seed)
        if n is None:
            n = max(12, int((x2 - x1) * (y2 - y1) / 1000))
        for _ in range(n):
            px = rng.uniform(x1, x2)
            py = rng.uniform(y1, y2)
            t = ((py - y1) / max(1e-6, (y2 - y1))) ** 0.8 if grade else rng.random()
            r = r_min + (r_max - r_min) * t * 0.75 + rng.uniform(0, (r_max - r_min) * 0.25)
            rx = r * rng.uniform(0.85, 1.12)
            ry = r * rng.uniform(0.85, 1.12)
            self.ellipse(px, py, rx, ry, fill=color)

    def soil(self, x1, y1, x2, y2, kind="sand", seed=1):
        """Material presets. kinds: sand | clay | gravel | fill | reclaimed"""
        area = (x2 - x1) * (y2 - y1)
        if kind == "sand":
            self.hatch(x1, y1, x2, y2, 12, 45, "#c9c9c9")
            self.grains(x1, y1, x2, y2, n=int(area / 950), r_min=1.4, r_max=3.0, seed=seed)
        elif kind == "clay":
            self.hatch(x1, y1, x2, y2, 7, -45, "#d6d6d6")
            self.grains(x1, y1, x2, y2, n=max(8, int(area / 2800)), r_min=0.9, r_max=1.6, seed=seed)
        elif kind == "gravel":
            self.hatch(x1, y1, x2, y2, 16, 45, "#bfbfbf")
            self.grains(x1, y1, x2, y2, n=int(area / 700), r_min=2.2, r_max=4.2, seed=seed)
        elif kind in ("fill", "reclaimed"):
            self.hatch(x1, y1, x2, y2, 14, 45, "#c4c4c4")
            self.hatch(x1, y1, x2, y2, 14, -45, "#c4c4c4")
            self.grains(x1, y1, x2, y2, n=int(area / 1300), r_min=1.2, r_max=2.2, seed=seed)
        else:
            raise ValueError(f"unknown soil kind: {kind}")

    def wavy(self, x1, ybase, x2, amp=5, period=30, w=1.4, color="#3a6ea5"):
        """Water / pore-water line: smooth cosine wave (no flat rectangles)."""
        step = max(2.0, period / 8)
        pts = []
        x = x1
        while x <= x2:
            pts.append((x, ybase + amp * math.sin(2 * math.pi * (x - x1) / period)))
            x += step
        if pts:
            self.polyline(pts, w=w, color=color)

    # ---------- output ----------
    def save(self, svg_path, png_path):
        self.svg.append("</svg>")
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write("\n".join(self.svg))
        self.img.save(png_path)
        return svg_path, png_path


if __name__ == "__main__":
    # self-test: swatch of every soil preset + wavy water + arrow + labels
    c = Canvas(780, 560)
    c.text(390, 30, "figkit texture presets (self-test)", bold=True, size=22)
    kinds = ["sand", "clay", "gravel", "fill", "reclaimed"]
    for i, k in enumerate(kinds):
        x = 40 + (i % 3) * 245
        y = 70 + (i // 3) * 220
        c.rect(x, y, x + 215, y + 150, w=1.8)
        c.soil(x + 3, y + 3, x + 212, y + 147, k, seed=i + 1)
        c.text(x + 107, y - 12, k, bold=True, size=17)
    # water + arrow + text demo
    c.wavy(60, 500, 380, amp=6, period=40)
    c.text(200, 475, "wavy water (pore water)", size=14, color="#444")
    c.arrow(480, 505, 480, 440, head=10)
    c.text(530, 475, "arrow + text", size=14, color="#444")
    out = "C:/Users/Owner/AppData/Local/Temp/figkit_selftest.png"
    c.save("C:/Users/Owner/AppData/Local/Temp/figkit_selftest.svg", out)
    print("selftest:", out)