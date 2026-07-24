import re

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<section[^>]*id="fleet"[^>]*>.*?</section>', html, re.DOTALL)
if match:
    print('Fleet images found:', re.findall(r'images/[a-zA-Z0-9_\.]+', match.group(0)))
    print('\nContent:\n', match.group(0))
