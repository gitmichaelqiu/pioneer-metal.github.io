"""Build the five static pages from shared shell and page fragments."""
from pathlib import Path
import re
import json
import hashlib
from html import escape

ROOT = Path(__file__).resolve().parent.parent
ASSETS = 'https://raw.githubusercontent.com/pioneer-metal/pioneer-metal.github.io/refs/heads/main/resources/'
PAGES = {'index': ('home', 'Steel profiles, formed at Pioneer'),
         'about': ('about', 'Manufacturing at Pioneer'),
         'products': ('products', 'Steel profiles and custom fabrication'),
         'news': ('news', 'Global exhibitions'),
         'contact': ('contact', 'Start a conversation')}
COPY = json.loads((ROOT / 'site/strings.json').read_text())
(ROOT / 'translations.js').write_text('/* Generated from site/strings.json by scripts/build_site.py. */\nconst i18nData = ' + json.dumps(COPY, ensure_ascii=False, indent=2) + ';\n')
VERSION = hashlib.sha256(b''.join((ROOT / name).read_bytes() for name in ['style.css', 'main.js', 'translations.js'])).hexdigest()[:10]
FAVICON_VERSION = hashlib.sha256((ROOT / 'resources/Favicon.png').read_bytes()).hexdigest()[:10]

for filename, (page, title) in PAGES.items():
    header = (ROOT / 'site/header.html').read_text()
    header = header.replace(f'data-page="{page}"', f'data-page="{page}" aria-current="page"')
    content = (ROOT / f'site/pages/{filename}.html').read_text()
    footer = (ROOT / 'site/footer.html').read_text()
    html = f'''<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Pioneer Metal Products Factory. Cold-rolled steel reinforcement, drywall and ceiling sections, and custom fabrication for global partners.">
    <meta name="theme-color" content="#d9271c">
    <title>{title} | Pioneer Metal</title>
    <link rel="icon" type="image/png" href="resources/Favicon.png?v={FAVICON_VERSION}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,500&family=Jost:wght@400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css?v={VERSION}">
    <script>try{{document.documentElement.dataset.theme=localStorage.getItem('theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light')}}catch(e){{}}</script>
    <script src="translations.js?v={VERSION}" defer></script>
    <script src="main.js?v={VERSION}" defer></script>
</head>
<body class="{page}" id="top">
    <a class="skip-link" href="#main">Skip to content</a>
    {header}
    <main id="main">{content}</main>
    {footer}
</body>
</html>
'''
    html = re.sub(r'\{\{asset:([^}]+)\}\}', lambda m: ASSETS + m[1], html)
    for key, copy in COPY['en'].items():
        pattern = r'(<[a-zA-Z][^>]*)(>\s*)' + re.escape(copy) + r'(\s*</[a-zA-Z][^>]*>)'
        def annotate(match):
            if 'data-i18n=' in match[1] or 'data-copy=' in match[1]:
                return match[0]
            return f'{match[1]} data-i18n="{key}"{match[2]}{copy}{match[3]}'
        html = re.sub(pattern, annotate, html)
        # The static, no-script page must carry the same canonical English copy.
        translated = r'(<(?P<tag>[a-z][a-z0-9]*)\b[^>]*data-i18n="' + re.escape(key) + r'"[^>]*>)[\s\S]*?(</(?P=tag)>)'
        rendered_copy = escape(copy, quote=False).replace('&lt;br&gt;', '<br>')
        html = re.sub(translated, lambda match: match[1] + rendered_copy + match[3], html)
    (ROOT / f'{filename}.html').write_text(html)
    print(f'Built {filename}.html')
