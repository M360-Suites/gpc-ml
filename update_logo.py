import re

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the text logo with the image logo in the nav
new_logo = '''<a href="#" class="nav__logo">
        <img src="images/logo.jpeg" alt="GPC Energy and Logistics Limited" style="height: 44px; width: auto; object-fit: contain;">
      </a>'''

html = re.sub(r'<a href="#" class="nav__logo">.*?</a>', new_logo, html, flags=re.DOTALL)

# In case there's a logo in the footer (previously using nav__logo class or similar), replace it there too if applicable
# Let's see if footer has a logo
new_footer_logo = '''<div class="footer__logo" style="margin-bottom: 1.5rem;">
          <img src="images/logo.jpeg" alt="GPC Energy and Logistics Limited" style="height: 40px; width: auto; object-fit: contain;">
        </div>'''
html = re.sub(r'<div class="footer__brand">.*?<p', new_footer_logo + '\n        <p', html, flags=re.DOTALL)

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated logo successfully.')
