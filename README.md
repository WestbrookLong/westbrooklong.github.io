# Jianyu Long · Westbrook

Personal projects and research portfolio. Static HTML, CSS, and a small JavaScript project filter; no framework or package installation required.

## Publishing pipeline

This repository is named `westbrooklong.github.io`, so GitHub Pages serves it at **https://westbrooklong.github.io/**.

The pipeline is:

```text
Edit content.json → run python3 build.py → commit and push → GitHub Pages publishes
```

Pages is configured to **Deploy from a branch**, using **main** and **/ (root)**. GitHub runs its Pages deployment automatically after a push. The `.nojekyll` file tells Pages to serve the static files directly.

To configure or inspect hosting, open the repository's **Settings → Pages**. To check deployment progress, open **Actions**, then the **pages build and deployment** run. Publishing can take several minutes.

## Make changes

1. Edit `content.json` to change your introduction, projects, research, education, or experience.
2. Run `python3 build.py` in this directory. This regenerates `index.html`.
3. Preview with `python3 -m http.server 4173`, then visit http://localhost:4173.
4. Commit `content.json` and the regenerated `index.html`, along with any other changes, and push to `main`.

You can also edit `index.html` directly in GitHub and commit the change for a quick update. The next run of `build.py` will replace it with the content from `content.json`, so keep both in sync.

For visual changes, edit `styles.css`. The project filter is in `script.js`. All project content remains visible with JavaScript disabled.

## Files

| File | Purpose |
| --- | --- |
| `content.json` | Editable profile and project content |
| `build.py` | Standard-library-only page generator |
| `index.html` | Generated page served by GitHub Pages |
| `styles.css` | Responsive layout and visual design |
| `script.js` | Accessible project filters and footer year |
| `favicon.svg` | Site icon |
| `.nojekyll` | Static-file publishing |

## Content notes

The initial content was adapted from the supplied CV. The OneTrans repository link uses the verified `OneTrans_Pytorch` repository name. University study at SUSTech is described without claiming a completed degree. No downloadable CV is included; the site uses the professional email address for contact.

## Official GitHub documentation

- [GitHub Pages quickstart](https://docs.github.com/en/pages/quickstart)
- [Configure a publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
