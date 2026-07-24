import re

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the specific color rule in .hero__sub
old_hero_sub = '''.hero__sub {
  font-size: 1.05rem;
  color: rgba(255,255,255,0.65);
  max-width: 460px;
  line-height: 1.8;
  margin-bottom: 2.5rem;
}'''

new_hero_sub = '''.hero__sub {
  font-size: 1.05rem;
  color: var(--dark-gray);
  max-width: 460px;
  line-height: 1.8;
  margin-bottom: 2.5rem;
}'''

html = html.replace(old_hero_sub, new_hero_sub)

# Just in case, let's also make sure we didn't miss .hero__badge-text or other hero texts
html = html.replace('color: var(--amber-light);', 'color: var(--amber-dark);')

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed hero__sub contrast")
