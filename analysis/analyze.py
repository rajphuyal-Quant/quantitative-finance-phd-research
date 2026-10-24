"""Reproduce descriptive statistics from the accompanying risk-normalized trade outcomes.
Run: python analysis/analyze.py
Uses only the Python standard library. No strategy signals or transaction costs are reconstructed.
"""
from pathlib import Path
import csv, statistics, collections
p=Path(__file__).resolve().parents[1]/"data"/"trade_outcomes.csv"
with p.open(newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
r=[float(x["R"]) for x in rows]
w=[x for x in r if x>0]; losses=[x for x in r if x<0]; zeros=[x for x in r if x==0]
pf=sum(w)/abs(sum(losses)) if losses else float("inf")
print(f"Trades: {len(r)}")
print(f"Net R: {sum(r):.3f}")
print(f"Mean R: {statistics.mean(r):.6f}")
print(f"Median R: {statistics.median(r):.3f}")
print(f"Wins/losses/zero: {len(w)}/{len(losses)}/{len(zeros)}")
print(f"Profit factor: {pf:.6f}")
print(f"Distinct dates: {len(set(x['Date'] for x in rows))}")
for field in ("Instrument","Period"):
 print("\n"+field)
 groups=collections.defaultdict(list)
 for x in rows: groups[x[field]].append(float(x["R"]))
 for key,v in sorted(groups.items()): print(f"  {key}: n={len(v)} net={sum(v):.3f} mean={statistics.mean(v):.4f}")
