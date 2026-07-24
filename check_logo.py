with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Has images/logo.jpeg:", "images/logo.jpeg" in html)
print("Nav logo text:", "GPC Energy and Logistics Limited" in html)
