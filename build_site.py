"""Render the academic homepage from assets/publications.json (no dependencies)."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent
PAPERS = json.loads((ROOT / 'assets/publications.json').read_text())
BY_SLUG = {p['slug']: p for p in PAPERS}
CV = 'assets/Hyunjae-Kim-CV.pdf'

def authors(value):
    return escape(value).replace('H Kim', '<strong>H Kim</strong>')

def paper_title(p, selected=False):
    url = p.get('url')
    if url:
        return f'<a href="{escape(url, quote=True)}">{escape(p["title"])}</a>'
    if selected:
        return f'<a href="publications.html#{p["slug"]}">{escape(p["title"])}</a>'
    return escape(p['title'])

def paper(p, selected=False):
    tag = 'li' if selected else 'article'
    ident = '' if selected else f' id="{p["slug"]}"'
    title_tag = 'p' if selected else 'h3'
    return f'''<{tag} class="paper-entry"{ident}>
  <p class="paper-authors">{authors(p['authors'])}</p>
  <{title_tag} class="paper-title">{paper_title(p, selected)}</{title_tag}>
  <p class="paper-venue">{escape(p['venue'])}</p>
</{tag}>'''

def shell(title, body, current='About'):
    nav = "".join('<a{} href="{}">{}</a>'.format(' aria-current="page"' if name == current else "", url, name) for name, url in [("About", "index.html"), ("Publications", "publications.html"), ("CV", CV)])
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)} | Hyunjae Kim</title>
  <meta name="description" content="Hyunjae Kim studies auditory perception and music through NeuroAI, computational modeling, and EEG at KAIST.">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header><div class="header-inner"><a class="brand" href="index.html">Hyunjae Kim</a><nav aria-label="Main navigation">{nav}</nav></div></header>
<div class="layout">
  <aside class="profile">
    <div class="monogram" aria-hidden="true">HK<span></span></div>
    <h2>Hyunjae Kim</h2>
    <p class="role">Ph.D. Student</p>
    <p>Music and Brain Lab<br>Graduate School of Culture Technology<br>KAIST</p>
    <p class="location">Daejeon, Republic of Korea</p>
    <div class="profile-links">
      <a href="mailto:present@kaist.ac.kr">Email <span aria-hidden="true">↗</span></a>
      <a href="https://www.linkedin.com/in/hyunjae-kim-b79b54151/">LinkedIn <span aria-hidden="true">↗</span></a>
      <a href="https://github.com/Hyunjae-Kim">GitHub <span aria-hidden="true">↗</span></a>
    </div>
  </aside>
  <main id="main">{body}</main>
</div>
<footer><div>© 2026 Hyunjae Kim<span>Auditory perception · NeuroAI · Music</span></div></footer>
</body>
</html>
'''

DIRECTIONS = [
    ('Computational Hearing', 'How do biological constraints shape auditory representations?', 'I build deep auditory models to study how cochlear processing and spectrotemporal constraints shape sound recognition and cortical selectivity.', ['music-selectivity', 'biomimetic-membrane']),
    ('Music & NeuroAI', 'What can music models reveal about human perception?', 'I compare representations in music foundation models with human brain responses and perception, focusing on auditory cortex alignment and musical emotion.', ['brain-alignment', 'musical-emotion']),
    ('EEG & Listening Experience', 'How does the brain respond to music in everyday listening?', 'I use EEG and behavioral experiments with naturalistic music to study immersive spatial audio, music preference, and familiarity.', ['spatial-audio', 'music-preference']),
]

intro = '''<h1 class="about-title">Auditory perception and music<br>through the lens of NeuroAI.</h1>
<p class="intro">I am a Ph.D. student in the Music and Brain Lab at KAIST, advised by Kyung Myun Lee. I study how the brain represents sound and music by combining deep auditory models, EEG, and behavioral experiments. My work focuses on how biological constraints shape auditory representations and how these representations relate to human perception and listening experience.</p>
<section class="research-interests" aria-labelledby="interests-heading">
  <div class="section-heading"><h2 id="interests-heading">Research interests</h2></div>
'''
for n, (title, question, description, selected) in enumerate(DIRECTIONS, 1):
    intro += f'''<details class="research-direction">
  <summary><span class="direction-number">0{n}</span><span class="direction-heading"><span class="direction-title">{escape(title)}</span><span class="direction-question">{escape(question)}</span></span><span class="toggle" aria-hidden="true"></span></summary>
  <div class="direction-content"><p>{escape(description)}</p><h3 class="selected-label">Selected work</h3><ul class="selected-papers">{''.join(paper(BY_SLUG[s], True) for s in selected)}</ul></div>
</details>'''
intro += '</section><a class="all-publications" href="publications.html">All publications <span aria-hidden="true">→</span></a>'
(ROOT/'index.html').write_text(shell('About', intro))

body = '<h1>Publications</h1><p class="page-intro">Papers and ongoing work.</p>'
for label, papers in [('In progress', [p for p in PAPERS if p['year'] is None])] + [(str(y), [p for p in PAPERS if p['year'] == y]) for y in sorted({p['year'] for p in PAPERS if p['year']}, reverse=True)]:
    body += f'<section class="publication-group" aria-labelledby="group-{label.replace(" ", "-")}"><h2 id="group-{label.replace(" ", "-")}">{label}</h2><div class="paper-list">'+''.join(paper(p) for p in papers)+'</div></section>'
(ROOT/'publications.html').write_text(shell('Publications', body, 'Publications'))

def redirect(target, title):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{escape(title)} | Hyunjae Kim</title><meta http-equiv="refresh" content="0; url={escape(target, quote=True)}"><link rel="canonical" href="{escape(target, quote=True)}"></head><body><p><a href="{escape(target, quote=True)}">{escape(title)} →</a></p></body></html>\n'''
(ROOT/'cv.html').write_text(redirect(CV, 'Curriculum vitae'))
for p in PAPERS:
    (ROOT/'publications'/f'{p["slug"]}.html').write_text(redirect(f'../publications.html#{p["slug"]}', 'Publications'))
(ROOT/'404.html').write_text(shell('Page not found', '<h1>Page not found.</h1><p><a href="/">Return to the homepage →</a></p>').replace('<meta charset="utf-8">','<meta charset="utf-8"><base href="/">'))
