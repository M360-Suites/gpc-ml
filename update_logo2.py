with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Nav Logo
old_nav_logo = '''<a href="/" class="nav__logo" aria-label="GPC Energy and Logistics Home">
      <div class="nav__logo-badge">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M5 12l5 5 9-9" stroke="#004070" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        </svg>
      </div>
      <div class="nav__logo-text">
        <strong>GPC Energy and Logistics</strong>
        <span>Always Good To Go</span>
      </div>
    </a>'''

new_nav_logo = '''<a href="/" class="nav__logo" aria-label="GPC Energy and Logistics Home">
      <img src="images/logo.jpeg" alt="GPC Energy and Logistics Logo" style="height: 52px; width: auto; object-fit: contain;">
    </a>'''

# Replace Footer Logo
old_footer_logo = '''<div class="nav__logo" style="margin-bottom:1rem;">
          <div class="nav__logo-badge">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M5 12l5 5 9-9" stroke="#004070" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>
          </div>
          <div class="nav__logo-text">
            <strong>GPC Energy and Logistics</strong>
            <span>Always Good To Go</span>
          </div>
        </div>'''

new_footer_logo = '''<div class="nav__logo" style="margin-bottom:1rem;">
          <img src="images/logo.jpeg" alt="GPC Energy and Logistics Logo" style="height: 52px; width: auto; object-fit: contain;">
        </div>'''

html = html.replace(old_nav_logo, new_nav_logo)
html = html.replace(old_footer_logo, new_footer_logo)

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated actual logo")
