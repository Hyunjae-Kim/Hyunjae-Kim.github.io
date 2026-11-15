"""Render the academic homepage from assets/publications.json (no dependencies)."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent
PAPERS = json.loads((ROOT / 'assets/publications.json').read_text())
BY_SLUG = {p['slug']: p for p in PAPERS}
CV = 'assets/Hyunjae-Kim-CV.pdf'

def authors(value):
    initials = {'H': 'H.', 'S-B': 'S.-B.', 'KM': 'K. M.', 'R': 'R.', 'S': 'S.', 'J': 'J.', 'T': 'T.', 'M': 'M.', 'EJ': 'E. J.', 'WS': 'W. S.', 'AN': 'A. N.', 'KH': 'K.-H.'}
    names = []
    for name in value.split(', '):
        first, last = name.split(' ', 1)
        formatted = escape(initials.get(first, first) + ' ' + last)
        names.append('<strong>' + formatted + '</strong>' if name == 'H Kim' else formatted)
    return ', '.join(names)

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
  <{title_tag} class="paper-title">{paper_title(p, selected)}</{title_tag}>
  <p class="paper-authors">{authors(p['authors'])}</p>
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
      <a href="mailto:present@kaist.ac.kr"><svg class="social-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/></svg>Email<span class="link-arrow" aria-hidden="true">↗</span></a>
      <a href="https://www.linkedin.com/in/hyunjae-kim-b79b54151/"><svg class="social-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 10v7m4 0v-7m0 3a3 3 0 0 1 6 0v4"/><circle cx="7" cy="7" r=".7" fill="currentColor" stroke="none"/></svg>LinkedIn<span class="link-arrow" aria-hidden="true">↗</span></a>
      <a href="https://github.com/Hyunjae-Kim"><svg class="social-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path fill="currentColor" stroke="none" d="M12 .8a11.4 11.4 0 0 0-3.6 22.2c.6.1.8-.2.8-.5v-2.1c-3.3.7-4-1.4-4-1.4-.5-1.3-1.3-1.6-1.3-1.6-1.1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.7 1.3 3.4 1 .1-.8.4-1.3.7-1.6-2.6-.3-5.4-1.3-5.4-5.7 0-1.3.4-2.3 1.2-3.1-.1-.3-.5-1.5.1-3.1 0 0 1-.3 3.2 1.2a11 11 0 0 1 5.8 0c2.2-1.5 3.2-1.2 3.2-1.2.6 1.6.2 2.8.1 3.1.8.8 1.2 1.8 1.2 3.1 0 4.4-2.8 5.4-5.4 5.7.4.4.8 1.1.8 2.2v3.1c0 .3.2.6.8.5A11.4 11.4 0 0 0 12 .8Z"/></svg>GitHub<span class="link-arrow" aria-hidden="true">↗</span></a>
      <a href="https://scholar.google.com/citations?user=HlWMOPAAAAAJ&amp;hl=en&amp;oi=ao"><svg class="social-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="m2 8 10-5 10 5-10 5-10-5Z"/><path d="M6 10v5c3 3 9 3 12 0v-5M22 8v8"/><path d="M8 20h8"/></svg>Google Scholar<span class="link-arrow" aria-hidden="true">↗</span></a>
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
