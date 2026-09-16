from PIL import Image, ImageDraw, ImageFont
import os

ARIAL = "/System/Library/Fonts/Supplemental/Arial.ttf"

def load(n):  return Image.open(f"out/{n}").convert("RGB")
def save(im,n):
    im.save(f"final/{n}"); print(f"  -> final/{n} {im.size}")

def erase(dr, box, fill=(255,255,255)):
    dr.rectangle(box, fill=fill)

def stamp(dr, box, text, font, fill=(0,0,0), align="center"):
    x0,y0,x1,y1 = box
    l,t,r,b = dr.textbbox((0,0), text, font=font)
    w,h = r-l, b-t
    if align == "center": x = x0 + (x1-x0-w)//2
    else:                 x = x0
    y = y0 + (y1-y0-h)//2
    dr.text((x-l, y-t), text, font=font, fill=fill)

# ---------- 6.2 : garbled "Reinforcement of soils" ----------
im = load("gen-6.2.png"); dr = ImageDraw.Draw(im)
erase(dr, (1906, 919, 3078, 1135))
stamp(dr, (1906, 919, 3078, 1135), "Reinforcement of soils", ImageFont.truetype(ARIAL, 82))
save(im, "fig-6.2.png")

# ---------- 6.1 : duplicate "COMPACTION" inside panel (b) ----------
im = load("gen-6.1.png"); dr = ImageDraw.Draw(im)
erase(dr, (1230, 1140, 1588, 1243))
save(im, "fig-6.1.png")

# ---------- 6.13 : duplicate "SAND MAT" label + its leader ----------
im = load("gen-6.13.png"); dr = ImageDraw.Draw(im)
erase(dr, (1692, 1223, 2125, 1455))
erase(dr, (1690, 1204, 1742, 1228))
save(im, "fig-6.13.png")

# ---------- 7.6 : ghost Japanese + baked-in caption ----------
im = load("gen-7.6.png"); dr = ImageDraw.Draw(im)
W,H = im.size
erase(dr, (385, 1032, 695, 1195))    # ghost, above progress arrow
erase(dr, (385, 1195, 570, 1360))    # ghost, left of arrow start
erase(dr, (0, 1360, W, H))           # baked-in "Figure 1 ..." caption
save(im, "fig-7.6.png")

# ---------- clean pass-throughs ----------
for src, dst in [("gen-4.9.png","fig-4.9.png"), ("gen-4.18.png","fig-4.18.png"),
                 ("gen-5.1.png","fig-5.1.png"), ("gen-5.5.png","fig-5.5.png"),
                 ("gen-5.18.png","fig-5.18.png")]:
    save(load(src), dst)
