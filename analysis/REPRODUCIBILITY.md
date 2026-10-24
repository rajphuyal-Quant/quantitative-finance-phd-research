# Reproducibility and Data Provenance

I assembled the descriptive dataset from the `All Trades` sheet of my combined research workbook (`Quant_PhD_Combined_Research_Workbook.xlsx`). The published CSV contains 242 numeric risk-normalized R outcomes and the fields used for this repository's summary analysis. I have not published the full source workbook because it may contain unrelated material.

## Run my descriptive analysis

From the repository root:

```bash
python analysis/analyze.py
```

The script uses the Python standard library. It recalculates trade counts, cumulative and mean R, median R, profit factor, and instrument/period summaries from `data/trade_outcomes.csv`. These are **descriptive replications only**. My current script does not recreate every bootstrap, significance test, sensitivity figure, or scenario in the manuscript.

## Data and inference boundaries

The available record has two non-contiguous windows (2017–2018 and 2025–2026), without 2019–2024. It includes dates but not a reliable within-day execution sequence, underlying intraday price bars, independently verified fills, or an exhaustive list of all eligible signals. As a result, sequential drawdown estimates may depend on within-day ordering. Transaction costs, slippage, and market-regime assignments have not been reconstructed from independently verified records.

## Next-stage validation

I intend to reconcile recorded outcomes with primary order records where available, document revisions and exclusions, freeze strategy specifications, reconstruct continuous price/signal histories, and evaluate untouched chronological samples with execution-cost adjustments and dependence-aware uncertainty estimates.

I welcome reproducibility questions and will distinguish reproduced outcomes from analyses that remain provisional.
