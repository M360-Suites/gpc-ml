import re

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Google Font
font_import = "@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&display=swap');\n"
html = html.replace('<style>', '<style>\n' + font_import)

# 2. Update --ff-head
html = re.sub(r'--ff-head:\s*\'Segoe UI\',\s*\'Lucida Sans\',\s*system-ui,\s*sans-serif;', r"--ff-head: 'Playfair Display', serif;", html)

# 3. Add styling for EM in headings
em_css = '''
h1 em, h2 em, h3 em {
  font-family: 'Playfair Display', serif;
  font-weight: 700;
  font-style: italic;
  color: #F57C00;
}
'''
html = html.replace('/* ── Scroll to top ── */', em_css + '\n/* ── Scroll to top ── */')

# 4. Remove form
form_pattern = r'<div class="cta-section__form reveal-right">.*?</div>\s*</div>\s*</div>\s*</section>'
html = re.sub(form_pattern, '</div>\n  </div>\n</section>', html, flags=re.DOTALL)

# Update CTA layout
html = re.sub(r'\.cta-section__inner\s*\{[^\}]*\}', '''.cta-section__inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  max-width: 680px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}''', html)
html = html.replace('<div class="cta-section__left reveal-left">', '<div class="cta-section__left reveal">')
html = html.replace('margin-top:1.5rem;display:flex;align-items:center;gap:1rem;', 'margin-top:2rem;display:flex;align-items:center;justify-content:center;gap:1rem;')

# 5. Footer CSS changes
html = re.sub(r'(\.footer\s*\{[^\}]*)background:\s*#000e1c;', r'\1background: var(--white);', html)
html = re.sub(r'(\.footer\s*\{[^\}]*)border-top:\s*3px\s*solid\s*var\(--amber\);', r'\1border-top: 1px solid var(--border);', html)

html = re.sub(r'(\.footer__brand-tagline\s*\{[^\}]*)color:\s*rgba\(255,255,255,0\.45\);', r'\1color: var(--dark-gray);', html)
html = re.sub(r'(\.footer__brand-desc\s*\{[^\}]*)color:\s*rgba\(255,255,255,0\.35\);', r'\1color: var(--mid-gray);', html)
html = re.sub(r'(\.footer__links\s*a\s*\{[^\}]*)color:\s*rgba\(255,255,255,0\.45\);', r'\1color: var(--dark-gray);', html)
html = re.sub(r'(\.footer__contact-text\s*\{[^\}]*)color:\s*rgba\(255,255,255,0\.4\);', r'\1color: var(--mid-gray);', html)
html = re.sub(r'(\.footer__contact-text\s*a\s*\{[^\}]*)color:\s*rgba\(255,255,255,0\.4\);', r'\1color: var(--dark-gray);', html)
html = re.sub(r'(\.footer__copy\s*\{[^\}]*)color:\s*rgba\(255,255,255,0\.25\);', r'\1color: var(--mid-gray);', html)
html = re.sub(r'(\.footer__legal\s*a\s*\{[^\}]*)color:\s*rgba\(255,255,255,0\.25\);', r'\1color: var(--mid-gray);', html)
html = re.sub(r'(\.footer__legal\s*a:hover\s*\{[^\}]*)color:\s*rgba\(255,255,255,0\.6\);', r'\1color: var(--dark-gray);', html)
html = re.sub(r'(\.footer__col-title\s*\{[^\}]*)color:\s*var\(--amber\);', r'\1color: var(--blue-dark);', html)

html = re.sub(r'(\.footer__social\s*svg\s*\{[^\}]*)fill:\s*rgba\(255,255,255,0\.6\);', r'\1fill: var(--blue-dark);', html)
html = re.sub(r'(\.footer__social\s*a:hover\s*svg\s*\{[^\}]*)fill:\s*var\(--blue-dark\);', r'\1fill: var(--white);', html)
html = re.sub(r'(\.footer__social\s*a:hover\s*\{[^\}]*)background:\s*var\(--amber\);', r'\1background: var(--blue-dark);', html)

html = re.sub(r'(\.footer__contact-icon\s*\{[^\}]*)color:\s*var\(--amber\);', r'\1color: var(--blue-dark);', html)

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied client feedback changes.")
