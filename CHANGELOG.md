# Changelog — SaNaSoft-ANN

## [2.3.0] – 2026-10-16

### Added
- A "Home" link to the SaNaSoft start page (https://sanapls.com/) in the same place as in every SaNaSoft app:
  top left in a thin bar above the header, and bottom left in the footer. A link to SaNaSoft fsQCA sits in the same bar.
- The logo and name lead to the Welcome step of ANN; nothing you entered is lost.
- Your work is kept automatically in this browser. Going to the start page and coming back in the same tab
  (Back button or the ANN link) reopens the same step with the same data and settings; in a new tab the Welcome step
  offers to resume. A warning appears if you try to leave while an analysis is running.
- The browser tab title names the current step; a "Skip to content" link; the steps are real buttons for keyboard users.
- Navigation test (tests/e2e/test_nav.py).

### Changed
- The fsQCA link moved from the header to the suite bar. No change to any computation.

## [2.2.0] – 2026-10-16

### Changed
- New "Ink & Paper" look, shared with the SaNaSoft suite: warm paper background, IBM Plex Sans and Source Serif 4,
  one quiet ink-blue accent, flat panels without shadows or gradients, APA-style tables (three rules, no fills),
  hairline notices instead of coloured side stripes. Charts and the network diagram use colour-blind-friendly colours.
- No change to any computation: the engine, results and reports are identical.

## [2.1.0] – 2026-09-28

### Changed
- SaNaSoft-ANN now has its own repository and address: https://samssabraznawaz.github.io/ann/ (previously the `ann/` folder of the SaNaSoft fsQCA repository). The software citation and the link to SaNaSoft fsQCA (https://samssabraznawaz.github.io/fsqca/) were updated.

### Removed
- The built-in SPSS tutorial. The analysis, defaults, presets, results and report are unchanged.

## [2.0.0] – 2026-09-25

### Added
- New pure-JavaScript neural engine (Float64, seeded) running in a Web Worker; FFBP (gradient descent with momentum), scaled conjugate gradient (Møller, 1993) and Adam.
- Full Leong et al. (2025) procedure: ten networks via k-fold cross-validation (90/10), RMSE table (mean, SD), R² (predictive and Leong formula), averaged normalized importance.
- Multiple ANN models (one per endogenous construct) in one run.
- Automatic selection of hidden neurons.
- PLS-SEM vs ANN ranking comparison.
- SPSS-style case processing summary, model summary, parameter estimates and network diagram (SVG/PNG export).
- Training curves, predicted vs observed, residuals, linear-regression benchmark, RESET test, VIF, data screening.
- Report generator with APA-formatted tables in seven citation styles (APA 7th, APA 6th, Harvard, Emerald, Chicago, IEEE, Vancouver — aligned with SaNaSoft fsQCA); Word/HTML export; software citation added automatically.
- Project save/open, built-in demo data, one-click presets (Leong et al., SPSS defaults), SPSS tutorial.
- Unit tests, end-to-end test and calibration against scikit-learn.
- Published as part of the SaNaSoft repository at `/ann/`, with links to and from SaNaSoft fsQCA.

### Fixed (relative to 1.x)
- Dependent variable is now normalized to 0–1 when the output activation is sigmoid.
- Missing values are handled by listwise deletion instead of being replaced by 0.
- Relative error now follows the SPSS definition (SSE / total sum of squares).
- Importance is averaged over all networks instead of a single small test sample.
- Random seed is respected for reproducibility.
- Corrected the Leong et al. (2025) reference and DOI.

## [1.0.0] – 2026-09-24
- First version (TensorFlow.js based).
