import re

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

nav_match = re.search(r'<a href="#" class="nav__logo">.*?</a>', html, re.DOTALL)
if nav_match:
    print('NAV LOGO FOUND:\n', nav_match.group(0))

footer_match = re.search(r'<div class="footer__brand">.*?(?=</div>\s*<div>\s*<div class="footer__col-title">)', html, re.DOTALL)
if footer_match:
    print('\nFOOTER BRAND FOUND:\n', footer_match.group(0))
