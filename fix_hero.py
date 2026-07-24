import re

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix btn-outline
html = re.sub(r'(\.btn-outline\s*\{[^\}]*)color:\s*rgba\(255,255,255,0\.85\);', r'\1color: var(--blue-dark);', html)
html = re.sub(r'(\.btn-outline\s*\{[^\}]*)border:\s*1\.5px\s*solid\s*rgba\(255,255,255,0\.25\);', r'\1border: 1.5px solid rgba(0, 90, 155, 0.25);', html)

# btn-outline hover
html = re.sub(r'(\.btn-outline:hover\s*\{[^\}]*)background:\s*rgba\(251,182,12,0\.06\);', r'\1background: rgba(0, 90, 155, 0.05);', html)

# Fix hero stat label
html = re.sub(r'(\.hero__stat-label\s*\{[^\}]*)color:\s*rgba\(255,255,255,0\.4\);', r'\1color: var(--mid-gray);', html)

# Fix hero stat border
html = re.sub(r'(\.hero__stat\s*\{[^\}]*)border-right:\s*1px\s*solid\s*rgba\(255,255,255,0\.1\);', r'\1border-right: 1px solid var(--border);', html)

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Fixed hero elements')
