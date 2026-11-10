#!/usr/bin/env python3
"""Build the 3-wall screen frames for "God With Us".

Each screen is a 3648x1152 frame: left wall | black gap | center wall | black gap | right wall.
Every wall is its own painting (never one wide image sliced across the gaps).

For each screen this writes:
  NNa.jpg  art only (operator shows this while the story is read)
  NNb.jpg  art + the kids' answer on the CENTER wall (operator clicks to it at the cue)
  Screen 4 also gets NNc / NNd: "No room!" grows as the kids get louder.

Usage:
  python3 build_screens.py --art ART_DIR --out OUT_DIR [--lang en|es]

ART_DIR holds per-wall images named  NN-L.*, NN-C.*, NN-R.*  (e.g. 05-C.png),
or a finished 3-wall frame  NN.jpg  (3648x1152) to re-use as is (screen 3 today).
For the Spanish no-pine-cone edition, put NN-C-sin.* next to NN-C.* and pass --sin.
"""
import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageStat

FRAME_W, FRAME_H = 3648, 1152
SIDE_W, CENTER_W, GAP = 864, 1440, 240
LEFT_X, CENTER_X, RIGHT_X = 0, SIDE_W + GAP, SIDE_W + GAP + CENTER_W + GAP  # 0, 1104, 2784

FONT = Path(__file__).with_name("fonts") / "Fredoka.ttf"

GOLD, CREAM, INK = "#FFD866", "#FFF8E8", "#2A1A0E"

# style, EN text, ES text
ANSWERS = {
    1: ("theme", "God will be with us!", "¡Dios estará con nosotros!"),
    3: ("theme", "God will be with us!", "¡Dios estará con nosotros!"),
    4: ("grow", "No room!", "¡No hay lugar!"),
    5: ("theme", "God will be with us!", "¡Dios estará con nosotros!"),
    6: ("whisper", "God will be with us…", "Dios estará con nosotros…"),
    7: ("shout", "Baby!", "¡Bebé!"),
    9: ("shout", "Munch, munch, munch!", "¡Ñam, ñam, ñam!"),
    10: ("soft", "God is with us.", "Dios está con nosotros."),
}

# Screen 3 keeps its old art, which has Gabriel's head in the top middle:
# two lines over the open wall to the upper left instead.
OVERRIDES = {
    3: {"en": {"lines": ["God will", "be with us!"], "size": 120, "cx": 370, "baselines": [150, 290]},
        "es": {"lines": ["¡Dios estará", "con nosotros!"], "size": 100, "cx": 390, "baselines": [140, 262]}},
}

MAX_LINE_W = CENTER_W - 2 * 96


def font(size, wght):
    f = ImageFont.truetype(str(FONT), size)
    f.set_variation_by_axes([wght, 100])  # axes are (wght, wdth)
    return f


def fit(text, size, wght, floor):
    while size > floor and font(size, wght).getlength(text) > MAX_LINE_W:
        size -= 2
    return size


def load_wall(path, w):
    im = Image.open(path).convert("RGB")
    # cover-fit to the wall, centred (generate at the right aspect so this barely crops)
    s = max(w / im.width, FRAME_H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - FRAME_H) // 2
    return im.crop((x, y, x + w, y + FRAME_H))


def assemble(art_dir, n, sin):
    whole = next(iter(sorted(art_dir.glob(f"{n:02d}.jp*g"))), None)
    if whole:
        im = Image.open(whole).convert("RGB")
        assert im.size == (FRAME_W, FRAME_H), f"{whole} must be {FRAME_W}x{FRAME_H}"
        return im
    def wall(tag):
        if tag == "C" and sin:
            m = sorted(art_dir.glob(f"{n:02d}-C-sin.*"))
            if m:
                return m[0]
        m = sorted(art_dir.glob(f"{n:02d}-{tag}.*"))
        if not m:
            raise SystemExit(f"missing {n:02d}-{tag}.* in {art_dir}")
        return m[0]
    frame = Image.new("RGB", (FRAME_W, FRAME_H), "black")
    frame.paste(load_wall(wall("L"), SIDE_W), (LEFT_X, 0))
    frame.paste(load_wall(wall("C"), CENTER_W), (CENTER_X, 0))
    frame.paste(load_wall(wall("R"), SIDE_W), (RIGHT_X, 0))
    return frame


def draw_lines(center, lines, size, wght, style, cx=None, baselines=None):
    """Draw text onto the 1440x1152 center-wall image (RGB) and return it."""
    f = font(size, wght)
    cx = CENTER_W // 2 if cx is None else cx
    if baselines is None:
        b0 = round(68 + 0.70 * size)
        baselines = [round(b0 + i * 1.15 * size) for i in range(len(lines))]

    # light-art flip: dark ink on pale backgrounds
    top = max(0, min(baselines) - size - 40)
    box = (max(0, cx - MAX_LINE_W // 2 - 40), top, min(CENTER_W, cx + MAX_LINE_W // 2 + 40), max(baselines) + 40)
    light = ImageStat.Stat(center.convert("L").crop(box)).mean[0] / 255 > 0.62

    if style in ("theme", "shout", "grow"):
        fill = "#3A2213" if light else (GOLD if style == "theme" else CREAM)
        stroke, sw = ("#FFF6E2", 6) if light else (INK, round(0.06 * size))
        glows = [("#FFF3D6" if light else "#1A0F08", 170 if light else 150, 18, sw + 6, (0, 6))]
        alpha = 255
    elif style == "whisper":
        fill, stroke, sw, alpha = ("#4A3626", None, 0, 230) if light else ("#FFF3D6", None, 0, 210)
        glows = [("#FFF6E2" if light else "#0E1530", 150, 14, 4, (0, 4))]
    else:  # soft
        fill, stroke, sw, alpha = ("#5A3412", None, 0, 255) if light else ("#FFE2A0", None, 0, 255)
        glows = ([("#FFF3D6", 170, 20, 8, (0, 0))] if light else
                 [("#FFC86A", 90, 32, 10, (0, 0)), ("#20120A", 140, 20, 6, (0, 4))])

    out = center.convert("RGBA")
    for color, a, blur, gw, (dx, dy) in glows:
        layer = Image.new("RGBA", out.size, (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        rgb = ImageDraw.ImageColor.getrgb(color)
        for line, b in zip(lines, baselines):
            d.text((cx + dx, b + dy), line, font=f, anchor="ms", fill=rgb + (a,),
                   stroke_width=gw, stroke_fill=rgb + (a,))
        out = Image.alpha_composite(out, layer.filter(ImageFilter.GaussianBlur(blur)))
    layer = Image.new("RGBA", out.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    rgb = ImageDraw.ImageColor.getrgb(fill)
    for line, b in zip(lines, baselines):
        kw = {"stroke_width": sw, "stroke_fill": stroke} if stroke else {}
        d.text((cx, b), line, font=f, anchor="ms", fill=rgb + (alpha,), **kw)
    return Image.alpha_composite(out, layer).convert("RGB")


def with_answer(frame, n, lang, size_override=None):
    style, en, es = ANSWERS[n]
    text = en if lang == "en" else es
    center = frame.crop((CENTER_X, 0, CENTER_X + CENTER_W, FRAME_H))
    if n in OVERRIDES:
        o = OVERRIDES[n][lang]
        center = draw_lines(center, o["lines"], o["size"], 600, style, o["cx"], o["baselines"])
    else:
        wght, size, floor = {"whisper": (400, 84, 70), "soft": (500, 108, 90)}.get(style, (600, 132, 104))
        size = fit(text, size_override or size, wght, floor)
        center = draw_lines(center, [text], size, wght, style)
    out = frame.copy()
    out.paste(center, (CENTER_X, 0))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--art", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--lang", choices=["en", "es"], default="en")
    ap.add_argument("--sin", action="store_true", help="Spanish no-pine-cone centers")
    ap.add_argument("--screens", default="1-10")
    a = ap.parse_args()
    lo, hi = (int(x) for x in a.screens.split("-")) if "-" in a.screens else (int(a.screens),) * 2
    a.out.mkdir(parents=True, exist_ok=True)
    pages = []
    for n in range(lo, hi + 1):
        frame = assemble(a.art, n, a.sin)
        frame.save(a.out / f"{n:02d}a.jpg", quality=92); pages.append(frame)
        if n == 4:
            for tag, size in (("b", 112), ("c", 132), ("d", 160)):
                f = with_answer(frame, n, a.lang, size)
                f.save(a.out / f"{n:02d}{tag}.jpg", quality=92); pages.append(f)
        elif n in ANSWERS:
            f = with_answer(frame, n, a.lang)
            f.save(a.out / f"{n:02d}b.jpg", quality=92); pages.append(f)
    pdf = a.out / f"screens-{a.lang}{'-sin' if a.sin else ''}.pdf"
    pages[0].save(pdf, save_all=True, append_images=pages[1:], resolution=288)
    print(f"wrote {len(pages)} frames -> {a.out}")


if __name__ == "__main__":
    main()
