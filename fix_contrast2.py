import re

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix btn-ghost-light
html = re.sub(r'(\.btn-ghost-light\s*\{[^\}]*)color:\s*var\(--dark-gray\);', r'\1color: rgba(255,255,255,0.85);', html)

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Ghost button fixed")
