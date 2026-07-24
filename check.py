with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    c = f.read()
print('Has Team:', '<!-- TEAM -->' in c)
print('Has SVG Phone:', '<svg viewBox="0 0 24 24"' in c)
print('Has i1.jpeg:', 'images/i1.jpeg' in c)
print('Has i2.jpeg:', 'images/i2.jpeg' in c)
print('No emojis:', '&#128222;' not in c)
print('File size:', len(c))
