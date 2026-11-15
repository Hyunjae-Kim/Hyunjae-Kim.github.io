# Hyunjae Kim — academic homepage

Static HTML/CSS website published through GitHub Pages.

- `index.html`: concise introduction and three expandable research directions
- `publications.html`: publications grouped by status and year; titles link to verified external sources when available
- `assets/Hyunjae-Kim-CV.pdf`: direct destination for the CV menu
- `cv.html` and `publications/*.html`: redirects that preserve old bookmarks

Edit publication metadata and URLs in `assets/publications.json`, and edit the introduction, research directions, and shared navigation in `build_site.py`. Run `python3 build_site.py` to regenerate the HTML pages. The site requires no browser JavaScript or external fonts.

Preview with `python3 -m http.server 8000`. GitHub Pages serves the root of `main`.
