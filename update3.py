with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add "Team" to navigation
# Find desktop nav and insert before Contact
html = html.replace('<li><a href="#csr">Impact</a></li>', '<li><a href="#csr">Impact</a></li>\n          <li><a href="#team">Team</a></li>')

# Find mobile nav and insert before Contact
html = html.replace('<li style="animation-delay: 0.4s"><a href="#csr">Impact</a></li>', '<li style="animation-delay: 0.4s"><a href="#csr">Impact</a></li>\n        <li style="animation-delay: 0.5s"><a href="#team">Team</a></li>')

# 2. Spice up the team cards
old_card_1 = '<div class="team-card reveal reveal-delay-1" style="background: var(--white); border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,90,155,0.05); transition: transform 0.3s, box-shadow 0.3s;">'
new_card_1 = '<div class="team-card reveal reveal-delay-1" style="background: var(--white); border-radius: 20px; overflow: hidden; box-shadow: 0 12px 40px rgba(0,90,155,0.08); transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); border: 1px solid rgba(0,90,155,0.05); transform-origin: center bottom;" onmouseover="this.style.transform=\'translateY(-10px) scale(1.02)\'; this.style.boxShadow=\'0 20px 50px rgba(0,90,155,0.12)\'" onmouseout="this.style.transform=\'translateY(0) scale(1)\'; this.style.boxShadow=\'0 12px 40px rgba(0,90,155,0.08)\'">'
html = html.replace(old_card_1, new_card_1)

old_card_2 = '<div class="team-card reveal reveal-delay-2" style="background: var(--white); border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,90,155,0.05); transition: transform 0.3s, box-shadow 0.3s;">'
new_card_2 = '<div class="team-card reveal reveal-delay-2" style="background: var(--white); border-radius: 20px; overflow: hidden; box-shadow: 0 12px 40px rgba(0,90,155,0.08); transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); border: 1px solid rgba(0,90,155,0.05); transform-origin: center bottom;" onmouseover="this.style.transform=\'translateY(-10px) scale(1.02)\'; this.style.boxShadow=\'0 20px 50px rgba(0,90,155,0.12)\'" onmouseout="this.style.transform=\'translateY(0) scale(1)\'; this.style.boxShadow=\'0 12px 40px rgba(0,90,155,0.08)\'">'
html = html.replace(old_card_2, new_card_2)

old_card_3 = '<div class="team-card reveal reveal-delay-3" style="background: var(--white); border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,90,155,0.05); transition: transform 0.3s, box-shadow 0.3s;">'
new_card_3 = '<div class="team-card reveal reveal-delay-3" style="background: var(--white); border-radius: 20px; overflow: hidden; box-shadow: 0 12px 40px rgba(0,90,155,0.08); transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); border: 1px solid rgba(0,90,155,0.05); transform-origin: center bottom;" onmouseover="this.style.transform=\'translateY(-10px) scale(1.02)\'; this.style.boxShadow=\'0 20px 50px rgba(0,90,155,0.12)\'" onmouseout="this.style.transform=\'translateY(0) scale(1)\'; this.style.boxShadow=\'0 12px 40px rgba(0,90,155,0.08)\'">'
html = html.replace(old_card_3, new_card_3)

old_card_4 = '<div class="team-card reveal reveal-delay-4" style="background: var(--white); border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,90,155,0.05); transition: transform 0.3s, box-shadow 0.3s;">'
new_card_4 = '<div class="team-card reveal reveal-delay-4" style="background: var(--white); border-radius: 20px; overflow: hidden; box-shadow: 0 12px 40px rgba(0,90,155,0.08); transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1); border: 1px solid rgba(0,90,155,0.05); transform-origin: center bottom;" onmouseover="this.style.transform=\'translateY(-10px) scale(1.02)\'; this.style.boxShadow=\'0 20px 50px rgba(0,90,155,0.12)\'" onmouseout="this.style.transform=\'translateY(0) scale(1)\'; this.style.boxShadow=\'0 12px 40px rgba(0,90,155,0.08)\'">'
html = html.replace(old_card_4, new_card_4)

# Spice up image hover effect and details container
old_img = 'style="width: 100%; aspect-ratio: 1; object-fit: cover;"'
new_img = 'style="width: 100%; aspect-ratio: 1; object-fit: cover; transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);"'
html = html.replace(old_img, new_img)

# We need to make the image scale on hover, so we add a wrapper or just use the inline style onmouseover
# Actually, since we added the onmouseover to the card above, we can just let CSS handle it if we had classes, but we are using inline styles.
# Let's write out the entire team section again for cleanliness.

old_team_section = html[html.find('<!-- TEAM -->'):html.find('<!-- PARTNERS -->')]

new_team_section = '''<!-- TEAM -->
<section class="team" id="team" aria-labelledby="team-heading" style="background: var(--off-white); padding: 7rem 0;">
  <div class="container">
    <div class="team__header reveal" style="text-align: center; margin-bottom: 4rem;">
      <span class="label" style="justify-content:center;">Our Leadership</span>
      <h2 id="team-heading" style="font-family: var(--ff-head); font-size: clamp(1.9rem, 2.8vw, 2.6rem); font-weight: 800; color: var(--blue-dark); line-height: 1.15; margin-bottom: 1rem; letter-spacing: -0.02em;">Meet the Core Team</h2>
      <p style="color: var(--dark-gray); font-size: 1rem; max-width: 600px; margin: 0 auto;">Dedicated professionals driving innovation and operational excellence across West Africa.</p>
    </div>
    
    <style>
      .team-card-v2 {
        background: var(--white);
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 12px 40px rgba(0,90,155,0.06);
        transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
        border: 1px solid rgba(0,90,155,0.05);
        position: relative;
        cursor: pointer;
      }
      .team-card-v2:hover {
        transform: translateY(-12px);
        box-shadow: 0 24px 64px rgba(0,90,155,0.12);
      }
      .team-card-v2__img-wrap {
        overflow: hidden;
        aspect-ratio: 1;
        position: relative;
      }
      .team-card-v2__img-wrap::after {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(to top, rgba(0,43,84,0.4) 0%, transparent 50%);
        opacity: 0;
        transition: opacity 0.4s ease;
      }
      .team-card-v2:hover .team-card-v2__img-wrap::after {
        opacity: 1;
      }
      .team-card-v2 img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.7s cubic-bezier(0.2, 0.8, 0.2, 1);
      }
      .team-card-v2:hover img {
        transform: scale(1.08);
      }
      .team-card-v2__content {
        padding: 1.75rem 1.5rem;
        text-align: center;
        position: relative;
        background: var(--white);
        z-index: 2;
      }
      .team-card-v2__social {
        display: flex;
        gap: 12px;
        justify-content: center;
        margin-top: 1rem;
        opacity: 0;
        transform: translateY(10px);
        transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
      }
      .team-card-v2:hover .team-card-v2__social {
        opacity: 1;
        transform: translateY(0);
      }
      .social-icon {
        width: 32px; height: 32px;
        border-radius: 50%;
        background: var(--off-white);
        display: flex; align-items: center; justify-content: center;
        color: var(--blue);
        transition: background 0.3s, color 0.3s;
      }
      .social-icon:hover {
        background: var(--blue);
        color: var(--white);
      }
    </style>

    <div class="team__grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 2.5rem;">
      <!-- Team Member 1 -->
      <div class="team-card-v2 reveal reveal-delay-1">
        <div class="team-card-v2__img-wrap">
          <img src="https://via.placeholder.com/500x500/eef2f7/005a9b?text=CEO" alt="CEO">
        </div>
        <div class="team-card-v2__content">
          <h3 style="font-family: var(--ff-head); font-size: 1.25rem; color: var(--blue-dark); margin-bottom: 0.3rem;">John Doe</h3>
          <p style="font-size: 0.85rem; color: var(--amber); font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;">Chief Executive Officer</p>
          <div class="team-card-v2__social">
            <a href="#" class="social-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
            <a href="#" class="social-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
          </div>
        </div>
      </div>
      <!-- Team Member 2 -->
      <div class="team-card-v2 reveal reveal-delay-2">
        <div class="team-card-v2__img-wrap">
          <img src="https://via.placeholder.com/500x500/eef2f7/005a9b?text=COO" alt="COO">
        </div>
        <div class="team-card-v2__content">
          <h3 style="font-family: var(--ff-head); font-size: 1.25rem; color: var(--blue-dark); margin-bottom: 0.3rem;">Jane Smith</h3>
          <p style="font-size: 0.85rem; color: var(--amber); font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;">Chief Operating Officer</p>
          <div class="team-card-v2__social">
            <a href="#" class="social-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
            <a href="#" class="social-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
          </div>
        </div>
      </div>
      <!-- Team Member 3 -->
      <div class="team-card-v2 reveal reveal-delay-3">
        <div class="team-card-v2__img-wrap">
          <img src="https://via.placeholder.com/500x500/eef2f7/005a9b?text=CFO" alt="CFO">
        </div>
        <div class="team-card-v2__content">
          <h3 style="font-family: var(--ff-head); font-size: 1.25rem; color: var(--blue-dark); margin-bottom: 0.3rem;">Michael Johnson</h3>
          <p style="font-size: 0.85rem; color: var(--amber); font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;">Chief Financial Officer</p>
          <div class="team-card-v2__social">
            <a href="#" class="social-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
            <a href="#" class="social-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
          </div>
        </div>
      </div>
      <!-- Team Member 4 -->
      <div class="team-card-v2 reveal reveal-delay-4">
        <div class="team-card-v2__img-wrap">
          <img src="https://via.placeholder.com/500x500/eef2f7/005a9b?text=CTO" alt="CTO">
        </div>
        <div class="team-card-v2__content">
          <h3 style="font-family: var(--ff-head); font-size: 1.25rem; color: var(--blue-dark); margin-bottom: 0.3rem;">Sarah Williams</h3>
          <p style="font-size: 0.85rem; color: var(--amber); font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;">Chief Technology Officer</p>
          <div class="team-card-v2__social">
            <a href="#" class="social-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
            <a href="#" class="social-icon"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
'''

html = html.replace(old_team_section, new_team_section)

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done injecting spiced up team cards and nav links')
