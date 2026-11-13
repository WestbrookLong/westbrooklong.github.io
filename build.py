"""Build a portable static portfolio using only the Python standard library."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'content.json').read_text())
e = lambda value: escape(str(value), quote=True)

def link(url, label, css='text-link'):
    if not url:
        return ''
    if not url.startswith(('https://', 'mailto:')):
        raise ValueError(f'Unsupported link: {url}')
    return f'<a class="{css}" href="{e(url)}">{e(label)} <span aria-hidden="true">↗</span></a>'

def visual(kind):
    if kind == 'memory':
        return '<div class="memory-visual"><span>conversation</span><i>↓</i><span class="memory-core">evidence → memory</span><i>↓</i><span>context that carries forward</span></div>'
    if kind == 'voice':
        bars = ''.join(f'<i style="--h:{h}px"></i>' for h in [12,22,35,18,46,60,32,48,24,14,38,56,28,45,19,30,51,65,34,20,42,27,13,34,49,23,40,16])
        return f'<div class="voice-visual"><div class="wave">{bars}</div><div class="transcript"><span>01:24</span> A conversation becomes a clearer picture.</div></div>'
    if kind == 'flow':
        return '<div class="flow-visual"><span class="phone">Aa</span><span class="stream">· · · →</span><span class="cursor-box">Hello, world<span class="cursor">|</span></span></div>'
    return '<div class="plan-visual"><span>01 &nbsp; Retrieve context</span><span>02 &nbsp; Build the plan</span><span class="plan-final">03 &nbsp; Evaluate & refine <b>✓</b></span></div>'

projects = ''.join(f'''<article class="project" data-category="{e(p['category'])}">
<div class="project-visual {e(p['visual'])}" aria-hidden="true">{visual(p['visual'])}</div>
<div class="project-body"><div class="eyebrow project-meta"><span>{e(p['category'])}</span><span>{e(p['period'])}</span></div>
<h3>{e(p['title'])}</h3><p class="subtitle">{e(p['subtitle'])}</p><p>{e(p['description'])}</p>
<p class="project-detail">{e(p['detail'])}</p><div class="project-bottom"><div class="tags">{''.join(f'<span>{e(t)}</span>' for t in p['tags'])}</div>{link(p['url'], p['linkLabel'])}</div></div></article>''' for p in data['projects'])

research = ''.join(f'''<article class="research-item"><span class="research-number">0{i+1}</span><div><p class="eyebrow">{e(r['label'])}</p><h3>{e(r['title'])}</h3><p>{e(r['description'])}</p><p class="research-tags">{e(r['tags'])}</p>{link(r['url'], r['linkLabel'])}</div></article>''' for i,r in enumerate(data['research']))

education = ''.join(f'<div class="education-item"><span class="eyebrow">{e(s["period"])}</span><h4>{e(s["school"])}</h4><p>{e(s["detail"])}</p></div>' for s in data['education'])
skills = ''.join(f'<div><h4>{e(s["title"])}</h4><p>{e(s["items"])}</p></div>' for s in data['skills'])
xp = data['experience']
headline = '<br>'.join(f'<em>{e(line)}</em>' if i == len(data['headline'].split('\n')) - 1 else e(line) for i, line in enumerate(data['headline'].split('\n')))

html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(data['name'])} (Westbrook) — Projects & Research</title>
<meta name="description" content="Jianyu Long (Westbrook). Data Science and Computer Science at UW–Madison. Projects in AI agents, voice interfaces, and machine learning.">
<meta name="theme-color" content="#214b3b"><meta property="og:title" content="Jianyu Long — Westbrook"><meta property="og:description" content="Projects, research, and building things that work."><meta property="og:type" content="website">
<link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"><script src="script.js" defer></script></head>
<body><a class="skip-link" href="#main">Skip to content</a>
<header class="site-header wrap"><a class="brand" href="#" aria-label="Jianyu Long, home"><span class="brand-mark">jl.</span><span>WESTBROOK<span class="brand-caption">Jianyu Long</span></span></a><nav aria-label="Main navigation"><a href="#projects">Projects</a><a href="#research">Research</a><a href="#about">About</a>{link('mailto:'+data['email'],'Say hello','nav-contact')}</nav></header>
<main id="main"><section class="hero wrap" aria-labelledby="hero-title"><div class="hero-main"><p class="eyebrow"><span class="small-dot"></span> PERSONAL PROJECTS & RESEARCH</p><h1 id="hero-title">{headline}</h1><p class="intro">{e(data['intro'])}</p><div class="hero-actions"><a class="button" href="#projects">Explore my work <span aria-hidden="true">↓</span></a>{link(data['github'],'GitHub')}</div></div>
<aside class="field-note" aria-label="Areas of exploration"><div class="note-top"><span>FIELD NOTES</span><span>JL / 01</span></div><div class="orbit" aria-hidden="true"><div class="orbit-line line-one"></div><div class="orbit-line line-two"></div><div class="orbit-line line-three"></div><span class="orbit-center">curiosity</span><span class="orbit-label label-one">agents</span><span class="orbit-label label-two">voice</span><span class="orbit-label label-three">learning</span><i class="orbit-dot dot-one"></i><i class="orbit-dot dot-two"></i></div><p>From a research idea<br>to a useful, working system.</p><div class="note-bottom"><span>BUILD · EVALUATE · ITERATE</span><span>↗</span></div></aside></section>
<div class="focus-strip wrap"><span class="eyebrow">AREAS OF EXPLORATION</span><p>Persistent memory <span>/</span> Voice interfaces <span>/</span> Applied machine learning</p></div>
<section id="projects" class="section wrap" aria-labelledby="projects-heading"><div class="section-heading"><div><p class="eyebrow">01 / SELECTED WORK</p><h2 id="projects-heading">Built to be used.</h2></div><p>From desktop companions to voice systems.<br>A selection of projects from idea to implementation.</p></div><div class="filters" role="group" aria-label="Filter projects" hidden><button type="button" class="active" data-filter="All" aria-pressed="true">All projects <span>04</span></button><button type="button" data-filter="Agents" aria-pressed="false">Agents</button><button type="button" data-filter="Voice" aria-pressed="false">Voice & interfaces</button></div><p class="sr-only" id="filter-status" role="status"></p><div class="projects-grid">{projects}</div></section>
<section id="research" class="research-section"><div class="wrap section"><div class="section-heading"><div><p class="eyebrow">02 / RESEARCH & IMPLEMENTATIONS</p><h2 id="research-heading">Understand it.<br>Then build it.</h2></div><p>Exploring model architectures, training pipelines,<br> and mathematical reasoning through code.</p></div><div class="research-list">{research}</div></div></section>
<section id="about" class="section wrap" aria-labelledby="about-heading"><div class="about-grid"><div><p class="eyebrow">03 / A LITTLE BACKGROUND</p><h2 id="about-heading">Jianyu Long.<br><em>Call me Westbrook.</em></h2><p class="about-copy">{e(data['about'])}</p>{link(data['github'],'Find me on GitHub')}<div class="education"><h3>Education</h3>{education}</div></div><div class="experience"><p class="eyebrow">EXPERIENCE</p><p class="experience-date">{e(xp['period'])}</p><h3>{e(xp['role'])}</h3><p class="company">{e(xp['company'])}</p><p>{e(xp['description'])}</p><span class="award">↗ {e(xp['recognition'])}</span><div class="skills">{skills}</div></div></div></section>
<section class="contact-section"><div class="wrap contact-inner"><div><p class="eyebrow">CONTINUE THE CONVERSATION</p><h2>Something on your mind?<br><em>Let’s talk.</em></h2></div><div>{link('mailto:'+data['email'],data['email'],'contact-link')}<p>Projects, research, and interesting ideas.</p></div></div></section></main>
<footer class="wrap"><span>© <span id="year">2026</span> {e(data['name'])} <span class="footer-nickname">/ Westbrook</span></span><div>{link(data['github'],'GitHub')}<a href="#main">Back to top ↑</a></div></footer>
</body></html>'''
(ROOT / 'index.html').write_text(html, encoding='utf-8')
print('Built index.html from content.json')
