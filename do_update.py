import re

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace emojis in footer and CTA
html = html.replace('&#128222; Call:', '<svg viewBox="0 0 24 24" width="18" height="18" style="vertical-align: middle; margin-right: 6px;" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg> Call:')
html = html.replace('<span class="footer__contact-icon">&#128205;</span>', '<span class="footer__contact-icon"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg></span>')
html = html.replace('<span class="footer__contact-icon">&#127981;</span>', '<span class="footer__contact-icon"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg></span>')
html = html.replace('<span class="footer__contact-icon">&#128222;</span>', '<span class="footer__contact-icon"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg></span>')
html = html.replace('<span class="footer__contact-icon">&#9993;&#65039;</span>', '<span class="footer__contact-icon"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg></span>')

# Replace CSR impact images
csr_start = html.find('<!-- CSR -->')
csr_end = html.find('<!-- PARTNERS -->')
if csr_start != -1 and csr_end != -1:
    csr_section = html[csr_start:csr_end]
    csr_section = csr_section.replace('images/il2.jpeg', 'images/i2.jpeg')
    csr_section = csr_section.replace('images/il1.jpeg', 'images/i1.jpeg')
    html = html[:csr_start] + csr_section + html[csr_end:]
else:
    print("Could not find CSR section")

# Inject team section
team_section = '''
<!-- TEAM -->
<section class="team" id="team" aria-labelledby="team-heading" style="background: var(--off-white); padding: 7rem 0;">
  <div class="container">
    <div class="team__header reveal" style="text-align: center; margin-bottom: 4rem;">
      <span class="label" style="justify-content:center;">Our Leadership</span>
      <h2 id="team-heading" style="font-family: var(--ff-head); font-size: clamp(1.9rem, 2.8vw, 2.6rem); font-weight: 800; color: var(--blue-dark); line-height: 1.15; margin-bottom: 1rem; letter-spacing: -0.02em;">Meet the Core Team</h2>
      <p style="color: var(--dark-gray); font-size: 1rem; max-width: 600px; margin: 0 auto;">Dedicated professionals driving innovation and operational excellence across West Africa.</p>
    </div>
    <div class="team__grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
      <!-- Team Member 1 -->
      <div class="team-card reveal reveal-delay-1" style="background: var(--white); border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,90,155,0.05); transition: transform 0.3s, box-shadow 0.3s;">
        <img src="https://via.placeholder.com/400x400/eef2f7/005a9b?text=CEO" alt="CEO" style="width: 100%; aspect-ratio: 1; object-fit: cover;">
        <div style="padding: 1.5rem; text-align: center;">
          <h3 style="font-family: var(--ff-head); font-size: 1.15rem; color: var(--blue-dark); margin-bottom: 0.25rem;">John Doe</h3>
          <p style="font-size: 0.9rem; color: var(--amber); font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Chief Executive Officer</p>
        </div>
      </div>
      <!-- Team Member 2 -->
      <div class="team-card reveal reveal-delay-2" style="background: var(--white); border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,90,155,0.05); transition: transform 0.3s, box-shadow 0.3s;">
        <img src="https://via.placeholder.com/400x400/eef2f7/005a9b?text=COO" alt="COO" style="width: 100%; aspect-ratio: 1; object-fit: cover;">
        <div style="padding: 1.5rem; text-align: center;">
          <h3 style="font-family: var(--ff-head); font-size: 1.15rem; color: var(--blue-dark); margin-bottom: 0.25rem;">Jane Smith</h3>
          <p style="font-size: 0.9rem; color: var(--amber); font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Chief Operating Officer</p>
        </div>
      </div>
      <!-- Team Member 3 -->
      <div class="team-card reveal reveal-delay-3" style="background: var(--white); border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,90,155,0.05); transition: transform 0.3s, box-shadow 0.3s;">
        <img src="https://via.placeholder.com/400x400/eef2f7/005a9b?text=CFO" alt="CFO" style="width: 100%; aspect-ratio: 1; object-fit: cover;">
        <div style="padding: 1.5rem; text-align: center;">
          <h3 style="font-family: var(--ff-head); font-size: 1.15rem; color: var(--blue-dark); margin-bottom: 0.25rem;">Michael Johnson</h3>
          <p style="font-size: 0.9rem; color: var(--amber); font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Chief Financial Officer</p>
        </div>
      </div>
      <!-- Team Member 4 -->
      <div class="team-card reveal reveal-delay-4" style="background: var(--white); border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,90,155,0.05); transition: transform 0.3s, box-shadow 0.3s;">
        <img src="https://via.placeholder.com/400x400/eef2f7/005a9b?text=CTO" alt="CTO" style="width: 100%; aspect-ratio: 1; object-fit: cover;">
        <div style="padding: 1.5rem; text-align: center;">
          <h3 style="font-family: var(--ff-head); font-size: 1.15rem; color: var(--blue-dark); margin-bottom: 0.25rem;">Sarah Williams</h3>
          <p style="font-size: 0.9rem; color: var(--amber); font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Chief Technology Officer</p>
        </div>
      </div>
    </div>
  </div>
</section>
'''
if '<!-- TEAM -->' not in html:
    html = html.replace('<!-- PARTNERS -->', team_section + '\n<!-- PARTNERS -->')
else:
    print("Team section already exists")

# Make the UI calmer and more elegant
html = html.replace('background: linear-gradient(135deg, #001a32 0%, #003766 50%, #005a9b 100%);', 'background: linear-gradient(135deg, #002b54 0%, #004b87 50%, #005a9b 100%);')
html = html.replace('box-shadow: 0 24px 64px rgba(0,90,155,0.15);', 'box-shadow: 0 24px 64px rgba(0,90,155,0.08);')
html = html.replace('box-shadow: 0 24px 64px rgba(0,90,155,0.18);', 'box-shadow: 0 24px 64px rgba(0,90,155,0.1);')
html = html.replace('box-shadow: 0 24px 64px rgba(0,64,112,0.2);', 'box-shadow: 0 24px 64px rgba(0,64,112,0.1);')

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done updating HTML')
