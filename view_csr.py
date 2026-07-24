import re

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<!-- CSR -->.*?(?=<!-- PARTNERS -->)', html, re.DOTALL)
if match:
    print('CSR Images:')
    print(re.findall(r'images/[a-zA-Z0-9_\.]+', match.group(0)))
else:
    print('CSR not found')
