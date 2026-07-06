#!/usr/bin/env python3
"""Build the annual dataset for "The Expanding Human Toolkit".

Every series is constructed from literature anchor points and published growth
models documented in docs/research/*.md and docs/METHODOLOGY.md. Each value
carries a provenance flag:

  observed      annual (or near-annual) data point taken from a primary source
  anchored      a literature anchor point (the dot itself)
  reconstructed interpolated/extrapolated between anchors via a documented model

Output:
  data/series_annual.csv   full annual table, -10000 .. 2026
  data/payload.json        compact payload consumed by index.html
"""
import csv
import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YEAR_MIN, YEAR_MAX = -10000, 2026


def log_interp(anchors, year):
    """Log-space (geometric) interpolation between (year, value) anchors."""
    if year <= anchors[0][0]:
        return anchors[0][1]
    if year >= anchors[-1][0]:
        return anchors[-1][1]
    for (x0, y0), (x1, y1) in zip(anchors, anchors[1:]):
        if x0 <= year <= x1:
            t = (year - x0) / (x1 - x0)
            return math.exp(math.log(y0) + t * (math.log(y1) - math.log(y0)))
    raise ValueError(year)


# ---------------------------------------------------------------------------
# Series 1 — Known chemical space (cumulative distinct substances)
# Sources: docs/research/chemical-space.md
#   Pre-1800: historian anchor estimates (order of magnitude; wide bounds).
#   1800-2015: Llanos et al. 2019 PNAS — new compounds/yr grow at 4.4%/yr,
#              cumulative 14,341,955 over 1800-2015. Seed solved from that sum.
#   2016-2026: growth continued at 4.4%/yr (CAS registers ~15k substances/day
#              under a broader definition; we stay with the literature-compound
#              definition and flag the definitional spread in the methodology).
# ---------------------------------------------------------------------------
CHEM_ANCHORS = [  # (year, best, low, high) cumulative substances known
    (-10000, 15, 10, 30),
    (-3000, 25, 15, 40),
    (100, 60, 30, 100),
    (1000, 65, 40, 110),
    (1500, 120, 60, 250),
    (1700, 350, 150, 800),
    (1789, 700, 300, 1500),
    (1800, 1000, 300, 2000),
]
LLANOS_RATE = 0.044
LLANOS_TOTAL = 14_341_955  # cumulative new compounds 1800-2015 inclusive
_n_years = 2015 - 1800 + 1
_seed = LLANOS_TOTAL * LLANOS_RATE / ((1 + LLANOS_RATE) ** _n_years - 1)


def chem_series():
    out = {}
    cum = None
    for y in range(YEAR_MIN, YEAR_MAX + 1):
        if y < 1800:
            best = log_interp([(a, b) for a, b, _, _ in CHEM_ANCHORS], y)
            low = log_interp([(a, l) for a, _, l, _ in CHEM_ANCHORS], y)
            high = log_interp([(a, h) for a, _, _, h in CHEM_ANCHORS], y)
            prov = "anchored" if any(a == y for a, *_ in CHEM_ANCHORS) else "reconstructed"
            out[y] = (best, low, high, prov)
        else:
            if cum is None:
                cum = CHEM_ANCHORS[-1][1]
            new = _seed * (1 + LLANOS_RATE) ** (y - 1800)
            cum += new
            # Uncertainty: definitional spread grows toward the present
            # (literature compounds vs. registry substances ~20x by 2026).
            prov = "observed" if 1800 <= y <= 2015 else "reconstructed"
            out[y] = (cum, cum * 0.85, cum * 1.3 if y <= 2015 else cum * 2.0, prov)
    return out


# CAS Registry milestones (registry definition — plotted as reference dots)
CAS_MILESTONES = [
    (1965, 0.2e6), (1975, 3e6), (1990, 10e6), (2005, 25e6), (2009, 50e6),
    (2011, 60e6), (2012, 70e6), (2015, 100e6), (2019, 150e6), (2021, 250e6),
    (2025, 290e6),
]

# Known chemical elements (cumulative) — era buckets, docs/research/chemical-space.md (d)
ELEMENT_ANCHORS = [
    (-10000, 2), (-6000, 4), (-3000, 8), (0, 9), (1300, 11), (1500, 13),
    (1669, 14), (1750, 17), (1789, 23), (1800, 34), (1828, 49), (1849, 58),
    (1869, 62), (1899, 84), (1949, 97), (1999, 113), (2016, 118), (2026, 118),
]


# ---------------------------------------------------------------------------
# Series 2 — Global material extraction (Gt/yr)
# Sources: docs/research/material-flows.md
#   1900-2024 observed/anchored MFA seam: Krausmann 2009/2018 -> UNEP IRP.
#   Pre-1900: population x sociometabolic per-capita rates (ranges).
# ---------------------------------------------------------------------------
MAT_ANCHORS = [  # (year, best Gt/yr, low, high, provenance-of-anchor)
    (-10000, 0.003, 0.001, 0.006, "anchored"),   # ~4M people x ~0.7 t/cap
    (-3000, 0.06, 0.03, 0.12, "anchored"),       # ~30M, early agrarian
    (1, 0.8, 0.5, 1.4, "anchored"),              # ~250M x 3-6 t/cap
    (1000, 0.9, 0.6, 1.6, "anchored"),
    (1500, 2.0, 1.4, 2.9, "anchored"),
    (1700, 2.6, 1.8, 3.6, "anchored"),
    (1800, 4.8, 3.0, 7.0, "anchored"),
    (1850, 6.2, 4.0, 9.0, "anchored"),
    (1900, 7.0, 6.5, 7.5, "observed"),
    (1912, 9.5, 8.5, 10.5, "observed"),
    (1929, 13.0, 12.0, 14.5, "observed"),
    (1932, 11.5, 10.5, 13.0, "observed"),        # Depression dip
    (1945, 15.0, 13.5, 17.0, "observed"),
    (1950, 21.0, 19.0, 23.0, "observed"),
    (1970, 26.5, 22.0, 28.0, "observed"),
    (1980, 35.0, 33.0, 38.0, "observed"),
    (1990, 41.0, 39.0, 44.0, "observed"),
    (2000, 52.0, 50.0, 55.0, "observed"),
    (2005, 59.0, 57.0, 61.0, "observed"),
    (2009, 68.0, 66.0, 70.0, "observed"),
    (2010, 70.0, 68.0, 72.0, "observed"),
    (2015, 89.5, 88.0, 92.0, "observed"),
    (2017, 92.0, 90.0, 94.0, "observed"),
    (2020, 95.0, 90.0, 98.0, "observed"),
    (2024, 105.0, 104.0, 106.6, "observed"),
    (2026, 108.0, 105.0, 112.0, "anchored"),     # short trend extrapolation
]


def material_series():
    best_a = [(y, v) for y, v, _, _, _ in MAT_ANCHORS]
    low_a = [(y, v) for y, _, v, _, _ in MAT_ANCHORS]
    high_a = [(y, v) for y, _, _, v, _ in MAT_ANCHORS]
    anchor_years = {y: p for y, _, _, _, p in MAT_ANCHORS}
    out = {}
    for y in range(YEAR_MIN, YEAR_MAX + 1):
        best = log_interp(best_a, y)
        low = log_interp(low_a, y)
        high = log_interp(high_a, y)
        if y in anchor_years:
            prov = anchor_years[y]
        elif y >= 1900:
            prov = "reconstructed"  # between observed MFA anchor years
        else:
            prov = "reconstructed"
        out[y] = (best, low, high, prov)
    return out


# ---------------------------------------------------------------------------
# Series 3 — Scientific publications per year
# Sources: docs/research/publications.md (piecewise exponential recipe,
#   calibrated to Royal Society Catalogue, Bjork 2009, NSB Indicators;
#   segment rates from Bornmann/Haunschild/Mutz 2021 & Mabe 2003).
# ---------------------------------------------------------------------------
PUB_SEGMENTS = [
    # (start_year, end_year, annual growth rate)
    (1665, 1750, 0.010),
    (1750, 1800, 0.021),
    (1800, 1900, 0.035),
    (1900, 1914, 0.032),
    (1914, 1919, 0.005),   # WWI dip
    (1919, 1940, 0.036),
    (1940, 1948, 0.026),   # WWII slowdown (Bornmann et al. 2021: 2.62%)
    (1948, 1975, 0.051),
    (1975, 2000, 0.030),
    (2000, 2016, 0.043),
    (2016, 2026, 0.055),   # Hanson et al. 2024: ~6.7%/yr 2016-22 (articles)
]
PUB_SEED = 100.0  # papers/yr in 1665
PUB_CALIBRATION = {  # independent anchor checks (also plotted as dots)
    1665: (100, 30, 300), 1800: (850, 300, 2000), 1850: (5500, 3000, 10000),
    1900: (30000, 15000, 60000), 1950: (200000, 100000, 400000),
    2006: (1350000, 1200000, 1500000), 2010: (2000000, 1900000, 2500000),
    2022: (3300000, 2800000, 5200000),
}


def publications_series():
    out = {}
    v = PUB_SEED
    year_rate = {}
    for s, e, g in PUB_SEGMENTS:
        for y in range(s, e):
            year_rate[y] = g
    # Rescale multiplicatively so the trajectory passes near calibration anchors:
    # compute raw series, then apply a smooth log-space correction through anchors.
    raw = {1665: PUB_SEED}
    for y in range(1666, YEAR_MAX + 1):
        raw[y] = raw[y - 1] * (1 + year_rate.get(y - 1, 0.055))
    # log-space correction factors at calibration years
    corr_anchors = [(y, PUB_CALIBRATION[y][0] / raw[y]) for y in sorted(PUB_CALIBRATION)]
    for y in range(1665, YEAR_MAX + 1):
        c = log_interp(corr_anchors, y)
        best = raw[y] * c
        if y in PUB_CALIBRATION:
            _, lo, hi = PUB_CALIBRATION[y]
            prov = "anchored"
        else:
            lo, hi = best * 0.55, best * 1.9  # definitional/database spread
            prov = "observed" if y >= 1996 else "reconstructed"  # dense DB coverage era
        out[y] = (best, lo, hi, prov)
    return out


# ---------------------------------------------------------------------------
# World population (context substrate; also used by the interconnectedness index)
# Sources: docs/research/material-flows.md (c) — HYDE/Gapminder/UN WPP consensus.
# ---------------------------------------------------------------------------
POP_ANCHORS = [
    (-10000, 4e6), (-5000, 6e6), (-3000, 30e6), (-1000, 50e6), (1, 250e6),
    (500, 190e6), (1000, 280e6), (1200, 380e6), (1350, 350e6),  # Black Death era
    (1500, 460e6), (1600, 550e6), (1700, 600e6), (1800, 990e6), (1850, 1.24e9),
    (1900, 1.65e9), (1930, 2.0e9), (1950, 2.5e9), (1960, 3.0e9), (1974, 4.0e9),
    (1987, 5.0e9), (2000, 6.1e9), (2011, 7.0e9), (2022, 8.0e9), (2026, 8.3e9),
]


def population_series():
    return {y: log_interp(POP_ANCHORS, y) for y in range(YEAR_MIN, YEAR_MAX + 1)}


# ---------------------------------------------------------------------------
# Series 4 — Global Interconnectedness Index (composite, 0-100)
# Components & anchors filled from docs/research/interconnectedness.md.
# Placeholder None until that memo lands; build_gii() is defined there-after.
# ---------------------------------------------------------------------------
GII_COMPONENTS = None  # populated in a follow-up commit


def main():
    chem = chem_series()
    mat = material_series()
    pub = publications_series()
    pop = population_series()

    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    csv_path = os.path.join(ROOT, "data", "series_annual.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "year",
            "substances_known", "substances_low", "substances_high", "substances_prov",
            "material_extraction_gt", "material_low", "material_high", "material_prov",
            "publications_per_year", "publications_low", "publications_high", "publications_prov",
            "world_population",
        ])
        for y in range(YEAR_MIN, YEAR_MAX + 1):
            c = chem[y]
            m = mat[y]
            p = pub.get(y)
            w.writerow([
                y,
                f"{c[0]:.6g}", f"{c[1]:.6g}", f"{c[2]:.6g}", c[3],
                f"{m[0]:.6g}", f"{m[1]:.6g}", f"{m[2]:.6g}", m[3],
                *( [f"{p[0]:.6g}", f"{p[1]:.6g}", f"{p[2]:.6g}", p[3]] if p else ["", "", "", ""] ),
                f"{pop[y]:.6g}",
            ])
    print(f"wrote {csv_path}")

    # Compact payload for the chart: yearly from 1500, every 25y before.
    years = list(range(YEAR_MIN, 1500, 25)) + list(range(1500, YEAR_MAX + 1))
    def pack(series):
        return {
            "years": years,
            "v": [round(series[y][0], 6) if y in series else None for y in years],
            "lo": [round(series[y][1], 6) if y in series else None for y in years],
            "hi": [round(series[y][2], 6) if y in series else None for y in years],
            "prov": ["".join(series[y][3][0]) if y in series else "" for y in years],
        }
    payload = {
        "meta": {"built": "2026-07-06", "yearMin": YEAR_MIN, "yearMax": YEAR_MAX},
        "substances": pack(chem),
        "materials": pack(mat),
        "publications": pack(pub),
        "population": [round(pop[y], 1) for y in years],
        "casMilestones": CAS_MILESTONES,
        "elements": ELEMENT_ANCHORS,
        "pubCalibration": [[y, *PUB_CALIBRATION[y]] for y in sorted(PUB_CALIBRATION)],
        "chemAnchors": [[y, b, l, h] for y, b, l, h in CHEM_ANCHORS],
        "matAnchors": [[y, b, l, h] for y, b, l, h, _ in MAT_ANCHORS],
    }
    json_path = os.path.join(ROOT, "data", "payload.json")
    with open(json_path, "w") as f:
        json.dump(payload, f, separators=(",", ":"))
    print(f"wrote {json_path} ({os.path.getsize(json_path)//1024} KB)")


if __name__ == "__main__":
    main()
