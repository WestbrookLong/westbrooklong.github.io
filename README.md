# Jianyu Long (Westbrook) — Academic Pages

Personal academic website at **https://westbrooklong.github.io/**, based on the [Academic Pages template](https://academicpages.github.io/) (upstream commit `8c57e1ae5da379512eb11165257fba02664b8531`). The original template license is retained in `LICENSE`.

## Update the website

You can edit these files directly on GitHub. Commit your changes to `main`; GitHub Actions builds Jekyll and deploys the result automatically. No manual HTML generation is needed.

| Content | File |
| --- | --- |
| Name, sidebar, email, GitHub, site URL | `_config.yml` |
| Top navigation | `_data/navigation.yml` |
| Homepage / About | `_pages/about.md` |
| Projects index | `_pages/portfolio.html` |
| Research index | `_pages/research.html` |
| Individual project and research pages | `_portfolio/*.md` |
| CV | `_pages/cv.md` |

Project entries use `kind: project`; research entries use `kind: research`. The `order` field controls ordering within each list. Template examples, placeholder publications, and unused navigation items are omitted.

## Deployment

Repository Settings → Pages → Source: **GitHub Actions**.

The workflow in `.github/workflows/jekyll.yml` installs Ruby and Node, builds the template JavaScript, runs `bundle exec jekyll build`, and deploys `_site` to GitHub Pages. Check the repository's Actions tab for build results.

The old static-page implementation remains recoverable in Git history at commit `7b3e0db985ea2ce91b38649df213ee4197120ec5`.

## Local preview

Requires Ruby 3.3+, Bundler, and Node.js:

```sh
bundle install
npm install
npm run build:js
bundle exec jekyll serve --host 127.0.0.1
```

Open http://127.0.0.1:4000. Configuration changes require restarting Jekyll.

## Attribution

[Academic Pages](https://github.com/academicpages/academicpages.github.io), derived from [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/), under the MIT License.
