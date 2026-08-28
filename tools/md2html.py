#!/usr/bin/env python3
"""
Ein sehr einfaches Markdown -> HTML Script.
Usage: python tools/md2html.py content_dir output_dir
Konvertiert einfache Markdown-Dateien (Überschriften # und Absätze) zu HTML-Dateien.
"""
import sys
import os

def md_to_html(md_text):
    lines = md_text.splitlines()
    out = []
    for line in lines:
        line = line.rstrip()
        if not line:
            out.append('<p></p>')
            continue
        if line.startswith('# '):
            out.append(f"<h1>{line[2:].strip()}</h1>")
        elif line.startswith('## '):
            out.append(f"<h2>{line[3:].strip()}</h2>")
        elif line.startswith('### '):
            out.append(f"<h3>{line[4:].strip()}</h3>")
        else:
            out.append(f"<p>{line}</p>")
    return '\n'.join(out)

def wrap_html(title, body_html):
    return f"""<!doctype html>
<html lang=\"de\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n  <title>{title}</title>\n  <link rel=\"stylesheet\" href=\"/assets/template.css\">\n</head>\n<body>\n  <header class=\"site-header\">\n    <div class=\"container header-inner\">\n      <a class=\"brand\" href=\"/\">Deine Marke</a>\n    </div>\n  </header>\n  <main>\n    <section class=\"content container\">\n{body}\n    </section>\n  </main>\n  <footer class=\"site-footer\">\n    <div class=\"container\">\n      <p>© Deine Marke</p>\n    </div>\n  </footer>\n</body>\n</html>""".replace('{body}', body_html)

def main():
    if len(sys.argv) < 3:
        print('Usage: md2html.py content_dir output_dir')
        sys.exit(1)
    content_dir = sys.argv[1]
    output_dir = sys.argv[2]
    os.makedirs(output_dir, exist_ok=True)
    for fname in os.listdir(content_dir):
        if not fname.lower().endswith('.md'):
            continue
        in_path = os.path.join(content_dir, fname)
        with open(in_path, 'r', encoding='utf-8') as f:
            md = f.read()
        html_body = md_to_html(md)
        title = fname.rsplit('.',1)[0]
        full = wrap_html(title, html_body)
        out_name = title + '.html'
        out_path = os.path.join(output_dir, out_name)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(full)
        print('Wrote', out_path)

if __name__ == '__main__':
    main()
