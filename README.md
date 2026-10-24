# Rule-Based Intraday Futures Returns

**Independent quantitative-finance research working paper | October 2026**  
**Author:** Raj Phuyal

This repository presents an exploratory empirical study of risk-normalized trade outcomes from rule-based Nasdaq and Euro futures strategies, and a research agenda for testing robustness and generalizability. It is intended as part of a **PhD application research portfolio**, not as a peer-reviewed publication.

## Read the paper

- [Research paper (PDF)](paper/Intraday_Futures_Research_Working_Paper.pdf)
- [Editable manuscript (DOCX)](paper/Intraday_Futures_Research_Working_Paper.docx)
- [Research statement](research_statement/Research_Statement.pdf)

## Recorded sample

| Measure | Recorded value |
|---|---:|
| Trade outcomes | 242 |
| Trading dates | 180 |
| Cumulative R | +149.970R |
| Average trade R | +0.620R |
| Median trade R | -1.000R |
| Profit factor | 2.172 |

**Crucial scope limitation:** observations cover 2017–2018 and 2025–2026; 2019–2024 is missing. This is **not** a continuous ten-year backtest, an independently verified strategy audit, or evidence of a proven out-of-sample trading edge. R is normalized initial trade risk, not a portfolio percentage return.

## Reproduce the basic descriptive results

```bash
python analysis/analyze.py
```

The analysis reads `data/trade_outcomes.csv`, derived from the combined research workbook. It verifies counts, net R, mean, median, profit factor, and breakdowns by instrument and period. It **does not** reproduce the paper's advanced inference or verify historical signals, fills, commissions, or data selection. See [reproducibility notes](analysis/REPRODUCIBILITY.md).

## Portfolio focus

The research demonstrates a developing approach to research design, risk-normalized analysis, empirical inference, sensitivity to outliers, and transparent limitations. The planned next phase includes continuous historical reconstruction, frozen strategy specifications, transaction-cost modeling, and untouched chronological validation.

## Research integrity

This is an independently presented research project using analytical and editorial assistance. Calculations, references, interpretation, and authorship should be checked by the researcher before submission. See [scope and integrity statement](RESEARCH_INTEGRITY.md). No claim of peer review, journal acceptance, or confirmed profitability is made.

## Files

- `paper/` — manuscript and reading PDF
- `research_statement/` — statement of research interests
- `data/` — trade-level R outcomes for replication; **review before public release**
- `analysis/` — executable descriptive analysis and methodological notes
- `figures/` — illustrative research figures from the working-paper package
- `application/` — portfolio summary and application checklist

## Citation

See [CITATION.cff](CITATION.cff).
