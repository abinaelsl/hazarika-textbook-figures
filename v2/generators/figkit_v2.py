#!/usr/bin/env python3
"""figkit v2 — shared drawing library for Hazarika textbook figures.

Upgraded from v1: adds arc(), tag(), polygon(), dashed polyline, angular
grain particles, depth-graded soil layers, improved text anchoring.

One Canvas object writes BOTH twins (SVG string-list + PIL PNG at 2x scale),
so a generator script stays the single source of truth and SVG/PNG can never
drift apart.

Usage:
    from figkit import Canvas
    c = Canvas(900, 440)
    c.soil(50, 260, 850, 430, "sand", seed=7)
    c.grains(400, 280, 60, 3.0, 4.5, seed=3)
    c.arc(300, 200, 80, 0, 180, "#222")  # semicircle
    c.tag(450, 80, "Movement")           # white-bg label
    c.save("source/fig-x.svg", "export/fig-x.png")

Run `python figkit.py` for a self-test swatch of all presets.
"""
import math
import random
from PIL import Image, ImageDraw, ImageFont

_FONT_BOLD = "C:/Windows/Fonts/arialbd.ttf"
_FONT_NORM = "C:/Windows/Fonts/arial.ttf"


def _esc(s):
    return (s.replace("&", "&").replace("<", "<")
             .replace(">", ">"))


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

    def arc(self, cx, cy, r, start_deg=0, end_deg=360, w=2.0, color="#111", dash=None):
        """Draw an arc (degrees, 0=right, 90=down in SVG coords)."""
        dsh = f' stroke-dasharray="{dash}"' if dash else ""
        sa, ea = math.radians(start_deg), math.radians(end_deg)
        x1 = cx + r * math.cos(sa)
        y1 = cy + r * math.sin(sa)
        x2 = cx + r * math.cos(ea)
        y2 = cy + r * math.sin(ea)
        large = 1 if (end_deg - start_deg) > 180 else 0
        self.svg.append(
            f'<path d="M {x1:.1f},{y1:.1f} A {r},{r} 0 {large} 1 {x2:.1f},{y2:.1f}" '
            f'fill="none" stroke="{color}" stroke-width="{w}"{dsh}/>'
        )
        # PIL arc: angles measured from positive x-axis, counterclockwise
        # but PIL y is down, so we need to negate
        self.d.arc([self._sp(cx - r), self._sp(cy - r),
                    self._sp(cx + r), self._sp(cy + r)],
                   start=start_deg, end=end_deg, fill=color,
                   width=max(1, int(w * self.scale)))

    def polygon(self, points, fill=None, outline="#111", w=1.6):
        pts_str = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
        f = f' fill="{fill}"' if fill else ' fill="none"'
        self.svg.append(
            f'<polygon points="{pts_str}" stroke="{outline}" '
            f'stroke-width="{w}"{f}/>'
        )
        scaled = [(self._sp(x), self._sp(y)) for x, y in points]
        if fill:
            self.d.polygon(scaled, fill=fill, outline=outline,
                           width=max(1, int(w * self.scale)))
        else:
            self.d.polygon(scaled, outline=outline,
                           width=max(1, int(w * self.scale)))

    def arrow(self, x1, y1, x2, y2, head=9, w=1.8, color="#222", two=False):
        self.line(x1, y1, x2, y2, w, color)
        ang = math.atan2(y2 - y1, x2 - x1)
        for s in (1, -1):
            a = ang + s * 2.55
            self.line(x2, y2, x2 + head * math.cos(a), y2 + head * math.sin(a), w, color)
        if two:
            for s in (1, -1):
                a = ang + math.pi + s * 2.55
                self.line(x1, y1, x1 + head * math.cos(a), y1 + head * math.sin(a), w, color)

    def text(self, cx, cy, s, bold=False, size=20, color="#111", anchor="mm"):
        """anchor: mm middle-middle | ml left | mr right | ma top"""
        anchors = {"mm": ("middle", "middle"), "ml": ("start", "middle"),
                   "mr": ("end", "middle"), "ma": ("middle", "start")}
        ta, dom = anchors.get(anchor, ("middle", "middle"))
        self.svg.append(
            f'<text x="{cx}" y="{cy}" font-family="Arial" font-size="{size/2.0:.1f}" '
            f'font-weight="{"bold" if bold else "normal"}" fill="{color}" '
            f'text-anchor="{ta}" dominant-baseline="{dom}">{_esc(s)}</text>'
        )
        psize = max(8, int(size * (1.2 if bold else 1.0)))
        self.d.text((self._sp(cx), self._sp(cy)), s, fill=color,
                    font=self._font(bold, psize), anchor=anchor)

    def tag(self, cx, cy, s, bold=False, size=16, color="#111",
            bg="#ffffff", border="#999", pad=6):
        """White-background label tag for readability over hatching."""
        fnt = self._font(bold, max(8, int(size * 1.0)))
        bbox = fnt.getbbox(s)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        rw = tw + 2 * pad
        rh = th + 2 * pad
        sx, sy = self._sp(cx), self._sp(cy)
        # background rect
        self.d.rounded_rectangle(
            [sx - rw / 2, sy - rh / 2, sx + rw / 2, sy + rh / 2],
            radius=3, fill=bg, outline=border, width=1)
        # SVG: rect + text
        self.svg.append(
            f'<rect x="{cx - rw/(2*self.scale):.1f}" y="{cy - rh/(2*self.scale):.1f}" '
            f'width="{rw/self.scale:.1f}" height="{rh/self.scale:.1f}" '
            f'rx="2" fill="{bg}" stroke="{border}" stroke-width="1"/>'
        )
        self.text(cx, cy, s, bold=bold, size=size, color=color, anchor="mm")

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
               color="#8f8f8f", seed=1, grade=True, angular=False):
        """Seeded, GRADED particles (finer near top, coarser near bottom),
        position-jittered — never a uniform dot grid.
        If angular=True, draws irregular polygons instead of ellipses."""
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
            if angular:
                # irregular polygon (4-6 sides) for gravel/rock look
                nsides = rng.randint(4, 6)
                pts = []
                rot = rng.uniform(0, math.pi)
                for i in range(nsides):
                    a = rot + 2 * math.pi * i / nsides
                    jitter = rng.uniform(0.8, 1.15)
                    pts.append((px + rx * jitter * math.cos(a),
                               py + ry * jitter * math.sin(a)))
                self.polygon(pts, fill=color, outline=None, w=0.5)
            else:
                self.ellipse(px, py, rx, ry, fill=color)

    def soil(self, x1, y1, x2, y2, kind="sand", seed=1):
        """Material presets. kinds: sand | clay | gravel | fill | reclaimed"""
        area = (x2 - x1) * (y2 - y1)
        if kind == "sand":
            self.hatch(x1, y1, x2, y2, 12, 45, "#d4d0c8")
            self.grains(x1, y1, x2, y2, n=int(area / 950), r_min=1.4, r_max=3.0,
                        color="#a09a8e", seed=seed)
        elif kind == "clay":
            self.hatch(x1, y1, x2, y2, 7, -45, "#d6d6d6")
            self.grains(x1, y1, x2, y2, n=max(8, int(area / 2800)), r_min=0.9, r_max=1.6,
                        color="#b8b4a8", seed=seed)
        elif kind == "gravel":
            self.hatch(x1, y1, x2, y2, 16, 45, "#bfbfbf")
            self.grains(x1, y1, x2, y2, n=int(area / 700), r_min=2.2, r_max=4.2,
                        color="#909090", seed=seed, angular=True)
        elif kind in ("fill", "reclaimed"):
            self.hatch(x1, y1, x2, y2, 14, 45, "#c4c4c4")
            self.hatch(x1, y1, x2, y2, 14, -45, "#c4c4c4")
            self.grains(x1, y1, x2, y2, n=int(area / 1300), r_min=1.2, r_max=2.2,
                        color="#a8a4a0", seed=seed)
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
    # self-test: swatch of every soil preset + wavy water + arrow + arc + tag
    c = Canvas(780, 560)
    c.text(390, 30, "figkit v2 texture presets (self-test)", bold=True, size=22)
    kinds = ["sand", "clay", "gravel", "fill", "reclaimed"]
    for i, k in enumerate(kinds):
        x = 40 + (i % 3) * 245
        y = 70 + (i // 3) * 220
        c.rect(x, y, x + 215, y + 150, w=1.8)
        c.soil(x + 3, y + 3, x + 212, y + 147, k, seed=i + 1)
        c.text(x + 107, y - 12, k, bold=True, size=17)
    # water + arrow + arc + tag demo
    c.wavy(60, 500, 380, amp=6, period=40)
    c.text(200, 475, "wavy water (pore water)", size=14, color="#444")
    c.arc(480, 480, 40, 0, 180, w=2.5, color="#347")
    c.tag(560, 480, "arc + tag", size=14)
    c.arrow(480, 505, 480, 440, head=10)
    out = "C:/Users/Owner/AppData/Local/Temp/figkit_selftest.png"
    c.save("C:/Users/Owner/AppData/Local/Temp/figkit_selftest.svg", out)
    print("selftest:", out)
