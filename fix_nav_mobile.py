import re

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix hamburger color
html = re.sub(r'(\.nav__hamburger\s*span\s*\{[^\}]*)background:\s*var\(--white\);', r'\1background: var(--blue-dark);', html)

# Make "Book a Truck" button slightly smaller on mobile
# add a media query for .nav__cta
media_query = '''
@media (max-width: 480px) {
  .nav__cta { padding: 6px 14px !important; font-size: 12px !important; }
  .btn-dark { padding: 10px 20px; font-size: 13px; }
  .btn-primary { padding: 10px 20px; font-size: 13px; }
}
'''
if 'max-width: 480px' in html:
    html = html.replace('@media (max-width: 480px) {\n  .about__pillars', '@media (max-width: 480px) {\n  .nav__cta { padding: 6px 14px !important; font-size: 12px !important; }\n  .btn-dark { padding: 10px 20px; font-size: 13px; }\n  .btn-primary { padding: 10px 20px; font-size: 13px; }\n  .about__pillars')

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Hamburger and buttons fixed")
