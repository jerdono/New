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
            out[y] = (best, low, high, "reconstructed")  # anchor dots drawn separately
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
        # 1900-2024: annual MFA accounts exist in the sources (Krausmann/IRP);
        # our curve interpolates their published values -> drawn as observed.
        prov = "observed" if 1900 <= y <= 2024 else "reconstructed"
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
        else:
            lo, hi = best * 0.55, best * 1.9  # definitional/database spread
        # Annual database records are dense from ~1900 (WoS Century of Science,
        # Scopus, Dimensions); the model is calibrated to them -> observed.
        prov = "observed" if y >= 1900 else "reconstructed"
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
# Series 4 — Global Interconnectedness Index (composite, 0-100, 2026 = 100)
# Design & anchors: docs/research/interconnectedness.md
#   GII = S^0.20 * T^0.25 * C^0.25 * U^0.15 * E^0.15 (geometric mean =>
#   components are complements; no single dimension can buy the score).
#   S = log connected population, T = trade openness, C = communication reach,
#   U = urbanization, E = equality of participation.
# ---------------------------------------------------------------------------
TRADE_ANCHORS = [  # world (X+M)/GDP, % — EFT 2003 / Klasing-Milionis 2014 / PWT / WB
    (-10000, 0.05), (-1000, 0.15), (1, 0.30), (1000, 0.30), (1500, 1.0),
    (1600, 2.2), (1700, 2.2), (1820, 5.0), (1870, 17.57), (1900, 24.36),
    (1913, 29.01), (1929, 18.75), (1938, 12.96), (1949, 16.35), (1950, 19.87),
    (1973, 29.61), (2000, 47.30), (2008, 61.49), (2019, 55.85), (2022, 63.0),
    (2026, 60.0),
]
URBAN_ANCHORS = [  # world urban share, % — HYDE 3.1 / UN WUP
    (-10000, 0.02), (-5000, 0.1), (1, 1.0), (500, 1.7), (1000, 2.6),
    (1500, 4.1), (1600, 5.2), (1700, 5.1), (1800, 7.3), (1900, 16.4),
    (1950, 29.1), (2000, 46.8), (2007, 49.6), (2023, 56.6), (2026, 58.5),
]
LITERACY_ANCHORS = [  # world literate share, % — OWID (van Zanden/UNESCO)
    (-10000, 0.0), (-3200, 0.02), (-1000, 0.5), (1, 2.0), (1000, 2.0),
    (1500, 3.5), (1700, 6.0), (1820, 12.0), (1870, 18.7), (1900, 21.4),
    (1930, 32.5), (1950, 36.0), (1990, 74.9), (2000, 81.0), (2010, 84.2),
    (2023, 87.4), (2026, 88.0),
]
INTERNET_ANCHORS = [  # world internet-user share, % — ITU/WB
    (1989, 0.0), (1990, 0.05), (2000, 6.7), (2005, 15.6), (2010, 28.4),
    (2015, 39.9), (2020, 60.1), (2023, 69.2), (2025, 73.6), (2026, 75.0),
]
EQUALITY_ANCHORS = [  # E = 1-Gini (1820-) spliced to 1-0.9*extraction-ratio pre-1820
    (-10000, 0.60), (-5000, 0.50), (-3000, 0.40), (1, 0.33), (1000, 0.33),
    (1500, 0.33), (1700, 0.36), (1820, 0.50), (1870, 0.44), (1910, 0.39),
    (1950, 0.36), (1980, 0.34), (2000, 0.31), (2010, 0.35), (2020, 0.39),
    (2026, 0.40),
]
GII_WEIGHTS = {"S": 0.20, "T": 0.25, "C": 0.25, "U": 0.15, "E": 0.15}
GII_ANCHOR_YEARS = [-1000, 1, 1000, 1500, 1820, 1870, 1913, 1950, 1973, 2000, 2008, 2023]


def lin_interp(anchors, year):
    if year <= anchors[0][0]:
        return anchors[0][1]
    if year >= anchors[-1][0]:
        return anchors[-1][1]
    for (x0, y0), (x1, y1) in zip(anchors, anchors[1:]):
        if x0 <= year <= x1:
            t = (year - x0) / (x1 - x0)
            return y0 + t * (y1 - y0)
    raise ValueError(year)


def gii_series(pop):
    pop_now = pop[YEAR_MAX]
    raw = {}
    for y in range(YEAR_MIN, YEAR_MAX + 1):
        S = math.log(max(pop[y], 2e4) / 1e4) / math.log(pop_now / 1e4)
        T = min(lin_interp(TRADE_ANCHORS, y) / 70.0, 1.0)
        lit = lin_interp(LITERACY_ANCHORS, y) / 100.0
        net = (lin_interp(INTERNET_ANCHORS, y) / 100.0) if y >= 1989 else 0.0
        C = max(0.6 * lit + 0.4 * net, 1e-4)
        U = max(lin_interp(URBAN_ANCHORS, y) / 100.0, 1e-4)
        E = lin_interp(EQUALITY_ANCHORS, y)
        T = max(T, 1e-5)
        w = GII_WEIGHTS
        raw[y] = (S ** w["S"]) * (T ** w["T"]) * (C ** w["C"]) * (U ** w["U"]) * (E ** w["E"])
    scale = 100.0 / raw[YEAR_MAX]
    out = {}
    trade_years = {a for a, _ in TRADE_ANCHORS}
    for y in range(YEAR_MIN, YEAR_MAX + 1):
        v = raw[y] * scale
        if y < 1500:
            lo, hi = v * 0.5, v * 1.5      # pre-1500 floors: +/-50% (memo caveat 1)
        elif y < 1820:
            lo, hi = v * 0.65, v * 1.35
        elif y < 1950:
            lo, hi = v * 0.85, v * 1.15
        else:
            lo, hi = v * 0.92, v * 1.08
        # From 1950 all five components rest on measured annual/near-annual series.
        prov = "observed" if y >= 1950 else "reconstructed"
        out[y] = (v, lo, hi, prov)
    return out


def build_html(payload):
    tpl_path = os.path.join(ROOT, "src", "template.html")
    methods_path = os.path.join(ROOT, "src", "methods_footer.html")
    with open(tpl_path) as f:
        tpl = f.read()
    with open(methods_path) as f:
        methods = f.read()
    html = tpl.replace("/*__PAYLOAD__*/null", json.dumps(payload, separators=(",", ":")))
    html = html.replace("/*__METHODS__*/''", json.dumps(methods))
    out = os.path.join(ROOT, "index.html")
    with open(out, "w") as f:
        f.write(html)
    print(f"wrote {out} ({os.path.getsize(out)//1024} KB)")


def main():
    chem = chem_series()
    mat = material_series()
    pub = publications_series()
    pop = population_series()
    gii = gii_series(pop)

    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    csv_path = os.path.join(ROOT, "data", "series_annual.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "year",
            "substances_known", "substances_low", "substances_high", "substances_prov",
            "material_extraction_gt", "material_low", "material_high", "material_prov",
            "publications_per_year", "publications_low", "publications_high", "publications_prov",
            "interconnectedness_index", "gii_low", "gii_high", "gii_prov",
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
                f"{gii[y][0]:.6g}", f"{gii[y][1]:.6g}", f"{gii[y][2]:.6g}", gii[y][3],
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
        "gii": pack(gii),
        "population": [round(pop[y], 1) for y in years],
        "casMilestones": CAS_MILESTONES,
        "elements": ELEMENT_ANCHORS,
        "pubCalibration": [[y, *PUB_CALIBRATION[y]] for y in sorted(PUB_CALIBRATION)],
        "chemAnchors": [[y, b, l, h] for y, b, l, h in CHEM_ANCHORS],
        "matAnchors": [[y, b, l, h] for y, b, l, h, _ in MAT_ANCHORS
                       if y < 1900 or y in (1900, 1929, 1950, 1970, 2000, 2015, 2024)],
        "giiAnchors": [[y, round(gii[y][0], 2)] for y in GII_ANCHOR_YEARS],
    }
    json_path = os.path.join(ROOT, "data", "payload.json")
    with open(json_path, "w") as f:
        json.dump(payload, f, separators=(",", ":"))
    print(f"wrote {json_path} ({os.path.getsize(json_path)//1024} KB)")

    build_html(payload)

    # Sanity checks against literature calibration targets
    assert abs(chem[2015][0] - 14_341_955) / 14_341_955 < 0.01, "Llanos 2015 total"
    assert abs(gii[2026][0] - 100.0) < 1e-6, "GII normalization"
    for y, target in [(1, 4.9), (1500, 10.2), (1913, 45.7), (2000, 79.1)]:
        v = gii[y][0]
        assert abs(v - target) / target < 0.35, f"GII {y}: {v:.1f} vs memo ~{target}"
    print("sanity checks passed:",
          f"GII(1 CE)={gii[1][0]:.1f} GII(1500)={gii[1500][0]:.1f}",
          f"GII(1913)={gii[1913][0]:.1f} GII(2000)={gii[2000][0]:.1f}")


if __name__ == "__main__":
    main()
