import re

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Services Header H2
html = re.sub(r'(\.services__header h2\s*\{[^\}]*)color:\s*var\(--blue-dark\);', r'\1color: var(--white);', html)

# 2. Service Card Title
html = re.sub(r'(\.service-card__title\s*\{[^\}]*)color:\s*var\(--blue-dark\);', r'\1color: var(--white);', html)

# 3. CSR Header H2
html = re.sub(r'(\.csr__header h2\s*\{[^\}]*)color:\s*var\(--blue-dark\);', r'\1color: var(--white);', html)

# 4. CSR Card Label Title
html = re.sub(r'(\.csr-card__label-title\s*\{[^\}]*)color:\s*var\(--blue-dark\);', r'\1color: var(--white);', html)

# 5. Stat Item Num
html = re.sub(r'(\.stat-item__num\s*\{[^\}]*)color:\s*var\(--blue-dark\);', r'\1color: var(--white);', html)

# 6. News Featured Headline
html = re.sub(r'(\.news-featured__headline\s*\{[^\}]*)color:\s*var\(--blue-dark\);', r'\1color: var(--white);', html)

# Let's also check if .footer has any issues. Footer bg is #000e1c (very dark).
# Links:
# .footer__links a { color: rgba(255,255,255,0.45); } - This is fine.
# .footer__links a:hover { color: var(--blue-dark); } - Hover should probably be var(--amber) or white since background is dark. Let's make it amber.
html = re.sub(r'(\.footer__links a:hover\s*\{[^\}]*)color:\s*var\(--blue-dark\);', r'\1color: var(--amber);', html)

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Contrast issues fixed")
