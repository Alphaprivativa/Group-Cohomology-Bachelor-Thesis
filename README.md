# (Co)homology of Groups and the Schur-Zassenhaus Theorem

**Bachelor thesis in Mathematics, Alma Mater Studiorum, University of Bologna, A.Y. 2023-2024.**

_(Co)omologia di gruppi ed il teorema di Schur-Zassenhaus_ - Tesi di Laurea in Teoria dei Gruppi.

| | |
|---|---|
| **Author** | Jacopo Elefante |
| **Supervisor** | Chiar.mo Prof. Luca Moci |
| **Co-supervisor** | Chiar.ma Dott. Martina Costa Cesari |
| **Degree** | Corso di Laurea in Matematica, Scuola di Scienze |
| **Academic year** | 2023-2024 |

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Web edition](https://img.shields.io/badge/read-online-blue.svg)](https://alphaprivativa.github.io/Group-Cohomology-Bachelor-Thesis/)

**[Read the web edition (English)](https://alphaprivativa.github.io/Group-Cohomology-Bachelor-Thesis/)**  ·  **[Download the PDF (Italiano)](Main_Thesis_PDF_IT/main.pdf)**

---

## About

The thesis develops the (co)homology of groups from the ground up and uses it to prove the
**Schur-Zassenhaus theorem**: every extension of a finite group $G$ by a normal subgroup $N$
with $\gcd(|N|, |G/N|) = 1$ splits, and all complements of $N$ are conjugate.

The route to that theorem is the classical one, told in full:

1. **Homological algebra.** Chain and cochain complexes, homology, chain homotopy, projective
   resolutions and their uniqueness up to homotopy, left derived functors, `Tor` and `Ext`.
2. **Group (co)homology.** Modules over a group algebra, fixed and cofixed points, the standard
   resolution and bar notation, explicit computation of $H^0$, $H^1$ and $H^2$, the cohomology of
   cyclic groups, restriction and transfer.
3. **Extensions.** Group extensions and their associated modules, splittings and complements,
   $H^1$ and the automorphisms of an extension, $H^2$ and Baer's theorem, the Baer sum and its
   identification with addition in $H^2(G, A)$.
4. **Applications.** The order of the group annihilates cohomology, Schur's theorem, and finally
   the Zassenhaus theorem in full generality.

An appendix collects the preliminary results used throughout: exact sequences, the snake lemma,
exact functors, projective, free and flat modules.

The original text (60 pages, PDF) is in **Italian**. The web edition is in **English**.

## The two editions

### PDF, Italian, the submitted thesis

[`Main_Thesis_PDF_IT/main.pdf`](Main_Thesis_PDF_IT/main.pdf) is the thesis exactly as written and
submitted in LaTeX. It is the citable version of record.

### Web, English, a hyperlinked rewrite

The web edition is not a page-by-page conversion of the PDF. The thesis was restructured into a
network of **atomic notes**, one per definition, theorem, lemma or proof, each of which links to
every notion it depends on. Instead of scrolling back to find where a term was defined, you click it.

What the web edition adds:

- **English translation** of the whole text.
- **Around 70 interlinked notes**, grouped under the same five chapters as the PDF.
- **An interactive graph view** of how the results depend on one another.
- **Full text search** across every note.
- **Backlinks**, so each result shows what uses it.
- **Rendered LaTeX** via MathJax, and commutative diagrams as SVG.

Entry point: [`main_HTML_ENG/000-home-coomologia-di-gruppi.html`](main_HTML_ENG/000-home-coomologia-di-gruppi.html),
which is the table of contents for the whole site.

## How the web edition was produced

The notes were written in [Obsidian](https://obsidian.md/) and exported to a static site with the
[**Webpage HTML Export**](https://github.com/KosmosisDire/obsidian-webpage-export) plugin, which
carries over the theme, the graph view, the search index and the backlinks. Commutative diagrams
were authored in LaTeX (`tikz-cd` / [quiver](https://q.uiver.app/)) and rendered to the SVG files
under `main_HTML_ENG/zz-allegati/quiver/`.

The translation from the Italian LaTeX source into English atomic notes was done **with the help of
AI**, then reviewed by the author. The mathematics, the proofs and the exposition are the author's
own; if the two editions ever disagree, the PDF is authoritative.

## Repository layout

```
.
├── index.html                 Redirects to the web edition
├── Main_Thesis_PDF_IT/
│   └── main.pdf               The thesis as submitted (Italian, 60 pp.)
├── main_HTML_ENG/             The web edition (English)
│   ├── 000-home-...html       Table of contents / home
│   ├── 001-homological-algebra.html
│   ├── 002-group-homology-and-cohomology.html
│   ├── 003-extensions.html
│   ├── 004-applications.html
│   ├── 005-appendix-preliminary-results.html
│   ├── <one file per definition, theorem or proof>
│   ├── site-lib/              Styles, scripts, fonts, search index, graph engine
│   └── zz-allegati/quiver/    Commutative diagrams as SVG
├── .github/workflows/static.yml   Deploys the site to GitHub Pages on push
├── tools/
│   └── mark-unresolved-links.py   Post-export tidy up, see below
├── LICENSE                    CC BY 4.0
└── .nojekyll                  Tells GitHub Pages to serve the files as they are
```

### Re-exporting

The thesis notes live inside a much larger Obsidian vault, and they link out to
notes that are not part of the thesis and therefore are not exported. Left alone, those
anchors are ordinary links that return 404. After every export, run

```bash
python tools/mark-unresolved-links.py main_HTML_ENG
```

which rewrites exactly those anchors into Obsidian's own *unresolved link* form: the text
and the tooltip stay, but the link is inert and rendered dimmed by the theme. Links whose
target does exist are left untouched, so the script is safe to re-run.

## Reading it locally

Opening `index.html` straight from the filesystem works for the text, but browsers block the
`fetch` calls the search index and the graph view rely on. To get the full site, serve the folder
over HTTP:

```bash
python -m http.server 8000
```

then open <http://localhost:8000>.

## Publishing on GitHub Pages

The site is plain static files, so there is no build step. Deployment is handled by
[`.github/workflows/static.yml`](.github/workflows/static.yml), which uploads the whole
repository and publishes it on every push to `main`.

One-time setup: **Settings → Pages → Build and deployment**, source **GitHub Actions**.
After that, every push redeploys, and the workflow can also be triggered by hand from the
**Actions** tab.

The site is live at
<https://alphaprivativa.github.io/Group-Cohomology-Bachelor-Thesis/>, where the root
`index.html` sends visitors into the web edition.

`.nojekyll` is committed so that `site-lib/` is copied verbatim rather than run through Jekyll.

## Citation

```bibtex
@thesis{elefante2024coomologia,
  author      = {Elefante, Jacopo},
  title       = {(Co)omologia di gruppi ed il teorema di Schur-Zassenhaus},
  type        = {Tesi di Laurea Triennale in Matematica},
  institution = {Alma Mater Studiorum, Universit\`a di Bologna},
  year        = {2024},
  language    = {italian},
  url         = {https://alphaprivativa.github.io/Group-Cohomology-Bachelor-Thesis/}
}
```

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
You are free to share and adapt it, including commercially, as long as you give appropriate credit.

See [LICENSE](LICENSE) for the full text.

## Acknowledgements

Thanks to Prof. Luca Moci and Dott. Martina Costa Cesari for their supervision, and to the
[Webpage HTML Export](https://github.com/KosmosisDire/obsidian-webpage-export) plugin, which made
the web edition possible.
