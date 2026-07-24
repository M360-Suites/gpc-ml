import re

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Company Name
html = html.replace('GPC Group Limited', 'GPC Energy and Logistics Limited')
html = html.replace('GPC Group Ltd', 'GPC Energy and Logistics Ltd')
html = html.replace('GPC Group', 'GPC Energy and Logistics')

# Update title tag if needed
html = html.replace('<title>GPC Energy and Logistics Limited — Always Good To Go</title>', '<title>GPC Energy and Logistics Limited — Always Good To Go</title>')

# 2. Typography
# Remove Google Fonts
html = re.sub(r'<link href=\"https://fonts.googleapis.com/css2\?family=[^>]+>', '', html)
html = html.replace('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n', '')

# Replace font variables
html = html.replace("--ff-head: 'Sora', system-ui, sans-serif;", "--ff-head: 'Segoe UI', 'Lucida Sans', system-ui, sans-serif;")
html = html.replace("--ff-body: 'Plus Jakarta Sans', system-ui, sans-serif;", "--ff-body: 'Segoe UI', 'Lucida Sans', system-ui, sans-serif;")

# 3. Colors & Mostly White Theme
# Update nav
html = html.replace('background: rgba(0, 26, 50, 0.92);', 'background: rgba(255, 255, 255, 0.95);')
html = html.replace('background: rgba(0, 26, 50, 0.98);', 'background: rgba(255, 255, 255, 0.98);')
html = html.replace('border-bottom: 1px solid var(--border-light);', 'border-bottom: 1px solid rgba(0, 90, 155, 0.1);')

# Update nav text colors
html = html.replace('color: var(--white);', 'color: var(--blue-dark);') # General white text to dark blue
html = html.replace('color: rgba(255,255,255,0.7);', 'color: var(--dark-gray);')
html = html.replace('background: rgba(255,255,255,0.08);', 'background: rgba(0, 90, 155, 0.05);')

# Revert specific instances where white is still needed (e.g., buttons)
html = html.replace('color: var(--blue-dark); /* for white */', 'color: var(--white);')

# Make hero mostly white
html = html.replace('background: linear-gradient(135deg, #002b54 0%, #004b87 50%, #005a9b 100%);', 'background: var(--white);')
# In Hero, text was white. Now it needs to be dark
html = re.sub(r'color: var\(--white\);(?=.*?Hero)', 'color: var(--blue-dark);', html, flags=re.DOTALL)

# Stats band (currently blue with white text)
html = html.replace('background: var(--blue-dark);', 'background: var(--white); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);')

# Footer (currently dark blue)
html = html.replace('background: #001a32;', 'background: var(--off-white); border-top: 1px solid var(--border);')
html = html.replace('border-top: 1px solid rgba(255,255,255,0.1);', 'border-top: 1px solid var(--border);')

# Replace inline fleet images with placeholders referencing the new images
# In the fleet section, we have il1.jpeg maybe. Let's add the fleet images.
html = html.replace('images/il1.jpeg', 'images/fleet1.jpg')
html = html.replace('images/il2.jpeg', 'images/fleet2.jpg')

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')
