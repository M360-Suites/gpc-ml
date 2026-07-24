with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    with open(r'c:\Users\Admin\Downloads\gpcgroup\out_consultation.txt', 'w', encoding='utf-8') as out:
        for i, line in enumerate(f):
            if 'consultation' in line.lower() or 'move your' in line.lower():
                out.write(f'{i+1}: {line.strip()}\n')
