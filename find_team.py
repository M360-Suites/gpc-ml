with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    with open(r'c:\Users\Admin\Downloads\gpcgroup\out_team.txt', 'w', encoding='utf-8') as out:
        for i, line in enumerate(f):
            if 'class="team"' in line or 'class="team-card' in line or 'team__grid' in line:
                out.write(f'{i+1}: {line.strip()}\n')
