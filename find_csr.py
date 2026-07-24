with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    with open(r'c:\Users\Admin\Downloads\gpcgroup\csr_lines.txt', 'w', encoding='utf-8') as out:
        for i, line in enumerate(f):
            if 'csr' in line.lower():
                out.write(f'{i+1}: {line.strip()}\n')
