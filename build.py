
html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="GPC Group Limited — Nigeria's leading precision truck logistics and supply chain partner. Transportation, Warehousing, Fleet Management, Import & Export across West Africa.">
<meta property="og:title" content="GPC Group Limited — Always Good To Go">
<meta property="og:description" content="West Africa's foremost precision logistics company. Delivering Excellence, Driving Success.">
<meta property="og:type" content="website">
<title>GPC Group Limited — Always Good To Go</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Sora:wght@400;600;700;800&display=swap" rel="stylesheet">

<style>
/* ── Reset ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
img { display: block; max-width: 100%; }
a { text-decoration: none; color: inherit; }
ul { list-style: none; }

/* ── Brand Tokens ── */
:root {
  --blue:        #005a9b;
  --blue-dark:   #004070;
  --blue-mid:    #006bbf;
  --blue-light:  #0a7fd4;
  --blue-glow:   rgba(0, 90, 155, 0.18);
  --amber:       #fbb60c;
  --amber-dark:  #e0a00a;
  --amber-light: #fdd060;
  --amber-glow:  rgba(251, 182, 12, 0.2);
  --white:       #ffffff;
  --off-white:   #f7f9fc;
  --light-gray:  #eef2f7;
  --mid-gray:    #94a3b8;
  --dark-gray:   #334155;
  --text:        #1e293b;
  --border:      rgba(0, 90, 155, 0.12);
  --border-light: rgba(255,255,255,0.12);

  --ff-head: 'Sora', system-ui, sans-serif;
  --ff-body: 'Plus Jakarta Sans', system-ui, sans-serif;

  --max-w: 1280px;
  --gutter: clamp(1.25rem, 5vw, 4rem);
  --nav-h: 72px;

  --ease-out: cubic-bezier(0.22, 1, 0.36, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* ── Base ── */
body {
  font-family: var(--ff-body);
  font-size: 16px;
  line-height: 1.7;
  color: var(--text);
  background: var(--white);
  overflow-x: hidden;
}

/* ── Utility ── */
.container {
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 var(--gutter);
}
.label {
  font-family: var(--ff-head);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--amber);
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 1rem;
}
.label::before {
  content: '';
  display: block;
  width: 24px;
  height: 2px;
  background: var(--amber);
  flex-shrink: 0;
}
.label--light { color: var(--amber-light); }
.label--light::before { background: var(--amber-light); }

/* ── Scroll-reveal ── */
.reveal {
  opacity: 0;
  transform: translateY(32px);
  transition: opacity 0.7s var(--ease-out), transform 0.7s var(--ease-out);
}
.reveal.visible { opacity: 1; transform: none; }
.reveal-left {
  opacity: 0;
  transform: translateX(-40px);
  transition: opacity 0.8s var(--ease-out), transform 0.8s var(--ease-out);
}
.reveal-left.visible { opacity: 1; transform: none; }
.reveal-right {
  opacity: 0;
  transform: translateX(40px);
  transition: opacity 0.8s var(--ease-out), transform 0.8s var(--ease-out);
}
.reveal-right.visible { opacity: 1; transform: none; }
.reveal-delay-1 { transition-delay: 0.1s; }
.reveal-delay-2 { transition-delay: 0.2s; }
.reveal-delay-3 { transition-delay: 0.3s; }
.reveal-delay-4 { transition-delay: 0.4s; }
.reveal-delay-5 { transition-delay: 0.5s; }

/* ═══ NAV ═══ */
.nav {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 200;
  height: var(--nav-h);
  background: rgba(0, 26, 50, 0.92);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border-light);
  transition: background 0.4s, box-shadow 0.4s;
}
.nav.scrolled {
  background: rgba(0, 26, 50, 0.98);
  box-shadow: 0 4px 32px rgba(0,0,0,0.25);
}
.nav__inner {
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 var(--gutter);
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
}
.nav__logo {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
}
.nav__logo-badge {
  width: 42px; height: 42px;
  background: var(--amber);
  border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
  transition: transform 0.3s var(--ease-spring);
}
.nav__logo:hover .nav__logo-badge { transform: rotate(-5deg) scale(1.05); }
.nav__logo-text { display: flex; flex-direction: column; line-height: 1.1; }
.nav__logo-text strong {
  font-family: var(--ff-head);
  font-weight: 800;
  font-size: 18px;
  color: var(--white);
  letter-spacing: -0.01em;
}
.nav__logo-text span {
  font-size: 9px;
  font-weight: 600;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--amber-light);
}
.nav__links {
  display: flex;
  align-items: center;
  gap: 0.25rem;
}
.nav__links a {
  font-size: 13.5px;
  font-weight: 600;
  letter-spacing: 0.02em;
  color: rgba(255,255,255,0.7);
  padding: 6px 14px;
  border-radius: 6px;
  transition: color 0.2s, background 0.2s;
}
.nav__links a:hover { color: var(--white); background: rgba(255,255,255,0.08); }
.nav__cta {
  background: var(--amber) !important;
  color: var(--blue-dark) !important;
  font-weight: 700 !important;
  border-radius: 8px !important;
  padding: 8px 20px !important;
  font-size: 13px !important;
  transition: background 0.2s, transform 0.2s !important;
}
.nav__cta:hover {
  background: var(--amber-dark) !important;
  transform: translateY(-1px) !important;
}
.nav__hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
  padding: 6px;
  border: none;
  background: none;
}
.nav__hamburger span {
  display: block;
  width: 24px; height: 2px;
  background: var(--white);
  border-radius: 2px;
  transition: transform 0.3s, opacity 0.3s;
}
.nav__hamburger.active span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
.nav__hamburger.active span:nth-child(2) { opacity: 0; }
.nav__hamburger.active span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }

.nav__mobile {
  position: fixed;
  inset: var(--nav-h) 0 0 0;
  background: rgba(0, 20, 45, 0.97);
  backdrop-filter: blur(20px);
  z-index: 190;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  transform: translateX(100%);
  transition: transform 0.4s var(--ease-out);
}
.nav__mobile.open { transform: translateX(0); }
.nav__mobile a {
  font-family: var(--ff-head);
  font-size: 1.4rem;
  font-weight: 700;
  color: rgba(255,255,255,0.8);
  transition: color 0.2s;
}
.nav__mobile a:hover { color: var(--amber); }

/* ═══ HERO ═══ */
.hero {
  min-height: 100vh;
  background: linear-gradient(135deg, #001a32 0%, #003766 50%, #005a9b 100%);
  display: grid;
  grid-template-columns: 1fr 1fr;
  position: relative;
  overflow: hidden;
  padding-top: var(--nav-h);
}
.hero::before {
  content: '';
  position: absolute;
  width: 600px; height: 600px;
  background: radial-gradient(circle, rgba(251,182,12,0.1) 0%, transparent 70%);
  top: -100px; right: 20%;
  border-radius: 50%;
  animation: orb-float 8s ease-in-out infinite;
  pointer-events: none;
}
.hero::after {
  content: '';
  position: absolute;
  width: 400px; height: 400px;
  background: radial-gradient(circle, rgba(0,107,191,0.3) 0%, transparent 70%);
  bottom: -50px; left: 10%;
  border-radius: 50%;
  animation: orb-float 10s ease-in-out infinite reverse;
  pointer-events: none;
}
@keyframes orb-float {
  0%, 100% { transform: translateY(0) scale(1); }
  50% { transform: translateY(-30px) scale(1.08); }
}
.hero__left {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 5rem var(--gutter) 5rem calc(var(--gutter) + 1.5rem);
  position: relative;
  z-index: 2;
}
.hero__badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border: 1px solid rgba(251,182,12,0.4);
  background: rgba(251,182,12,0.08);
  padding: 6px 16px;
  border-radius: 100px;
  width: fit-content;
  margin-bottom: 2rem;
  animation: badge-glow 3s ease-in-out infinite;
}
@keyframes badge-glow {
  0%, 100% { box-shadow: 0 0 0 0 rgba(251,182,12,0); }
  50% { box-shadow: 0 0 20px rgba(251,182,12,0.15); }
}
.hero__badge-dot {
  width: 6px; height: 6px;
  background: var(--amber);
  border-radius: 50%;
  animation: pulse-dot 2s infinite;
}
@keyframes pulse-dot {
  0%, 100% { opacity: 1; box-shadow: 0 0 0 0 rgba(251,182,12,0.4); }
  50% { opacity: 0.7; box-shadow: 0 0 0 6px rgba(251,182,12,0); }
}
.hero__badge-text {
  font-family: var(--ff-head);
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--amber-light);
}
.hero__headline {
  font-family: var(--ff-head);
  font-size: clamp(2.8rem, 4.5vw, 5rem);
  font-weight: 800;
  line-height: 1.03;
  color: var(--white);
  margin-bottom: 1.5rem;
  letter-spacing: -0.02em;
}
.hero__headline em {
  font-style: normal;
  color: var(--amber);
  position: relative;
}
.hero__headline em::after {
  content: '';
  position: absolute;
  bottom: 2px; left: 0; right: 0;
  height: 3px;
  background: var(--amber);
  border-radius: 2px;
  opacity: 0.4;
}
.hero__sub {
  font-size: 1.05rem;
  color: rgba(255,255,255,0.65);
  max-width: 460px;
  line-height: 1.8;
  margin-bottom: 2.5rem;
}
.hero__actions {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 3.5rem;
}
.btn-primary {
  background: var(--amber);
  color: var(--blue-dark);
  padding: 14px 32px;
  font-family: var(--ff-head);
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.03em;
  border-radius: 10px;
  display: inline-block;
  transition: background 0.2s, transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 4px 20px var(--amber-glow);
}
.btn-primary:hover {
  background: var(--amber-dark);
  transform: translateY(-2px);
  box-shadow: 0 8px 28px rgba(251,182,12,0.4);
}
.btn-outline {
  color: rgba(255,255,255,0.85);
  font-size: 14px;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border: 1.5px solid rgba(255,255,255,0.25);
  padding: 13px 26px;
  border-radius: 10px;
  transition: border-color 0.2s, color 0.2s, background 0.2s;
}
.btn-outline:hover {
  border-color: var(--amber);
  color: var(--amber);
  background: rgba(251,182,12,0.06);
}
.btn-outline svg { width: 16px; height: 16px; transition: transform 0.2s; }
.btn-outline:hover svg { transform: translateX(4px); }

.hero__stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  border-top: 1px solid rgba(255,255,255,0.1);
  padding-top: 2rem;
}
.hero__stat {
  padding-right: 1.5rem;
  border-right: 1px solid rgba(255,255,255,0.1);
}
.hero__stat:last-child { border-right: none; padding-right: 0; padding-left: 1.5rem; }
.hero__stat:nth-child(2) { padding: 0 1.5rem; }
.hero__stat-num {
  font-family: var(--ff-head);
  font-size: 2.4rem;
  font-weight: 800;
  color: var(--white);
  line-height: 1;
}
.hero__stat-num sup { font-size: 1rem; color: var(--amber); vertical-align: super; }
.hero__stat-label {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.4);
  margin-top: 6px;
}
.hero__right {
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}
.hero__right::before {
  content: '';
  position: absolute;
  top: 0; left: -60px; bottom: 0;
  width: 120px;
  background: linear-gradient(135deg, #001a32 0%, #003766 100%);
  clip-path: polygon(0 0, 40% 0, 100% 100%, 0 100%);
  z-index: 2;
}
.hero__img-wrap {
  position: relative;
  z-index: 1;
  width: 100%;
  height: 100%;
  min-height: 500px;
  background: linear-gradient(135deg,#003260,#001a32);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}
.hero__img-wrap img {
  width: 100%;
  max-height: 100%;
  object-fit: contain;
}
.hero__float-badge {
  position: absolute;
  bottom: 2.5rem;
  left: 2rem;
  background: var(--white);
  border-radius: 12px;
  padding: 1rem 1.25rem;
  box-shadow: 0 12px 40px rgba(0,0,0,0.25);
  z-index: 3;
  display: flex;
  align-items: center;
  gap: 12px;
  animation: float-badge 4s ease-in-out infinite;
}
@keyframes float-badge {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}
.hero__float-badge-icon {
  width: 40px; height: 40px;
  background: var(--blue);
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.hero__float-badge-icon svg { width: 22px; height: 22px; stroke: white; fill: none; stroke-width: 1.8; }
.hero__float-badge-text strong {
  display: block;
  font-family: var(--ff-head);
  font-weight: 800;
  font-size: 18px;
  color: var(--blue-dark);
  line-height: 1;
}
.hero__float-badge-text span {
  font-size: 11px;
  color: var(--mid-gray);
  font-weight: 500;
}

/* ═══ TICKER ═══ */
.ticker {
  background: var(--blue);
  padding: 14px 0;
  overflow: hidden;
  white-space: nowrap;
}
.ticker__track {
  display: inline-flex;
  animation: ticker-scroll 32s linear infinite;
}
.ticker__track:hover { animation-play-state: paused; }
@keyframes ticker-scroll {
  from { transform: translateX(0); }
  to { transform: translateX(-50%); }
}
.ticker__item {
  display: inline-flex;
  align-items: center;
  gap: 14px;
  padding: 0 2.5rem;
  font-family: var(--ff-head);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.9);
}
.ticker__sep { color: var(--amber); font-size: 14px; }

/* ═══ ABOUT ═══ */
.about { background: var(--white); padding: 7rem 0; }
.about__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5rem;
  align-items: center;
}
.about__visual { position: relative; }
.about__img-main-wrap { overflow: hidden; border-radius: 16px; }
.about__img-main {
  width: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
  border-radius: 16px;
  box-shadow: 0 24px 64px rgba(0,90,155,0.15);
  transition: transform 0.5s var(--ease-out);
  display: block;
}
.about__visual:hover .about__img-main { transform: scale(1.02); }
.about__badge {
  position: absolute;
  bottom: -1.5rem; right: -1.5rem;
  background: var(--blue);
  color: white;
  border-radius: 14px;
  padding: 1.5rem 1.75rem;
  text-align: center;
  box-shadow: 0 12px 40px rgba(0,90,155,0.35);
}
.about__badge-num {
  font-family: var(--ff-head);
  font-size: 2.4rem;
  font-weight: 800;
  color: var(--amber);
  line-height: 1;
}
.about__badge-label {
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.6);
  margin-top: 4px;
}
.about__frame {
  position: absolute;
  top: -12px; left: -12px;
  width: 56px; height: 56px;
  border-top: 3px solid var(--amber);
  border-left: 3px solid var(--amber);
  border-radius: 4px 0 0 0;
  z-index: 1;
}
.about__content h2 {
  font-family: var(--ff-head);
  font-size: clamp(1.9rem, 2.8vw, 2.6rem);
  font-weight: 800;
  line-height: 1.15;
  color: var(--blue-dark);
  margin-bottom: 1.5rem;
  letter-spacing: -0.02em;
}
.about__content h2 em { font-style: normal; color: var(--amber-dark); }
.about__content p {
  color: var(--dark-gray);
  font-size: 0.975rem;
  line-height: 1.9;
  margin-bottom: 1rem;
}
.about__pillars {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.85rem;
  margin: 1.75rem 0 2rem;
}
.about__pillar {
  background: var(--off-white);
  border: 1px solid var(--border);
  border-left: 3px solid var(--blue);
  border-radius: 8px;
  padding: 0.85rem 1rem;
  transition: background 0.2s, transform 0.2s;
}
.about__pillar:hover { background: rgba(0,90,155,0.04); transform: translateY(-2px); }
.about__pillar-title { font-weight: 700; font-size: 13px; color: var(--blue-dark); }
.about__pillar-sub { font-size: 11.5px; color: var(--mid-gray); margin-top: 2px; }
.btn-blue {
  background: var(--blue);
  color: var(--white);
  padding: 14px 32px;
  font-family: var(--ff-head);
  font-size: 14px;
  font-weight: 700;
  border-radius: 10px;
  display: inline-block;
  transition: background 0.2s, transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 4px 16px rgba(0,90,155,0.25);
}
.btn-blue:hover {
  background: var(--blue-dark);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,90,155,0.35);
}

/* ═══ SERVICES ═══ */
.services {
  background: linear-gradient(180deg, #001a32 0%, #003260 100%);
  padding: 7rem 0;
}
.services__header {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: end;
  margin-bottom: 4rem;
}
.services__header h2 {
  font-family: var(--ff-head);
  font-size: clamp(1.9rem, 2.8vw, 2.6rem);
  font-weight: 800;
  color: var(--white);
  line-height: 1.15;
  letter-spacing: -0.02em;
}
.services__header h2 em { font-style: normal; color: var(--amber); }
.services__header-right p {
  color: rgba(255,255,255,0.5);
  font-size: 0.95rem;
  line-height: 1.85;
  margin-bottom: 1.5rem;
}
.btn-ghost-light {
  color: rgba(255,255,255,0.7);
  font-size: 13.5px;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1px solid rgba(255,255,255,0.25);
  padding-bottom: 2px;
  transition: color 0.2s, border-color 0.2s;
}
.btn-ghost-light:hover { color: var(--amber); border-color: var(--amber); }
.btn-ghost-light svg { width: 16px; height: 16px; transition: transform 0.2s; }
.btn-ghost-light:hover svg { transform: translateX(4px); }
.services__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1px;
  background: rgba(255,255,255,0.06);
  border-radius: 16px;
  overflow: hidden;
}
.service-card {
  background: rgba(0, 40, 80, 0.5);
  padding: 2.5rem 2rem;
  position: relative;
  overflow: hidden;
  cursor: default;
  transition: background 0.3s;
}
.service-card::before {
  content: '';
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 3px;
  background: var(--amber);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.4s var(--ease-out);
}
.service-card:hover { background: rgba(0, 60, 110, 0.7); }
.service-card:hover::before { transform: scaleX(1); }
.service-card__icon {
  width: 52px; height: 52px;
  background: rgba(251,182,12,0.12);
  border: 1px solid rgba(251,182,12,0.2);
  border-radius: 12px;
  display: flex; align-items: center; justify-content: center;
  margin-bottom: 1.5rem;
  transition: background 0.3s, transform 0.3s var(--ease-spring);
}
.service-card:hover .service-card__icon {
  background: rgba(251,182,12,0.2);
  transform: scale(1.08) rotate(-3deg);
}
.service-card__icon svg { width: 24px; height: 24px; stroke: var(--amber); fill: none; stroke-width: 1.8; }
.service-card__num {
  font-family: var(--ff-head);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.2em;
  color: rgba(251,182,12,0.5);
  margin-bottom: 0.6rem;
  display: block;
}
.service-card__title {
  font-family: var(--ff-head);
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--white);
  margin-bottom: 0.85rem;
  line-height: 1.25;
}
.service-card__desc {
  font-size: 0.86rem;
  color: rgba(255,255,255,0.5);
  line-height: 1.8;
  margin-bottom: 1.5rem;
}
.service-card__link {
  font-size: 12px;
  font-family: var(--ff-head);
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--amber);
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: gap 0.2s;
}
.service-card:hover .service-card__link { gap: 12px; }

/* ═══ FLEET ═══ */
.fleet { background: var(--off-white); padding: 7rem 0; }
.fleet__inner {
  display: grid;
  grid-template-columns: 1fr 1.1fr;
  gap: 5rem;
  align-items: center;
}
.fleet__content h2 {
  font-family: var(--ff-head);
  font-size: clamp(1.9rem, 2.8vw, 2.6rem);
  font-weight: 800;
  color: var(--blue-dark);
  line-height: 1.15;
  margin-bottom: 1.25rem;
  letter-spacing: -0.02em;
}
.fleet__content h2 em { font-style: normal; color: var(--amber-dark); }
.fleet__content p {
  color: var(--dark-gray);
  line-height: 1.9;
  margin-bottom: 1.25rem;
  font-size: 0.975rem;
}
.fleet__specs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.6rem 1.5rem;
  margin: 1.75rem 0 2rem;
}
.fleet__spec {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  color: var(--dark-gray);
  font-weight: 500;
}
.fleet__spec::before {
  content: '';
  width: 7px; height: 7px;
  background: var(--blue);
  border-radius: 50%;
  flex-shrink: 0;
}
.fleet__visual { position: relative; }
.fleet__img-main-wrap { overflow: hidden; border-radius: 16px; }
.fleet__img-main {
  width: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
  border-radius: 16px;
  box-shadow: 0 24px 64px rgba(0,90,155,0.18);
  transition: transform 0.5s var(--ease-out);
  display: block;
}
.fleet__visual:hover .fleet__img-main { transform: scale(1.03); }
.fleet__stat-chip {
  position: absolute;
  top: 1.5rem; right: -1.5rem;
  background: var(--amber);
  border-radius: 12px;
  padding: 1rem 1.25rem;
  text-align: center;
  box-shadow: 0 8px 28px rgba(251,182,12,0.35);
}
.fleet__stat-chip-num {
  font-family: var(--ff-head);
  font-size: 2rem;
  font-weight: 800;
  color: var(--blue-dark);
  line-height: 1;
}
.fleet__stat-chip-label {
  font-size: 9.5px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: rgba(0,40,80,0.6);
  margin-top: 3px;
}

/* ═══ STATS BAND ═══ */
.stats-band {
  background: var(--blue);
  padding: 5rem 0;
  position: relative;
  overflow: hidden;
}
.stats-band::before {
  content: '';
  position: absolute;
  width: 500px; height: 500px;
  background: radial-gradient(circle, rgba(255,255,255,0.05) 0%, transparent 70%);
  top: -150px; right: -100px;
  pointer-events: none;
}
.stats-band__inner {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  text-align: center;
  position: relative;
  z-index: 1;
}
.stat-item {
  padding: 2rem;
  border-right: 1px solid rgba(255,255,255,0.15);
}
.stat-item:last-child { border-right: none; }
.stat-item__num {
  font-family: var(--ff-head);
  font-size: clamp(2.4rem, 3.5vw, 3.2rem);
  font-weight: 800;
  color: var(--white);
  line-height: 1;
  margin-bottom: 0.5rem;
}
.stat-item__num span { color: var(--amber); }
.stat-item__label {
  font-family: var(--ff-head);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.45);
}

/* ═══ WHY CHOOSE US ═══ */
.why { background: var(--white); padding: 7rem 0; }
.why__header {
  text-align: center;
  max-width: 680px;
  margin: 0 auto 4rem;
}
.why__header h2 {
  font-family: var(--ff-head);
  font-size: clamp(1.9rem, 2.8vw, 2.6rem);
  font-weight: 800;
  color: var(--blue-dark);
  line-height: 1.15;
  margin-bottom: 1rem;
  letter-spacing: -0.02em;
}
.why__header p { color: var(--dark-gray); font-size: 1rem; line-height: 1.8; }
.why__grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}
.why-card {
  background: var(--off-white);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 2.5rem;
  transition: transform 0.3s var(--ease-out), box-shadow 0.3s, border-color 0.3s;
  position: relative;
  overflow: hidden;
}
.why-card::after {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--blue), var(--amber));
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.4s var(--ease-out);
}
.why-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 20px 50px rgba(0,90,155,0.12);
  border-color: rgba(0,90,155,0.2);
}
.why-card:hover::after { transform: scaleX(1); }
.why-card__icon {
  width: 56px; height: 56px;
  background: rgba(0,90,155,0.08);
  border-radius: 14px;
  display: flex; align-items: center; justify-content: center;
  margin-bottom: 1.5rem;
  transition: background 0.3s, transform 0.3s var(--ease-spring);
}
.why-card:hover .why-card__icon {
  background: rgba(0,90,155,0.14);
  transform: scale(1.1) rotate(-5deg);
}
.why-card__icon svg { width: 26px; height: 26px; stroke: var(--blue); fill: none; stroke-width: 1.8; }
.why-card__title {
  font-family: var(--ff-head);
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--blue-dark);
  margin-bottom: 0.75rem;
}
.why-card__desc { font-size: 0.9rem; color: var(--dark-gray); line-height: 1.8; }

/* ═══ CSR ═══ */
.csr {
  background: linear-gradient(180deg, #001a32 0%, #003260 100%);
  padding: 7rem 0;
}
.csr__header {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: end;
  margin-bottom: 4rem;
}
.csr__header h2 {
  font-family: var(--ff-head);
  font-size: clamp(1.9rem, 2.8vw, 2.6rem);
  font-weight: 800;
  color: var(--white);
  line-height: 1.15;
  letter-spacing: -0.02em;
}
.csr__header h2 em { font-style: normal; color: var(--amber); }
.csr__header-right p { color: rgba(255,255,255,0.55); font-size: 0.95rem; line-height: 1.85; }
.csr__grid {
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  grid-template-rows: auto auto;
  gap: 1rem;
}
.csr-card {
  border-radius: 14px;
  overflow: hidden;
  position: relative;
  background: rgba(0,50,90,0.5);
  border: 1px solid rgba(255,255,255,0.07);
  min-height: 260px;
  transition: transform 0.3s var(--ease-out), box-shadow 0.3s;
}
.csr-card:hover {
  transform: scale(1.015);
  box-shadow: 0 20px 50px rgba(0,0,0,0.3);
}
.csr-card:first-child { grid-row: span 2; min-height: auto; }
.csr-card__img {
  width: 100%; height: 100%;
  object-fit: cover;
  display: block;
  filter: brightness(0.8);
  transition: filter 0.3s, transform 0.5s var(--ease-out);
}
.csr-card:hover .csr-card__img { filter: brightness(0.9); transform: scale(1.04); }
.csr-card__img-wrap { position: absolute; inset: 0; overflow: hidden; }
.csr-card__overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0,20,45,0.85) 0%, transparent 50%);
}
.csr-card__label {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  padding: 1.25rem 1.5rem;
  z-index: 2;
}
.csr-card__label-title {
  font-family: var(--ff-head);
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--white);
}
.csr-card__label-sub {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.08em;
  color: var(--amber-light);
  margin-top: 3px;
}

/* ═══ PARTNERS ═══ */
.partners {
  background: var(--off-white);
  padding: 5rem 0;
  border-top: 1px solid var(--border);
}
.partners__header { text-align: center; margin-bottom: 3rem; }
.partners__header h3 {
  font-family: var(--ff-head);
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--blue-dark);
}
.partners__logos {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}
.partner-pill {
  background: var(--white);
  border: 1.5px solid var(--border);
  border-radius: 100px;
  padding: 10px 24px;
  font-family: var(--ff-head);
  font-size: 13px;
  font-weight: 700;
  color: var(--mid-gray);
  transition: color 0.2s, border-color 0.2s, transform 0.2s, box-shadow 0.2s;
}
.partner-pill:hover {
  color: var(--blue);
  border-color: var(--blue);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0,90,155,0.12);
}

/* ═══ NEWS ═══ */
.news { background: var(--white); padding: 7rem 0; }
.news__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 3rem;
}
.news__header h2 {
  font-family: var(--ff-head);
  font-size: clamp(1.6rem, 2.4vw, 2.2rem);
  font-weight: 800;
  color: var(--blue-dark);
  letter-spacing: -0.02em;
}
.news__grid {
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 1.5rem;
}
.news-featured {
  background: var(--blue);
  border-radius: 16px;
  padding: 3rem;
  position: relative;
  overflow: hidden;
}
.news-featured::before {
  content: 'GPC';
  font-family: var(--ff-head);
  font-size: 14rem;
  font-weight: 800;
  color: rgba(255,255,255,0.04);
  position: absolute;
  right: -2rem; bottom: -2rem;
  line-height: 1;
  pointer-events: none;
}
.news-featured__tag {
  display: inline-block;
  background: var(--amber);
  color: var(--blue-dark);
  font-family: var(--ff-head);
  font-size: 9.5px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  padding: 5px 12px;
  border-radius: 100px;
  margin-bottom: 1.5rem;
}
.news-featured__headline {
  font-family: var(--ff-head);
  font-size: 1.45rem;
  font-weight: 700;
  color: var(--white);
  line-height: 1.35;
  margin-bottom: 1rem;
}
.news-featured__body {
  color: rgba(255,255,255,0.55);
  font-size: 0.9rem;
  line-height: 1.8;
  margin-bottom: 2rem;
}
.news-featured__meta {
  font-family: var(--ff-head);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--amber-light);
}
.news-sidebar { display: flex; flex-direction: column; gap: 1rem; }
.news-card {
  background: var(--off-white);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 1.75rem;
  flex: 1;
  transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
}
.news-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 30px rgba(0,90,155,0.1);
  border-color: rgba(0,90,155,0.2);
}
.news-card__tag {
  font-family: var(--ff-head);
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--blue);
  margin-bottom: 0.75rem;
}
.news-card__title {
  font-family: var(--ff-head);
  font-size: 0.975rem;
  font-weight: 700;
  color: var(--blue-dark);
  line-height: 1.35;
  margin-bottom: 0.5rem;
}
.news-card__excerpt { font-size: 13px; color: var(--dark-gray); line-height: 1.7; }

/* ═══ CTA ═══ */
.cta-section {
  background: var(--amber);
  padding: 6rem 0;
  position: relative;
  overflow: hidden;
}
.cta-section::before {
  content: '';
  position: absolute;
  width: 600px; height: 600px;
  background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 70%);
  top: -150px; right: -100px;
  pointer-events: none;
}
.cta-section__inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5rem;
  align-items: center;
  position: relative;
  z-index: 1;
}
.cta-section__left h2 {
  font-family: var(--ff-head);
  font-size: clamp(2rem, 3vw, 2.8rem);
  font-weight: 800;
  color: var(--blue-dark);
  line-height: 1.1;
  margin-bottom: 1rem;
  letter-spacing: -0.02em;
}
.cta-section__left p {
  color: rgba(0,40,80,0.72);
  font-size: 1rem;
  line-height: 1.8;
  margin-bottom: 2rem;
}
.btn-dark {
  background: var(--blue-dark);
  color: var(--white);
  padding: 14px 32px;
  font-family: var(--ff-head);
  font-size: 14px;
  font-weight: 700;
  border-radius: 10px;
  display: inline-block;
  transition: background 0.2s, transform 0.2s;
}
.btn-dark:hover { background: #001f3f; transform: translateY(-2px); }
.cta-section__form {
  background: var(--white);
  border-radius: 20px;
  padding: 2.5rem;
  box-shadow: 0 24px 64px rgba(0,64,112,0.2);
}
.form-row { margin-bottom: 1rem; }
.form-row label {
  display: block;
  font-size: 11.5px;
  font-family: var(--ff-head);
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--dark-gray);
  margin-bottom: 6px;
}
.form-row input,
.form-row select,
.form-row textarea {
  width: 100%;
  padding: 12px 16px;
  background: var(--off-white);
  border: 1.5px solid var(--border);
  border-radius: 8px;
  color: var(--text);
  font-family: var(--ff-body);
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
  appearance: none;
  -webkit-appearance: none;
}
.form-row input:focus,
.form-row select:focus,
.form-row textarea:focus {
  border-color: var(--blue);
  box-shadow: 0 0 0 3px rgba(0,90,155,0.1);
}
.form-row input::placeholder, .form-row textarea::placeholder { color: var(--mid-gray); }
.form-row-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.btn-form {
  width: 100%;
  background: var(--blue);
  color: var(--white);
  border: none;
  padding: 14px;
  font-family: var(--ff-head);
  font-size: 14px;
  font-weight: 700;
  border-radius: 10px;
  cursor: pointer;
  transition: background 0.2s, transform 0.2s;
  margin-top: 0.5rem;
}
.btn-form:hover { background: var(--blue-dark); transform: translateY(-1px); }

/* ═══ FOOTER ═══ */
.footer {
  background: #000e1c;
  padding: 5rem 0 2rem;
  border-top: 3px solid var(--amber);
}
.footer__top {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 3rem;
  margin-bottom: 4rem;
  padding-bottom: 4rem;
  border-bottom: 1px solid rgba(255,255,255,0.07);
}
.footer__brand-tagline {
  font-family: var(--ff-head);
  font-size: 1rem;
  font-style: italic;
  color: rgba(255,255,255,0.45);
  margin: 1rem 0;
  line-height: 1.5;
}
.footer__brand-desc {
  font-size: 0.875rem;
  color: rgba(255,255,255,0.35);
  line-height: 1.85;
  margin-bottom: 1.5rem;
}
.footer__social { display: flex; gap: 0.75rem; }
.footer__social a {
  width: 38px; height: 38px;
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  transition: border-color 0.2s, background 0.2s, transform 0.2s;
}
.footer__social a:hover {
  border-color: var(--amber);
  background: var(--amber);
  transform: translateY(-2px);
}
.footer__social a:hover svg { fill: var(--blue-dark); }
.footer__social svg { width: 16px; height: 16px; fill: rgba(255,255,255,0.6); transition: fill 0.2s; }
.footer__col-title {
  font-family: var(--ff-head);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--amber);
  margin-bottom: 1.25rem;
}
.footer__links li + li { margin-top: 0.65rem; }
.footer__links a {
  font-size: 13.5px;
  color: rgba(255,255,255,0.45);
  transition: color 0.2s;
  line-height: 1.5;
}
.footer__links a:hover { color: var(--white); }
.footer__contact-item {
  display: flex;
  gap: 10px;
  margin-bottom: 0.85rem;
  align-items: flex-start;
}
.footer__contact-icon { color: var(--amber); font-size: 14px; flex-shrink: 0; margin-top: 2px; }
.footer__contact-text { font-size: 12.5px; color: rgba(255,255,255,0.4); line-height: 1.65; }
.footer__contact-text a { color: rgba(255,255,255,0.4); transition: color 0.2s; }
.footer__contact-text a:hover { color: var(--amber); }
.footer__bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}
.footer__copy { font-size: 12px; color: rgba(255,255,255,0.25); font-family: var(--ff-head); }
.footer__legal { display: flex; gap: 1.5rem; }
.footer__legal a {
  font-size: 12px;
  color: rgba(255,255,255,0.25);
  font-family: var(--ff-head);
  font-weight: 600;
  letter-spacing: 0.05em;
  transition: color 0.2s;
}
.footer__legal a:hover { color: rgba(255,255,255,0.6); }

/* ═══ RESPONSIVE ═══ */
@media (max-width: 1024px) {
  .hero { grid-template-columns: 1fr; }
  .hero__right { display: none; }
  .hero__left { padding: 4rem var(--gutter); }
  .services__grid { grid-template-columns: 1fr 1fr; }
  .fleet__inner { grid-template-columns: 1fr; }
  .fleet__stat-chip { right: 1rem; }
  .fleet__visual { max-width: 600px; margin: 0 auto; }
  .stats-band__inner { grid-template-columns: 1fr 1fr; }
  .csr__header { grid-template-columns: 1fr; }
  .csr__grid { grid-template-columns: 1fr 1fr; }
  .csr-card:first-child { grid-column: span 2; grid-row: span 1; min-height: 320px; }
  .news__grid { grid-template-columns: 1fr; }
  .footer__top { grid-template-columns: 1fr 1fr; }
  .why__grid { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 768px) {
  .nav__links { display: none; }
  .nav__hamburger { display: flex; }
  .hero__headline { font-size: 2.4rem; }
  .hero__stats { grid-template-columns: 1fr 1fr; }
  .hero__stat:nth-child(3) { grid-column: span 2; border: none; padding-left: 0; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1); }
  .about__grid { grid-template-columns: 1fr; }
  .about__badge { bottom: auto; top: -1rem; right: 1rem; }
  .services__grid { grid-template-columns: 1fr; }
  .services__header { grid-template-columns: 1fr; }
  .csr__grid { grid-template-columns: 1fr; }
  .csr-card:first-child { grid-column: span 1; }
  .cta-section__inner { grid-template-columns: 1fr; gap: 3rem; }
  .footer__top { grid-template-columns: 1fr; gap: 2rem; }
  .footer__bottom { flex-direction: column; align-items: flex-start; }
  .form-row-2 { grid-template-columns: 1fr; }
  .news__header { flex-direction: column; align-items: flex-start; gap: 1rem; }
  .why__grid { grid-template-columns: 1fr; }
}
@media (max-width: 480px) {
  .about__pillars { grid-template-columns: 1fr; }
  .fleet__specs { grid-template-columns: 1fr; }
}

/* ── Scroll to top ── */
#scroll-top {
  position: fixed;
  bottom: 2rem; right: 2rem;
  width: 48px; height: 48px;
  background: var(--blue);
  color: white;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.3s, transform 0.3s, background 0.2s;
  z-index: 150;
  box-shadow: 0 6px 20px rgba(0,90,155,0.4);
}
#scroll-top.visible { opacity: 1; transform: translateY(0); }
#scroll-top:hover { background: var(--blue-dark); }
#scroll-top svg { width: 20px; height: 20px; stroke: white; fill: none; stroke-width: 2.5; }
</style>
</head>
<body>

<!-- NAV -->
<nav class="nav" id="main-nav" aria-label="Main navigation">
  <div class="nav__inner">
    <a href="/" class="nav__logo" aria-label="GPC Group Home">
      <div class="nav__logo-badge">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M5 12l5 5 9-9" stroke="#004070" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        </svg>
      </div>
      <div class="nav__logo-text">
        <strong>GPC Group</strong>
        <span>Always Good To Go</span>
      </div>
    </a>
    <ul class="nav__links" role="list">
      <li><a href="#about">About</a></li>
      <li><a href="#services">Services</a></li>
      <li><a href="#fleet">Fleet</a></li>
      <li><a href="#csr">Impact</a></li>
      <li><a href="#contact" class="nav__cta">Book a Truck</a></li>
    </ul>
    <button class="nav__hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>

<!-- Mobile Nav -->
<div class="nav__mobile" id="mobile-menu" role="dialog" aria-label="Mobile navigation">
  <a href="#about" class="mobile-link">About</a>
  <a href="#services" class="mobile-link">Services</a>
  <a href="#fleet" class="mobile-link">Fleet</a>
  <a href="#csr" class="mobile-link">Impact</a>
  <a href="#contact" class="nav__cta mobile-link">Book a Truck</a>
</div>

<!-- HERO -->
<section class="hero" aria-label="Hero">
  <div class="hero__left">
    <div class="hero__badge">
      <span class="hero__badge-dot"></span>
      <span class="hero__badge-text">Nigeria's Logistics Partner of Choice</span>
    </div>
    <h1 class="hero__headline">
      Delivering<br>
      <em>Excellence,</em><br>
      Driving Success.
    </h1>
    <p class="hero__sub">
      GPC Group is West Africa's foremost precision logistics company — connecting businesses to markets through safe, reliable transportation, warehousing, fleet intelligence, and seamless import-export services.
    </p>
    <div class="hero__actions">
      <a href="#contact" class="btn-primary">Get a Free Assessment</a>
      <a href="#services" class="btn-outline">
        Our Services
        <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" xmlns="http://www.w3.org/2000/svg"><path d="M3 8h10M9 4l4 4-4 4"/></svg>
      </a>
    </div>
    <div class="hero__stats">
      <div class="hero__stat">
        <div class="hero__stat-num" data-target="220">0<sup>+</sup></div>
        <div class="hero__stat-label">Active Trucks</div>
      </div>
      <div class="hero__stat">
        <div class="hero__stat-num" data-target="360">0<sup>+</sup></div>
        <div class="hero__stat-label">Jobs Created</div>
      </div>
      <div class="hero__stat">
        <div class="hero__stat-num" data-target="15">0<sup>+</sup></div>
        <div class="hero__stat-label">States Covered</div>
      </div>
    </div>
  </div>
  <div class="hero__right" aria-hidden="true">
    <div class="hero__img-wrap">
      <img src="images/about.png" alt="GPC Group branded MAN truck">
    </div>
    <div class="hero__float-badge">
      <div class="hero__float-badge-icon">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 00-4 0v2M8 11h.01M12 11h.01M16 11h.01"/>
        </svg>
      </div>
      <div class="hero__float-badge-text">
        <strong>&#x20A6;20bn</strong>
        <span>InfraCredit Guarantee</span>
      </div>
    </div>
  </div>
</section>

<!-- TICKER -->
<div class="ticker" aria-hidden="true">
  <div class="ticker__track">
    <span class="ticker__item">Transportation <span class="ticker__sep">&#9670;</span></span>
    <span class="ticker__item">Warehousing <span class="ticker__sep">&#9670;</span></span>
    <span class="ticker__item">Fleet Management <span class="ticker__sep">&#9670;</span></span>
    <span class="ticker__item">Import &amp; Export <span class="ticker__sep">&#9670;</span></span>
    <span class="ticker__item">Live GPS Tracking <span class="ticker__sep">&#9670;</span></span>
    <span class="ticker__item">On-Demand Logistics <span class="ticker__sep">&#9670;</span></span>
    <span class="ticker__item">Supply Chain Solutions <span class="ticker__sep">&#9670;</span></span>
    <span class="ticker__item">Nigeria &middot; West Africa <span class="ticker__sep">&#9670;</span></span>
    <span class="ticker__item">Transportation <span class="ticker__sep">&#9670;</span></span>
    <span class="ticker__item">Warehousing <span class="ticker__sep">&#9670;</span></span>
    <span class="ticker__item">Fleet Management <span class="ticker__sep">&#9670;</span></span>
    <span class="ticker__item">Import &amp; Export <span class="ticker__sep">&#9670;</span></span>
    <span class="ticker__item">Live GPS Tracking <span class="ticker__sep">&#9670;</span></span>
    <span class="ticker__item">On-Demand Logistics <span class="ticker__sep">&#9670;</span></span>
    <span class="ticker__item">Supply Chain Solutions <span class="ticker__sep">&#9670;</span></span>
    <span class="ticker__item">Nigeria &middot; West Africa <span class="ticker__sep">&#9670;</span></span>
  </div>
</div>

<!-- ABOUT -->
<section class="about" id="about" aria-labelledby="about-heading">
  <div class="container">
    <div class="about__grid">
      <div class="about__visual reveal-left">
        <div class="about__frame"></div>
        <div class="about__img-main-wrap">
          <img class="about__img-main" src="images/il2.jpeg" alt="GPC logistics operations at the warehouse" loading="lazy">
        </div>
        <div class="about__badge">
          <div class="about__badge-num">2012</div>
          <div class="about__badge-label">Est. Year</div>
        </div>
      </div>
      <div class="about__content reveal-right">
        <span class="label">Who We Are</span>
        <h2 id="about-heading">
          Built for the African road.<br>
          <em>Trusted</em> across the continent.
        </h2>
        <p>
          GPC Group Limited is Nigeria's leading precision truck logistics company, with over a decade of proven operations spanning transportation, warehousing, fleet management, and international trade facilitation.
        </p>
        <p>
          Founded with a singular vision — to make supply chains in Africa smarter, safer, and more reliable — we have grown from a regional hauler into a full-spectrum logistics powerhouse, backed by infrastructure financing from InfraCredit.
        </p>
        <div class="about__pillars">
          <div class="about__pillar">
            <div class="about__pillar-title">Safety First</div>
            <div class="about__pillar-sub">ISO-compliant HSE standards</div>
          </div>
          <div class="about__pillar">
            <div class="about__pillar-title">Digital-Driven</div>
            <div class="about__pillar-sub">Real-time fleet intelligence</div>
          </div>
          <div class="about__pillar">
            <div class="about__pillar-title">Pan-Nigeria Reach</div>
            <div class="about__pillar-sub">Lagos &amp; Ogun State depots</div>
          </div>
          <div class="about__pillar">
            <div class="about__pillar-title">Client-Centered</div>
            <div class="about__pillar-sub">Tailored logistics solutions</div>
          </div>
        </div>
        <a href="https://gpcgroupltd.com/about/" class="btn-blue">Read Our Full Story</a>
      </div>
    </div>
  </div>
</section>

<!-- SERVICES -->
<section class="services" id="services" aria-labelledby="services-heading">
  <div class="container">
    <div class="services__header">
      <div class="reveal">
        <span class="label label--light">What We Do</span>
        <h2 id="services-heading">One partner.<br><em>Every mile.</em></h2>
      </div>
      <div class="services__header-right reveal reveal-delay-2">
        <p>From the moment goods leave the factory gate to the moment they reach the end consumer, GPC is there — managing risk, ensuring compliance, and delivering certainty at every stage of your supply chain.</p>
        <a href="https://gpcgroupltd.com/services/" class="btn-ghost-light">
          View all services
          <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" xmlns="http://www.w3.org/2000/svg"><path d="M3 8h10M9 4l4 4-4 4"/></svg>
        </a>
      </div>
    </div>
    <div class="services__grid">
      <div class="service-card reveal reveal-delay-1">
        <div class="service-card__icon">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><rect x="1" y="8" width="15" height="10" rx="1.5"/><path d="M16 10.5l5 2.5v5h-5v-7.5z"/><circle cx="5.5" cy="18.5" r="1.8"/><circle cx="18.5" cy="18.5" r="1.8"/></svg>
        </div>
        <span class="service-card__num">01</span>
        <div class="service-card__title">Transportation</div>
        <p class="service-card__desc">Safe, top-notch haulage of liquid and solid products from source to end users. GPS-monitored fleet with certified drivers trained to the highest safety standards — delivering on time, every time.</p>
        <a href="https://gpcgroupltd.com/services/" class="service-card__link">Explore &rarr;</a>
      </div>
      <div class="service-card reveal reveal-delay-2">
        <div class="service-card__icon">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
        </div>
        <span class="service-card__num">02</span>
        <div class="service-card__title">Warehousing</div>
        <p class="service-card__desc">Massive, climate-suitable storage facilities strategically located across Nigeria. Inventory management, cross-docking, and order fulfilment tailored to the scale and cadence of your operations.</p>
        <a href="https://gpcgroupltd.com/services/" class="service-card__link">Explore &rarr;</a>
      </div>
      <div class="service-card reveal reveal-delay-3">
        <div class="service-card__icon">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
        </div>
        <span class="service-card__num">03</span>
        <div class="service-card__title">Fleet Management</div>
        <p class="service-card__desc">360-degree visibility of your fleet through our Lynk platform — route planning, driver behaviour monitoring, preventive maintenance scheduling, and live GPS data in one powerful dashboard.</p>
        <a href="https://gpcgroupltd.com/services/" class="service-card__link">Explore &rarr;</a>
      </div>
      <div class="service-card reveal reveal-delay-4">
        <div class="service-card__icon">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 010 20M12 2a15.3 15.3 0 000 20"/></svg>
        </div>
        <span class="service-card__num">04</span>
        <div class="service-card__title">Import &amp; Export</div>
        <p class="service-card__desc">End-to-end trade facilitation — ground clearance, customs documentation, port handling, and last-mile delivery. We remove the friction from cross-border trade so your goods arrive on schedule.</p>
        <a href="https://gpcgroupltd.com/services/" class="service-card__link">Explore &rarr;</a>
      </div>
    </div>
  </div>
</section>

<!-- FLEET -->
<section class="fleet" id="fleet" aria-labelledby="fleet-heading">
  <div class="container">
    <div class="fleet__inner">
      <div class="fleet__content reveal-left">
        <span class="label">Our Fleet</span>
        <h2 id="fleet-heading">220 trucks.<br><em>Zero compromise.</em></h2>
        <p>Our fleet is one of Nigeria's largest and most modern — purpose-built MAN and Scania rigs maintained to OEM standards, equipped with telematics hardware feeding live data into our Lynk operations platform.</p>
        <p>The &#x20A6;20 billion bond guarantee with InfraCredit enabled a dramatic fleet expansion, creating over 360 direct and indirect jobs and significantly increasing cargo capacity nationwide.</p>
        <div class="fleet__specs">
          <div class="fleet__spec">MAN Diesel Rigid &amp; Articulated Trucks</div>
          <div class="fleet__spec">Scania Long-Haul Rigs</div>
          <div class="fleet__spec">Live GPS Telematics on Every Unit</div>
          <div class="fleet__spec">Preventive Maintenance Scheduling</div>
          <div class="fleet__spec">Insured Cargo &amp; Third-Party Cover</div>
          <div class="fleet__spec">Certified Driver Training Programme</div>
        </div>
        <a href="#contact" class="btn-blue">Book a Truck Today</a>
      </div>
      <div class="fleet__visual reveal-right">
        <div class="fleet__stat-chip">
          <div class="fleet__stat-chip-num">220<sup style="font-size:1rem;">+</sup></div>
          <div class="fleet__stat-chip-label">Trucks</div>
        </div>
        <div class="fleet__img-main-wrap">
          <img class="fleet__img-main" src="images/il1.jpeg" alt="GPC logistics truck at loading dock" loading="lazy">
        </div>
      </div>
    </div>
  </div>
</section>

<!-- STATS BAND -->
<section class="stats-band" aria-label="Key statistics">
  <div class="container">
    <div class="stats-band__inner">
      <div class="stat-item reveal reveal-delay-1">
        <div class="stat-item__num" data-target="220">0<span>+</span></div>
        <div class="stat-item__label">Trucks in Fleet</div>
      </div>
      <div class="stat-item reveal reveal-delay-2">
        <div class="stat-item__num" data-prefix="&#x20A6;" data-target="20" data-suffix="bn">&#x20A6;0<span>bn</span></div>
        <div class="stat-item__label">InfraCredit Guarantee</div>
      </div>
      <div class="stat-item reveal reveal-delay-3">
        <div class="stat-item__num" data-target="360">0<span>+</span></div>
        <div class="stat-item__label">Jobs Created</div>
      </div>
      <div class="stat-item reveal reveal-delay-4">
        <div class="stat-item__num" data-target="10">0<span>+</span></div>
        <div class="stat-item__label">Years of Operations</div>
      </div>
    </div>
  </div>
</section>

<!-- WHY CHOOSE US -->
<section class="why" aria-labelledby="why-heading">
  <div class="container">
    <div class="why__header reveal">
      <span class="label" style="justify-content:center;">Why Choose GPC</span>
      <h2 id="why-heading">The Standard in Nigerian Logistics</h2>
      <p>Our commitment to safety, technology, and service excellence sets us apart from the rest of the industry.</p>
    </div>
    <div class="why__grid">
      <div class="why-card reveal reveal-delay-1">
        <div class="why-card__icon">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <div class="why-card__title">ISO-Compliant Safety</div>
        <div class="why-card__desc">Our HSE standards meet international benchmarks. Every driver is trained, every truck is inspected, and every load is insured — your cargo is always in safe hands.</div>
      </div>
      <div class="why-card reveal reveal-delay-2">
        <div class="why-card__icon">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/></svg>
        </div>
        <div class="why-card__title">Real-Time Intelligence</div>
        <div class="why-card__desc">Our Lynk platform gives you a live view of your shipment at all times — GPS tracking, ETA alerts, and driver behaviour reports — all in one seamless dashboard.</div>
      </div>
      <div class="why-card reveal reveal-delay-3">
        <div class="why-card__icon">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg>
        </div>
        <div class="why-card__title">Proven Partnerships</div>
        <div class="why-card__desc">We are the logistics partner of choice for Nestl&eacute;, PZ Cussons, Nigerian Breweries, Flour Mills, and dozens of Nigeria's leading FMCG and industrial brands.</div>
      </div>
    </div>
  </div>
</section>

<!-- CSR -->
<section class="csr" id="csr" aria-labelledby="csr-heading">
  <div class="container">
    <div class="csr__header">
      <div class="reveal">
        <span class="label label--light">Our Impact</span>
        <h2 id="csr-heading">Moving goods.<br><em>Moving communities.</em></h2>
      </div>
      <div class="csr__header-right reveal reveal-delay-2">
        <p>GPC Group believes a truly great logistics company doesn't just move cargo — it lifts the communities it operates in. Through job creation, skills training, and environmental stewardship, we are building a legacy beyond the road.</p>
      </div>
    </div>
    <div class="csr__grid">
      <div class="csr-card reveal">
        <div class="csr-card__img-wrap">
          <img class="csr-card__img" src="images/il2.jpeg" alt="GPC logistics operations community impact" loading="lazy">
        </div>
        <div class="csr-card__overlay"></div>
        <div class="csr-card__label">
          <div class="csr-card__label-title">Community Investment</div>
          <div class="csr-card__label-sub">Skills Training &amp; Job Creation</div>
        </div>
      </div>
      <div class="csr-card reveal reveal-delay-1">
        <div class="csr-card__img-wrap">
          <img class="csr-card__img" src="images/il1.jpeg" alt="GPC fleet environmental responsibility" loading="lazy">
        </div>
        <div class="csr-card__overlay"></div>
        <div class="csr-card__label">
          <div class="csr-card__label-title">Environmental Stewardship</div>
          <div class="csr-card__label-sub">Green fleet &amp; emission reduction</div>
        </div>
      </div>
      <div class="csr-card reveal reveal-delay-2" style="background:rgba(251,182,12,0.08);border:1px solid rgba(251,182,12,0.15);display:flex;align-items:center;justify-content:center;flex-direction:column;gap:1rem;padding:2rem;min-height:240px;">
        <div style="font-family:var(--ff-head);font-size:3.5rem;font-weight:800;color:var(--amber);line-height:1;">360<sup style="font-size:1.4rem;color:rgba(251,182,12,0.6);">+</sup></div>
        <div style="font-family:var(--ff-head);font-size:11px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:rgba(255,255,255,0.5);text-align:center;">Jobs Created Across<br>Nigeria</div>
      </div>
      <div class="csr-card reveal reveal-delay-3" style="background:rgba(0,90,155,0.15);border:1px solid rgba(0,90,155,0.25);display:flex;align-items:center;justify-content:center;flex-direction:column;gap:1rem;padding:2rem;min-height:240px;">
        <div style="font-family:var(--ff-head);font-size:3.5rem;font-weight:800;color:var(--white);line-height:1;">&#x20A6;20<sup style="font-size:1.4rem;color:var(--amber);">bn</sup></div>
        <div style="font-family:var(--ff-head);font-size:11px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;color:rgba(255,255,255,0.5);text-align:center;">InfraCredit Bond<br>Guarantee</div>
      </div>
    </div>
  </div>
</section>

<!-- PARTNERS -->
<section class="partners" aria-label="Partners and clients">
  <div class="container">
    <div class="partners__header reveal">
      <span class="label" style="justify-content:center;margin-bottom:0.75rem;">Trusted By</span>
      <h3>Our Partners &amp; Clients</h3>
    </div>
    <div class="partners__logos reveal reveal-delay-1">
      <div class="partner-pill">MAN Trucks</div>
      <div class="partner-pill">Nestl&eacute; Nigeria</div>
      <div class="partner-pill">PZ Cussons</div>
      <div class="partner-pill">Nigerian Breweries</div>
      <div class="partner-pill">Guinness Nigeria</div>
      <div class="partner-pill">Frigoglass</div>
      <div class="partner-pill">Flour Mills NG</div>
      <div class="partner-pill">InfraCredit</div>
    </div>
  </div>
</section>

<!-- NEWS -->
<section class="news" aria-labelledby="news-heading">
  <div class="container">
    <div class="news__header reveal">
      <div>
        <span class="label">Latest News</span>
        <h2 id="news-heading">GPC in the Headlines</h2>
      </div>
      <a href="https://gpcgroupltd.com/blog/" class="btn-ghost-light" style="color:var(--blue);border-color:rgba(0,90,155,0.3);">
        All News
        <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" xmlns="http://www.w3.org/2000/svg"><path d="M3 8h10M9 4l4 4-4 4"/></svg>
      </a>
    </div>
    <div class="news__grid">
      <div class="news-featured reveal">
        <div class="news-featured__tag">Press Release</div>
        <div class="news-featured__headline">InfraCredit and GPC Energy Sign &#x20A6;20bn Bond Guarantee to Expand Logistics Capacity Across Nigeria</div>
        <p class="news-featured__body">Infrastructure Credit Guarantee Company Limited (InfraCredit) has signed a landmark bond guarantee with GPC Energy and Logistics Limited to fund the acquisition of 220 new trucks — creating over 360 direct and indirect jobs for Nigerians and significantly boosting cargo capacity in Nigeria's logistics sector.</p>
        <div class="news-featured__meta">Bond Issuance &middot; InfraCredit Partnership &middot; 2023</div>
      </div>
      <div class="news-sidebar">
        <div class="news-card reveal reveal-delay-1">
          <div class="news-card__tag">Fleet Operations</div>
          <div class="news-card__title">GPC Deploys Real-Time Telematics Across Entire Fleet via Lynk Platform</div>
          <p class="news-card__excerpt">Our proprietary Lynk platform now covers all active trucks with live GPS, driver behaviour monitoring, and automated maintenance alerts.</p>
        </div>
        <div class="news-card reveal reveal-delay-2">
          <div class="news-card__tag">Partnerships</div>
          <div class="news-card__title">GPC Renews Long-Term Logistics Contracts with Major FMCG Brands</div>
          <p class="news-card__excerpt">Multi-year partnerships with Nestl&eacute;, PZ Cussons, and Nigerian Breweries renewed — cementing GPC's role as the logistics partner of choice.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CTA / CONTACT -->
<section class="cta-section" id="contact" aria-labelledby="cta-heading">
  <div class="container">
    <div class="cta-section__inner">
      <div class="cta-section__left reveal-left">
        <span class="label" style="color:rgba(0,40,80,0.7);">Free Consultation</span>
        <h2 id="cta-heading">Let's move your<br>business forward.</h2>
        <p>Book a free logistics assessment and let our experts design a supply chain solution built around your operations — from a single lane to a full national distribution network.</p>
        <a href="tel:+2349036324098" class="btn-dark">&#128222; Call: +234 903 632 4098</a>
        <div style="margin-top:1.5rem;display:flex;align-items:center;gap:1rem;">
          <img src="images/cc.jpeg" alt="GPC Customer Support Representative" style="width:52px;height:52px;border-radius:50%;object-fit:cover;border:3px solid var(--blue-dark);">
          <div>
            <div style="font-family:var(--ff-head);font-weight:700;font-size:13px;color:var(--blue-dark);">Speak to an Expert</div>
            <div style="font-size:12px;color:rgba(0,40,80,0.6);">Mon&ndash;Fri, 8am &ndash; 6pm WAT</div>
          </div>
        </div>
      </div>
      <div class="cta-section__form reveal-right">
        <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST" aria-label="Logistics assessment request">
          <div class="form-row-2">
            <div class="form-row">
              <label for="fname">Full Name</label>
              <input type="text" id="fname" name="name" placeholder="Ade Johnson" required>
            </div>
            <div class="form-row">
              <label for="company">Company</label>
              <input type="text" id="company" name="company" placeholder="Acme Nigeria Ltd">
            </div>
          </div>
          <div class="form-row">
            <label for="email">Email Address</label>
            <input type="email" id="email" name="email" placeholder="ade@company.com" required>
          </div>
          <div class="form-row">
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" name="phone" placeholder="+234 800 000 0000">
          </div>
          <div class="form-row">
            <label for="industry">Industry</label>
            <select id="industry" name="industry">
              <option value="">Select your industry</option>
              <option>Agriculture</option>
              <option>Construction / Real Estate</option>
              <option>Consumer Goods (FMCG)</option>
              <option>Healthcare / Pharma</option>
              <option>Industrial Goods</option>
              <option>Oil &amp; Gas</option>
              <option>Natural Resources</option>
              <option>ICT</option>
              <option>Utilities</option>
              <option>Other</option>
            </select>
          </div>
          <div class="form-row">
            <label for="message">Tell us about your logistics challenge</label>
            <textarea id="message" name="message" rows="3" placeholder="Describe your routes, volume, or logistics challenge..."></textarea>
          </div>
          <button type="submit" class="btn-form" id="submit-btn">Request Free Assessment &rarr;</button>
        </form>
      </div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer class="footer" aria-label="Site footer">
  <div class="container">
    <div class="footer__top">
      <div>
        <div class="nav__logo" style="margin-bottom:1rem;">
          <div class="nav__logo-badge">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M5 12l5 5 9-9" stroke="#004070" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>
          </div>
          <div class="nav__logo-text">
            <strong>GPC Group</strong>
            <span>Always Good To Go</span>
          </div>
        </div>
        <p class="footer__brand-tagline">"The Logistics Partner of Choice."</p>
        <p class="footer__brand-desc">GPC Group Limited is Nigeria's leading precision truck logistics and supply chain company — connecting businesses to markets across West Africa since 2012.</p>
        <div class="footer__social">
          <a href="https://www.facebook.com/gpcenergyandlogistics/" aria-label="Facebook" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg>
          </a>
          <a href="https://twitter.com/GPC_group" aria-label="Twitter" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z"/></svg>
          </a>
          <a href="https://www.instagram.com/gpc_energyandlogistics/" aria-label="Instagram" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z" fill="none" stroke="rgba(255,255,255,0.7)" stroke-width="1.5"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5" stroke="rgba(255,255,255,0.7)" stroke-width="1.5" stroke-linecap="round"/></svg>
          </a>
          <a href="https://www.linkedin.com/in/gpc-logistics-0375a41a5/" aria-label="LinkedIn" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg>
          </a>
        </div>
      </div>
      <div>
        <div class="footer__col-title">Quick Links</div>
        <ul class="footer__links">
          <li><a href="https://gpcgroupltd.com/about/">About GPC Group</a></li>
          <li><a href="https://gpcgroupltd.com/our-team/">Our Team</a></li>
          <li><a href="https://gpcgroupltd.com/services/">Our Services</a></li>
          <li><a href="https://gpcgroupltd.com/blog/">News &amp; Blog</a></li>
          <li><a href="https://gpcgroupltd.com/logistics-on-demand/">Book a Truck</a></li>
          <li><a href="https://gpcgroupltd.com/contact-us/">Contact Us</a></li>
        </ul>
      </div>
      <div>
        <div class="footer__col-title">Compliance</div>
        <ul class="footer__links">
          <li><a href="https://gpcgroupltd.com/wp-content/uploads/2022/12/QUALITY-POLICY-STATEMEN1.pdf">Quality Policy</a></li>
          <li><a href="https://gpcgroupltd.com/wp-content/uploads/2024/01/HSE-POLICY-FD.pdf">HSE Policy</a></li>
          <li><a href="#">Privacy Policy</a></li>
          <li><a href="#">Terms of Service</a></li>
        </ul>
      </div>
      <div>
        <div class="footer__col-title">Contact</div>
        <div class="footer__contact-item">
          <span class="footer__contact-icon">&#128205;</span>
          <span class="footer__contact-text">4B, Regina Coker Street, Off Alhaji Kofoworola Crescent, Ikeja, Lagos</span>
        </div>
        <div class="footer__contact-item">
          <span class="footer__contact-icon">&#127981;</span>
          <span class="footer__contact-text">Km 45, Lagos-Abeokuta Expressway, Beside Lafarge Cement, Ewekoro, Ogun State</span>
        </div>
        <div class="footer__contact-item">
          <span class="footer__contact-icon">&#128222;</span>
          <span class="footer__contact-text">
            <a href="tel:+2349036324098">+234 903 632 4098</a><br>
            <a href="tel:+2348024450950">+234 802 445 0950</a>
          </span>
        </div>
        <div class="footer__contact-item">
          <span class="footer__contact-icon">&#9993;&#65039;</span>
          <span class="footer__contact-text"><a href="mailto:info@gpcgroupltd.com">info@gpcgroupltd.com</a></span>
        </div>
      </div>
    </div>
    <div class="footer__bottom">
      <span class="footer__copy">&copy; 2026 GPC Group Limited. All rights reserved.</span>
      <div class="footer__legal">
        <a href="#">Privacy</a>
        <a href="#">Terms</a>
        <a href="https://gpcgroupltd.com/wp-content/uploads/2024/01/HSE-POLICY-FD.pdf">HSE Policy</a>
      </div>
    </div>
  </div>
</footer>

<button id="scroll-top" aria-label="Scroll to top">
  <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M18 15l-6-6-6 6"/></svg>
</button>

<script>
/* Nav scroll */
const nav = document.getElementById('main-nav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 60);
  document.getElementById('scroll-top').classList.toggle('visible', window.scrollY > 400);
});

/* Mobile menu */
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobile-menu');
hamburger.addEventListener('click', () => {
  const isOpen = mobileMenu.classList.toggle('open');
  hamburger.classList.toggle('active', isOpen);
  hamburger.setAttribute('aria-expanded', isOpen);
  document.body.style.overflow = isOpen ? 'hidden' : '';
});
document.querySelectorAll('.mobile-link').forEach(link => {
  link.addEventListener('click', () => {
    mobileMenu.classList.remove('open');
    hamburger.classList.remove('active');
    hamburger.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  });
});

/* Scroll-reveal */
const revealObs = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('visible'); revealObs.unobserve(e.target); }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -50px 0px' });
document.querySelectorAll('.reveal, .reveal-left, .reveal-right').forEach(el => revealObs.observe(el));

/* Counter animation */
function animateCounter(el) {
  const target = parseInt(el.getAttribute('data-target'));
  if (!target) return;
  const span = el.querySelector('span');
  const sup = el.querySelector('sup');
  const prefix = el.getAttribute('data-prefix') || '';
  let current = 0;
  const timer = setInterval(() => {
    current = Math.min(current + target / 60, target);
    const num = Math.round(current);
    if (span) {
      el.childNodes[0].textContent = prefix + num;
    } else if (sup) {
      el.childNodes[0].textContent = prefix + num;
    } else {
      el.textContent = prefix + num;
    }
    if (current >= target) clearInterval(timer);
  }, 1600 / 60);
}
const counterObs = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) { animateCounter(e.target); counterObs.unobserve(e.target); }
  });
}, { threshold: 0.5 });
document.querySelectorAll('[data-target]').forEach(el => counterObs.observe(el));

/* Scroll to top */
document.getElementById('scroll-top').addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

/* Reduced motion */
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  document.querySelectorAll('.ticker__track').forEach(t => t.style.animation = 'none');
  document.querySelectorAll('.reveal, .reveal-left, .reveal-right').forEach(el => {
    el.style.opacity = '1';
    el.style.transform = 'none';
  });
}

/* Form feedback */
const form = document.querySelector('form');
if (form) {
  form.addEventListener('submit', () => {
    const btn = document.getElementById('submit-btn');
    btn.textContent = 'Sending...';
    btn.style.opacity = '0.7';
  });
}
</script>
</body>
</html>"""

with open(r'c:\Users\Admin\Downloads\gpcgroup\gpcgroup.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('SUCCESS: gpcgroup.html written successfully')
print('File size:', len(html), 'characters')
