# Rule-Based Intraday Futures Returns

**Quantitative finance research working paper | October 2026**  
**Raj Phuyal | Independent Researcher**

Welcome to my quantitative finance research portfolio. I study the statistical reliability of rule-based intraday futures trading outcomes, with particular attention to payoff asymmetry, uncertainty, and the distinction between a promising historical result and a validated trading strategy.

This repository accompanies my research working paper and documents my current evidence, reproducible descriptive calculations, and next-stage research questions. I present it as part of my prospective PhD research portfolio; it is not a peer-reviewed publication.

## Read my research

- [Working paper (PDF)](paper/Intraday_Futures_Research_Working_Paper.pdf)
- [Working paper (editable Word file)](paper/Intraday_Futures_Research_Working_Paper.docx)
- [Research integrity and transparency](RESEARCH_INTEGRITY.md)
- [Reproducibility and data provenance](analysis/REPRODUCIBILITY.md)

## Recorded sample

| Measure | Recorded value |
|---|---:|
| Recorded trade outcomes | 242 |
| Distinct trading dates | 180 |
| Total risk-normalized outcomes | +149.970R |
| Mean per trade | +0.620R |
| Median per trade | −1.000R |
| Profit factor | 2.172 |

My available observations cover **2017–2018** and **2025–2026**, with no observations for **2019–2024**. I do not present them as a continuous ten-year backtest. These records are not independently audited live returns or proof of future profitability. Each R multiple represents a result relative to initial trade risk, not a portfolio percentage return.

## Reproduce the descriptive analysis

From the repository root, with Python installed, run:

```bash
python analysis/analyze.py
```

The script reads [`data/trade_outcomes.csv`](data/trade_outcomes.csv) and recalculates key descriptive statistics. It does **not** reproduce every inferential test in the manuscript, reconstruct raw futures price data, or audit transaction costs and fills. I describe these boundaries in my [reproducibility notes](analysis/REPRODUCIBILITY.md).

## My research direction

My next objective is to reconstruct continuous price and signal histories, pre-specify and freeze rules, evaluate realistic execution costs, account for time dependence and multiple testing, and run chronological out-of-sample tests. I regard negative and inconclusive results as important research findings.

## Repository contents

- [`paper/`](paper/) — research manuscript in PDF and Word formats
- [`analysis/`](analysis/) — descriptive analysis code and reproducibility notes
- [`data/`](data/) — outcomes used by the descriptive script
- [`figures/`](figures/) — charts included with the working-paper package
- [`RESEARCH_INTEGRITY.md`](RESEARCH_INTEGRITY.md) — my research responsibilities and evidence boundaries
- [`CITATION.cff`](CITATION.cff) — citation metadata

## Attribution and research integrity

I take responsibility for understanding and verifying the research I publish. Computational, statistical, and editorial assistance, including AI-assisted tools, contributed to the preparation of parts of this portfolio; I disclose such assistance where institutional or publication requirements apply. The source records, assumptions, and analysis limitations remain open to scrutiny. See my [research-integrity statement](RESEARCH_INTEGRITY.md).

**Research status:** Independent working paper; exploratory recorded-outcome evidence; not peer-reviewed and not independently audited.
