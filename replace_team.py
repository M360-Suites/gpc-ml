import re

team_members = [
    {"name": "Dr Mike ASEKOME (Ph.d)", "role": "CHAIRMAN", "img": "team/mike.jpeg"},
    {"name": "Elvis Chukwudi OKONJI", "role": "MANAGING DIRECTOR/CHIEF EXECUTIVE OFFICER", "img": "team/elvis.jpeg"},
    {"name": "Opemikun IBITOYE", "role": "DEPUTY MANAGING DIRECTOR", "img": "team/ibitoye.jpeg"},
    {"name": "Olusola TIJANI", "role": "EXECUTIVE DIRECTOR, OPERATIONS AND BUSINESS DEVELOPMENT", "img": "team/tijani.jpeg"},
    {"name": "Hajiya Rakiya ABDULKADIR", "role": "NON EXECUTIVE DIRECTOR", "img": "team/hajiya.jpeg"},
    {"name": "Hajiya Hadiza Kubura", "role": "NON EXECUTIVE DIRECTOR", "img": "team/kubura.jpeg"},
    {"name": "Mrs. Ololade AYO-BRAIMOH", "role": "NON EXECUTIVE DIRECTOR", "img": "team/ololade.jpeg"},
    {"name": "HRM Jimoh rasaki", "role": "INDEPENDENT DIRECTOR", "img": "team/rasaki.jpeg"}
]

html_cards = []
for i, member in enumerate(team_members):
    delay = (i % 4) + 1
    card = f'''      <div class="team-card-v2 reveal reveal-delay-{delay}">
        <div class="team-card-v2__img-wrap">
          <img src="{member['img']}" alt="{member['name']}">
        </div>
        <div class="team-card-v2__content">
          <h3 style="font-family: var(--ff-head); font-size: 1.25rem; color: var(--blue-dark); margin-bottom: 0.3rem;">{member['name']}</h3>
          <p style="font-size: 0.85rem; color: var(--amber); font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;">{member['role']}</p>
          <div class="team-card-v2__social">
            <a href="#" class="social-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
            <a href="#" class="social-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
          </div>
        </div>
      </div>'''
    html_cards.append(card)

new_grid_content = '\n'.join(html_cards)

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace between <div class="team__grid" ...> and its closing </div>
pattern = r'(<div class="team__grid"[^>]*>).*?(</section>)'
def repl(m):
    return m.group(1) + '\n' + new_grid_content + '\n    </div>\n  </div>\n' + m.group(2)

new_content = re.sub(pattern, repl, content, flags=re.DOTALL)

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Team replaced.")
