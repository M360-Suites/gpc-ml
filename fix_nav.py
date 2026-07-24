import re

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add to 1024px
html = html.replace('@media (max-width: 1024px) {\n  .hero', '@media (max-width: 1024px) {\n  .nav__links { display: none; }\n  .nav__hamburger { display: flex; }\n  .hero')

# Remove from 768px
html = html.replace('  .nav__links { display: none; }\n  .nav__hamburger { display: flex; }\n', '')

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Hamburger menu updated for medium devices")
