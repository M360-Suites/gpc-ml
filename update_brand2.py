import re

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Company Name
html = html.replace('GPC Group Limited', 'GPC Energy and Logistics Limited')
html = html.replace('GPC Group Ltd', 'GPC Energy and Logistics Ltd')
html = html.replace('GPC Group', 'GPC Energy and Logistics')

# 2. Typography
html = re.sub(r'<link href=\"https://fonts.googleapis.com/css2\?family=[^>]+>', '', html)
html = html.replace('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n', '')
html = html.replace("--ff-head: 'Sora', system-ui, sans-serif;", "--ff-head: 'Segoe UI', 'Lucida Sans', system-ui, sans-serif;")
html = html.replace("--ff-body: 'Plus Jakarta Sans', system-ui, sans-serif;", "--ff-body: 'Segoe UI', 'Lucida Sans', system-ui, sans-serif;")

# 3. Mostly White Theme
# Nav Background
html = html.replace('background: rgba(0, 26, 50, 0.92);', 'background: rgba(255, 255, 255, 0.95);')
html = html.replace('background: rgba(0, 26, 50, 0.98);', 'background: rgba(255, 255, 255, 0.98);')
html = html.replace('border-bottom: 1px solid var(--border-light);', 'border-bottom: 1px solid rgba(0, 90, 155, 0.1);')

# Fix nav text colors
html = re.sub(r'\.nav__logo-text strong\s*\{([^\}]*)color:\s*var\(--white\);', r'.nav__logo-text strong {\1color: var(--blue-dark);', html)
html = re.sub(r'\.nav__links a\s*\{([^\}]*)color:\s*rgba\(255,255,255,0\.7\);', r'.nav__links a {\1color: var(--dark-gray);', html)
html = re.sub(r'\.nav__links a:hover\s*\{([^\}]*)color:\s*var\(--white\);\s*background:\s*rgba\(255,255,255,0\.08\);', r'.nav__links a:hover {\1color: var(--blue-dark); background: rgba(0, 90, 155, 0.05);', html)

# Fix Mobile menu overlay
html = html.replace('background: rgba(0, 26, 50, 0.98);', 'background: rgba(255, 255, 255, 0.98);')
html = re.sub(r'\.nav__mobile-links a\s*\{([^\}]*)color:\s*var\(--white\);', r'.nav__mobile-links a {\1color: var(--blue-dark);', html)
html = html.replace('background: rgba(255,255,255,0.05);', 'background: rgba(0,90,155,0.05);')

# Hero Background
html = html.replace('background: linear-gradient(135deg, #002b54 0%, #004b87 50%, #005a9b 100%);', 'background: var(--white); border-bottom: 1px solid var(--border);')
html = html.replace('background: linear-gradient(135deg, #001a32 0%, #003766 50%, #005a9b 100%);', 'background: var(--white); border-bottom: 1px solid var(--border);')

# Hero text colors
html = re.sub(r'\.hero__title\s*\{([^\}]*)color:\s*var\(--white\);', r'.hero__title {\1color: var(--blue-dark);', html)
html = re.sub(r'\.hero__subtitle\s*\{([^\}]*)color:\s*rgba\(255,255,255,0\.85\);', r'.hero__subtitle {\1color: var(--dark-gray);', html)

# Stats band
html = re.sub(r'\.stats\s*\{([^\}]*)background:\s*var\(--blue-dark\);([^\}]*)color:\s*var\(--white\);', r'.stats {\1background: var(--white); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);\2color: var(--blue-dark);', html)
html = html.replace('color: var(--amber); /* label color */', 'color: var(--amber);')
html = html.replace('color: var(--white);', 'color: var(--blue-dark);') # This might replace too many, let's revert it and be specific

# Specific white replacements in HTML body
# "12+ Years" label color etc.
html = html.replace('<div class="stat-item reveal" style="color: var(--white);">', '<div class="stat-item reveal" style="color: var(--blue-dark);">')
html = html.replace('<h3 style="font-family: var(--ff-head); font-size: 2.5rem; font-weight: 800; color: var(--white); margin-bottom: 0.5rem;"', '<h3 style="font-family: var(--ff-head); font-size: 2.5rem; font-weight: 800; color: var(--blue-dark); margin-bottom: 0.5rem;"')

# Footer
html = html.replace('background: #001a32;', 'background: var(--white); border-top: 1px solid var(--border);')
html = html.replace('background: #002b54;', 'background: var(--white);')
html = html.replace('color: rgba(255,255,255,0.7);', 'color: var(--dark-gray);')
html = html.replace('border-top: 1px solid rgba(255,255,255,0.1);', 'border-top: 1px solid var(--border);')

# Contact section 
html = html.replace('background: var(--blue-dark);', 'background: var(--white);')
html = html.replace('background: rgba(255,255,255,0.03);', 'background: var(--white); box-shadow: 0 4px 20px rgba(0,0,0,0.05); border: 1px solid var(--border);')
html = html.replace('border: 1px solid rgba(255,255,255,0.1);', '')

# Replace Fleet images to point to the new files (assuming user placed them or I will instruct them)
# Using placeholder names for the attached images: fleet1.jpg, fleet2.jpg
html = html.replace('images/il1.jpeg', 'images/fleet1.jpg')
html = html.replace('images/il2.jpeg', 'images/fleet2.jpg')

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')
