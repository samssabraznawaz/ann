# Maintainer guide — SaNaSoft-ANN

SaNaSoft-ANN has its own repository, https://github.com/samssabraznawaz/ann, published with GitHub Pages at
**https://samssabraznawaz.github.io/ann/**. SaNaSoft fsQCA lives separately at https://github.com/samssabraznawaz/fsqca.

## Everyday changes
Edit `src/`, then from the repository root run `node build.js` and `npm test`; commit `src/` **and** `index.html`.
The *ANN tests* workflow fails if `index.html` was not rebuilt.

## Version and citation
Change the version in `src/app-core.js` (`VERSION` and the welcome heading), `src/shell.html` (header badge),
`package.json` and `CHANGELOG.md`; the citation link in `src/app-report.js` (`SOFTWARE_URL`).

## Releases and DOI
Repository releases (and a Zenodo DOI, if enabled) now cover the ANN tool alone.
