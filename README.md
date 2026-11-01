# Telecom Churn Classification

[![Validation](https://github.com/Ashik-Mohammed-S/Telecom_Churn_prediction/actions/workflows/validate.yml/badge.svg)](https://github.com/Ashik-Mohammed-S/Telecom_Churn_prediction/actions/workflows/validate.yml)

Identify customers with the supplied churn label, evaluating positive-class detection alongside precision and calibration.

Independent public portfolio work; historical educational notebooks remain under `historical/`. The current implementation and results described here take precedence over historical in-sample numbers.

## Data and approach

Three 7,043-row source tables joined one-to-one on customerID.

Stratified 80/20 holdout; fit imputers, scaling and categorical encoders on training data only. Evaluate a class-balanced logistic regression at a fixed 0.5 threshold against a dummy prior baseline.

## Current full-data result

| Measure | Current analysis | Baseline where applicable |
| --- | --- | --- |
| ROC-AUC | 0.841 | 0.500 |
| PR-AUC (average precision) | 0.632 | 0.265 |
| Churn recall | 0.783 | 0.000 |
| Accuracy | 0.737 | 0.735 |

Results are specific to the documented dataset and split. See generated `results/analysis.json` after execution for full metrics and assumptions.

## Run locally

Use the Python version in `.python-version`, then:

```sh
python -m pip install -r requirements.txt
python scripts/fetch_data.py
python scripts/run_notebook.py --mode full
```

Reference data is committed under `dataset/`, directly or as reconstructable compressed parts. The downloader verifies checksums and restores stored data offline. See [DATA.md](DATA.md) and [dataset-sources.json](dataset-sources.json) for provenance and upstream terms. Package installation and the spaCy model, where needed, require network access on a fresh machine.

## Review the implementation

Inspect the one-to-one join, target mapping, preprocessing pipeline and PR-AUC/recall tradeoff. Start with [scripts/analysis.py](scripts/analysis.py), then the root notebook. The workflow validates dependencies, smoke checks and full-data notebook execution with dataset downloads disabled.

## Limitations

Accuracy alone barely exceeds the majority baseline, while positive-class recall changes substantially. No test-set threshold tuning or claim of retention-campaign uplift is made.

[Method notes](ANALYSIS.md) · [All portfolio projects](https://github.com/Ashik-Mohammed-S/Ashik-Mohammed-S/blob/main/PORTFOLIO.md)
