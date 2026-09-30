"""Generate font outlines for GitHub; requires fonttools. Run from any directory."""
from pathlib import Path
from html import escape
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
OUT = ASSETS / 'headings'
OUT.mkdir(exist_ok=True)
BRUSH = TTFont(ASSETS / 'fonts/CaveatBrush-Regular.ttf')
DISPLAY = TTFont(ASSETS / 'fonts/Rye-Regular.ttf')

def outline(font, text, size):
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    pen = SVGPathPen(glyphs)
    bounds = BoundsPen(glyphs)
    advance = 0
    for char in text:
        name = cmap.get(ord(char))
        if name is None:
            raise ValueError(f'Missing glyph: {char!r}')
        glyph = glyphs[name]
        transform = (1, 0, 0, 1, advance, 0)
        glyph.draw(TransformPen(pen, transform))
        glyph.draw(TransformPen(bounds, transform))
        advance += glyph.width
    return pen.getCommands(), bounds.bounds, size / font['head'].unitsPerEm

def word(font, text, size, cx, cy, color):
    data, (x0, y0, x1, y1), scale = outline(font, text, size)
    x = cx - (x0 + x1) * scale / 2
    y = cy + (y0 + y1) * scale / 2
    return f'<path fill="{color}" transform="translate({x:.3f} {y:.3f}) scale({scale:.6f} {-scale:.6f})" d="{data}"/>'

HEADINGS = {
    'hello': 'Hola, soy Juan Sebastián',
    'about': 'Un poco de mí',
    'goals': 'Hacia dónde apunto',
    'projects': 'Cosas que he construido',
    'tools': 'Herramientas',
    'backend': 'Backend y datos',
    'frontend': 'Frontend',
    'activity': 'Actividad en GitHub',
    'contact': 'Conversemos.',
    'xora': 'XoraMarket',
    'alquila': 'Alquila Ya',
    'data': 'Data Science',
    'portfolio': 'Portafolio',
}

for name, text in HEADINGS.items():
    data, (x0, y0, x1, y1), scale = outline(BRUSH, text, 40)
    width = round((x1 - x0) * scale + 4, 2)
    height = round((y1 - y0) * scale + 6, 2)
    for theme, color in [('dark', '#ede4ff'), ('light', '#3b225c')]:
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(text)}">
<title>{escape(text)}</title>
<path fill="{color}" transform="translate({2-x0*scale:.3f} {3+y1*scale:.3f}) scale({scale:.6f} {-scale:.6f})" d="{data}"/>
</svg>'''
        (OUT / f'{name}-{theme}.svg').write_text(svg, encoding='utf-8')

footer = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="270" viewBox="0 0 1000 270" role="img" aria-labelledby="title desc">
<title id="title">¡Gracias! Por tomarse el tiempo de leer.</title>
<desc id="desc">Una postal de papel crema, lavanda y coral, con estrellas dibujadas a mano y letras ornamentales grandes.</desc>
<defs>
  <linearGradient id="paper" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#fff5df"/><stop offset=".52" stop-color="#f8e8eb"/><stop offset="1" stop-color="#e8dcff"/></linearGradient>
  <pattern id="grain" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="3" cy="5" r=".7" fill="#957189" opacity=".18"/><circle cx="16" cy="17" r=".55" fill="#957189" opacity=".13"/></pattern>
</defs>
<style>.spark{transform-box:fill-box;transform-origin:center;animation:breathe 5s ease-in-out infinite}.later{animation-delay:-2s}@keyframes breathe{50%{transform:scale(.82) rotate(8deg);opacity:.65}}@media(prefers-reduced-motion:reduce){.spark{animation:none}}</style>
<rect x="1" y="1" width="998" height="268" rx="24" fill="url(#paper)" stroke="#dcc8e4" stroke-width="2"/>
<rect x="2" y="2" width="996" height="266" rx="23" fill="url(#grain)"/>
<path d="M0 247C102 198 173 211 245 270H0Z" fill="#d8ccf4"/>
<path d="M793 0C844 92 933 89 1000 54V0Z" fill="#efc7c5" opacity=".75"/>
<path d="M802 254C887 208 945 224 1000 186" fill="none" stroke="#9976bc" stroke-width="2"/>
<path d="M26 190C74 137 18 126 61 93" fill="none" stroke="#b88096" stroke-width="2.5" stroke-linecap="round"/>
<g class="spark" fill="#9570c0"><path d="m91 53 7 20 20 7-20 7-7 20-7-20-20-7 20-7Z"/><path d="m862 186 5 14 14 5-14 5-5 14-5-14-14-5 14-5Z"/></g>
<g class="spark later" fill="#bf6b83"><path d="m902 69 6 16 16 6-16 6-6 16-6-16-16-6 16-6Z"/><path d="m185 191 4 12 12 4-12 4-4 12-4-12-12-4 12-4Z"/></g>
<g fill="none" stroke="#8d6cae" stroke-width="2.5" stroke-linecap="round"><path d="m133 126 8 4m-2-17 5-8M863 127l9 3m-16 12 3 8"/><circle cx="111" cy="165" r="5"/><circle cx="819" cy="63" r="4"/></g>
'''
footer += word(DISPLAY, '¡Gracias!', 112, 500, 112, '#49235f')
footer += word(BRUSH, 'Por tomarse el tiempo de leer.', 39, 500, 206, '#705073')
footer += '\n</svg>\n'
(ASSETS / 'footer.svg').write_text(footer, encoding='utf-8')
print(f'Created {len(HEADINGS)*2} heading assets and footer.svg')
