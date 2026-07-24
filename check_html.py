with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
match = re.search(r'<section class="cta-section".*?</section>', html, re.DOTALL)
if match:
    print('CTA Section:\n' + match.group(0)[:500])

match_footer = re.search(r'<footer.*?</footer>', html, re.DOTALL)
if match_footer:
    print('\nFooter:\n' + match_footer.group(0)[-500:])
