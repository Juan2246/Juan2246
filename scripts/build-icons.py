"""Rebuild the original 32px animated heading icons (requires Pillow)."""

from math import cos, pi, sin
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "icons"
SIZE, SCALE, FRAMES = 32, 4, 18
PURPLE = (132, 87, 224, 255)
CYAN = (15, 166, 189, 255)
PINK = (216, 105, 170, 255)


class Canvas:
    def __init__(self):
        self.image = Image.new("RGBA", (SIZE * SCALE, SIZE * SCALE))
        self.draw = ImageDraw.Draw(self.image)

    def line(self, points, color=PURPLE, width=1.8):
        points = [(round(x * SCALE), round(y * SCALE)) for x, y in points]
        self.draw.line(points, fill=color, width=round(width * SCALE), joint="curve")
        r = width * SCALE / 2
        for x, y in (points[0], points[-1]):
            self.draw.ellipse((x-r, y-r, x+r, y+r), fill=color)

    def ellipse(self, box, color=PURPLE, width=1.8, fill=None):
        self.draw.ellipse(tuple(round(v*SCALE) for v in box), outline=color, width=round(width*SCALE), fill=fill)

    def dot(self, x, y, r=1.15, color=CYAN):
        self.ellipse((x-r, y-r, x+r, y+r), color, fill=color)

    def arc(self, box, start, end, color=PURPLE, width=1.8):
        self.draw.arc(tuple(round(v*SCALE) for v in box), start=start, end=end, fill=color, width=round(width*SCALE))

    def sparkle(self, x, y, r=2, color=CYAN):
        self.line([(x-r,y),(x+r,y)], color, 1.3)
        self.line([(x,y-r),(x,y+r)], color, 1.3)


def cat(t, n):
    c = Canvas()
    dy = .5*sin(t)
    c.line([(7,14+dy),(6.6,6+dy),(12,9.8+dy),(20,9.8+dy),(25.4,6+dy),(25,14+dy)])
    c.arc((6,8+dy,26,27+dy), 17, 163)
    c.line([(6.6,17+dy),(2.7,16+dy)], CYAN, 1.4)
    c.line([(6.3,20+dy),(2.7,21+dy)], CYAN, 1.4)
    c.line([(25.4,17+dy),(29.3,16+dy)], CYAN, 1.4)
    c.line([(25.7,20+dy),(29.3,21+dy)], CYAN, 1.4)
    if n in (12,13):
        c.line([(10,15.3+dy),(12.5,15.3+dy)], PURPLE, 1.4)
        c.line([(19.5,15.3+dy),(22,15.3+dy)], PURPLE, 1.4)
    else:
        c.dot(11.5,15+dy,.85,PURPLE)
        c.dot(20.5,15+dy,.85,PURPLE)
    c.line([(14.5,18+dy),(16,19.2+dy),(17.5,18+dy)], PINK, 1.25)
    c.line([(16,19.2+dy),(16,21+dy)], PURPLE, 1.2)
    c.arc((12.9,18.7+dy,16.1,22.1+dy),0,120,width=1.1)
    c.arc((15.9,18.7+dy,19.1,22.1+dy),60,180,width=1.1)
    return c


def target(t, n):
    c = Canvas()
    c.arc((3,6,27,30), -31, 293)
    c.arc((8,11,22,25), -32, 294)
    c.dot(15,18,1.6,PURPLE)
    d = .65*sin(t)
    c.line([(15+d,18-d),(26+d,7-d)], CYAN, 1.8)
    c.line([(22+d,7-d),(26+d,7-d),(26+d,11-d)], CYAN, 1.7)
    c.line([(24+d,3-d),(24+d,8-d),(29+d,8-d)], CYAN, 1.4)
    return c


def build(t, n):
    c = Canvas()
    c.line([(5,23),(5,8),(27,8),(27,23),(5,23)])
    c.line([(2,27),(30,27)], CYAN, 1.8)
    c.line([(12,27),(13,24),(19,24),(20,27)], CYAN, 1.4)
    d = .8*sin(t)
    c.line([(12-d,13),(9-d,16),(12-d,19)], CYAN, 1.65)
    c.line([(20+d,13),(23+d,16),(20+d,19)], CYAN, 1.65)
    c.line([(17,12),(15,20)], PURPLE, 1.35)
    return c


def tools(t, n):
    c = Canvas()
    # A wrench and pencil, each legible as an independent tool at 32px.
    c.line([(8,4),(5,7),(5,11),(9,15),(22,28),(26,24),(13,11),(13,7),(10,4)], PURPLE, 1.7)
    c.line([(8,4),(8,9),(10,11),(13,11)], PURPLE, 1.7)
    dx, dy = .45*sin(t), .45*cos(t)
    c.line([(x+dx,y+dy) for x,y in [(26,4),(28,6),(11,23),(7,25),(9,21),(26,4)]], CYAN, 1.7)
    c.line([(23.5+dx,6.5+dy),(25.5+dx,8.5+dy)], CYAN, 1.4)
    c.dot(23,25,1,PURPLE)
    r = 1.5+.35*sin(t)
    c.sparkle(26,16,r,CYAN)
    return c


def activity(t, n):
    c = Canvas()
    c.line([(3,25),(3,7)], PURPLE, 1.6)
    c.line([(3,25),(29,25)], PURPLE, 1.6)
    c.line([(6,20),(11,16),(16,19),(21,10),(27,7)], CYAN, 1.85)
    c.dot(11,16,1.3,PURPLE)
    c.dot(16,19,1.3,PURPLE)
    c.dot(21,10,1.3,PURPLE)
    c.dot(27,7,1.5+.3*sin(t),PURPLE)
    # The travelling marker makes activity perceptible without flashing.
    pts = [(6,20),(11,16),(16,19),(21,10),(27,7)]
    p = (1-cos(t))*2
    i = min(3,int(p))
    f = p-i
    x = pts[i][0]*(1-f)+pts[i+1][0]*f
    y = pts[i][1]*(1-f)+pts[i+1][1]*f
    c.dot(x,y,1.25,PINK)
    return c


def chat(t, n):
    c = Canvas()
    c.line([(10,23),(9,27),(14,25),(26,25),(29,22),(29,16),(26,13)], CYAN, 1.7)
    c.line([(7,5),(21,5),(24,8),(24,16),(21,19),(12,19),(6,23),(7,19),(3,16),(3,9),(7,5)], PURPLE, 1.7)
    for j,x in enumerate((8.5,13.5,18.5)):
        c.dot(x,12+.85*sin(t-j*.8),1.15,CYAN)
    return c


def gif_frame(canvas):
    source = canvas.image.resize((SIZE,SIZE), Image.Resampling.LANCZOS)
    rgba = list(source.get_flattened_data())
    # GIF supports only binary alpha. Quantize the original stroke RGB, never
    # composite against a background, so light and dark themes stay halo-free.
    rgb = Image.new("RGB", source.size)
    rgb.putdata([(r,g,b) for r,g,b,a in rgba])
    quantized = rgb.quantize(colors=254, method=Image.Quantize.MEDIANCUT)
    palette = quantized.getpalette()[:254*3] + [0,0,0,0,0,0]
    result = Image.new("P", source.size)
    result.putpalette(palette)
    values = list(quantized.get_flattened_data())
    result.putdata([v if rgba[i][3] >= 85 else 255 for i,v in enumerate(values)])
    result.info["transparency"] = 255
    return result


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    for name,draw in (("cat",cat),("target",target),("build",build),("tools",tools),("activity",activity),("chat",chat)):
        frames = [gif_frame(draw(n/FRAMES*2*pi,n)) for n in range(FRAMES)]
        path = OUT / f"{name}.gif"
        frames[0].save(path,save_all=True,append_images=frames[1:],duration=120,loop=0,transparency=255,disposal=2,optimize=False)
        with Image.open(path) as actual:
            assert actual.size == (32,32)
            assert actual.n_frames > 1
            assert actual.info["loop"] == 0
            for i in range(actual.n_frames):
                actual.seek(i)
                assert actual.convert("RGBA").getpixel((0,0))[3] == 0
            print(f"{path.name}: 32x32, {actual.n_frames} frames, transparent, {path.stat().st_size} bytes")


if __name__ == "__main__":
    main()
