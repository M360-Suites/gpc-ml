import re

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add a secondary image to the fleet section
old_fleet_img_html = '''<div class="fleet__img-main-wrap">
          <img class="fleet__img-main" src="images/fleet1.jpg" alt="GPC logistics truck at loading dock" loading="lazy">
        </div>'''

new_fleet_img_html = '''<div class="fleet__img-main-wrap" style="position: relative;">
          <img class="fleet__img-main" src="images/fleet1.jpg" alt="GPC Energy and Logistics truck at loading dock" loading="lazy" style="border-radius: 12px; width: 100%; box-shadow: 0 12px 30px rgba(0,0,0,0.1);">
          <img class="fleet__img-secondary" src="images/fleet2.jpg" alt="GPC Energy and Logistics truck cabin" loading="lazy" style="position: absolute; bottom: -30px; left: -30px; width: 50%; border-radius: 12px; border: 6px solid var(--white); box-shadow: 0 12px 30px rgba(0,0,0,0.15);">
        </div>'''

html = html.replace(old_fleet_img_html, new_fleet_img_html)

# Also fix the button color in fleet
html = html.replace('<a href="#contact" class="btn-blue">Book a Truck Today</a>', '<a href="#contact" class="btn-dark">Book a Truck Today</a>')

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated fleet images')
