# Research memo — Scientific publications per year (1665 → 2025)

> Compiled by a web-research pass on 2026-07-06. [derived] marks calibrated
> interpolations by the research pass, not published numbers.

## (a) Anchor table: publications per year

| Year | Papers/yr (best) | Low–High | Basis |
|---|---|---|---|
| 1665 | ~100 | 30–300 | First two journals: *Journal des Sçavans* (Jan 1665), *Phil. Trans.* (Mar 1665) |
| 1700 | ~150 | 50–500 | [derived] ~30 journals; Kronick 1976 (1,858 periodical titles 1665–1790) |
| 1750 | ~300 | 100–1,000 | [derived] Bornmann & Mutz 2015 phase 1 (<1%/yr to mid-18th c.); ~10 journals (Price) |
| 1800 | ~850 | 300–2,000 | [derived] backcast from Royal Society *Catalogue of Scientific Papers 1800–1900* (~770–800k papers for the century); ~100 journals |
| 1850 | ~5,500 | 3,000–10,000 | [derived] 3.5%/yr Catalogue-consistent; ~1,000 journals by 1850 (Price) |
| 1900 | ~30,000 | 15,000–60,000 | [derived] Catalogue endpoint ~28k; Bornmann 4.10% backcast ~34k; ~10,000 journals (Price) |
| 1950 | ~200,000 | 100k–400k | [derived] Mabe 3.23% pre-1940 + WWII dip 2.62%/yr (BHM 2021) |
| 1980 | ~650,000 | 400k–900k | [derived] post-war ~5%/yr (BHM 2021: PhysTech 5.51%, Life 4.79%) |
| 2000 | ~1.15M | 0.9–1.5M | [derived]; Björk, Roos & Lauri 2009: 1.35M peer-reviewed articles in 2006 |
| 2010 | ~2.0M | 1.9–2.5M | NSB Science & Engineering Indicators (Scopus S&E) |
| 2016 | ~1.9M (WoS+Scopus) | — | Hanson et al. 2024, QSS 5(4):823 |
| 2020 | ~3.0M articles / 4.2M citable / 4.7M Dimensions / 10.2M OpenAlex works | 3–10M by definition | STM 2021; Alperin et al. 2024 (arXiv:2404.17663) |
| 2022 | 3.3M (Scopus S&E) | 2.8–5.2M | NSB Indicators; Hanson et al. 2024 |
| 2023–25 | ~3.3–3.5M S&E articles; ~4.5–5.5M all article-types | 3–11M | NSB; Scopus/Dimensions extrapolation |

Journal counts (Price 1961/1963; Mabe 2003): ~10 (1750) → ~100 (1800) → ~1,000 (1850) →
~10,000 (1900) → ~25,000 active peer-reviewed (2020, Scopus).

## (b) Growth models

### Bornmann & Mutz 2015 (JASIST 66:2215) — cited-references 1650–2012
Phases: <1%/yr to mid-1700s; 2–3%/yr to interwar; 8–9%/yr postwar (doubling ~9 yr —
reference-based, overstates output growth). WoS publication-based 1980–2012: 2.96%/yr.

### Bornmann, Haunschild & Mutz 2021 (HSSC 8:224) — publications 1665–2018
Four databases jointly (Dimensions from 1665, MA, WoS, Scopus), latent piecewise model.
- Overall: **4.10%/yr, doubling 17.3 yr**.
- Segments: 1675–1809: **2.87%/yr** (doubling 24.5y) · 1815–1881: **5.62%/yr** (12.6y) ·
  1881–1952: **3.78%/yr** (18.7y) · post-1952: **5.08%/yr** (14.0y).
- UK 8-segment analysis: 1780–1805 7.73%; 1805–1844 5.93%; 1844–~1920s 3.70%;
  1940–48 **2.62%** (WWII slowdown); 1948–59 6.80%; 1959–83 8.65%; post-1983 6.42%.
- Note: segment rates extracted via search summaries, cross-confirmed ≥2 sources each.

### Reconstruction recipe [derived] (piecewise exponential, calibrated)

| Segment | g/yr | Calibration | Endpoint |
|---|---|---|---|
| 1665–1750 | 1.0% | N(1665)=130 | ~300 (1750) |
| 1750–1800 | 2.1% | N(1750)=300 | ~850 (1800) |
| 1800–1900 | 3.5% | N(1800)=850 (fits RS Catalogue ~780k total) | ~28k (1900) |
| 1900–1945 | 3.2% (dips 1914–18, 1940–48 to ~2.6%) | N(1900)=28k | ~115k (1945) |
| 1945–1975 | 5.1% | N(1945)=115k | ~530k (1975) |
| 1975–2000 | 3.0% | N(1975)=530k | ~1.12M (2000) ✓ Björk |
| 2000–2025 | 4.3% | N(2010)=2.0M | ~3.5–3.8M (2025) |

## (c) Cumulative totals

| Date | Cumulative articles | Source |
|---|---|---|
| 1800 | ~25–30k | [derived]; Kronick 1976 |
| 1900 | ~0.8–0.9M | Royal Society Catalogue 1800–1900 |
| 1961 | ~6M | de Solla Price, *Little Science, Big Science* 1963 |
| 2009 | ~50M | Jinha 2010, *Learned Publishing* 23(3):258 |
| 2014 | ≥114M scholarly docs on web | Khabsa & Giles 2014, PLOS ONE 9(5):e93949 |
| 2025 | ~110–120M journal articles [derived]; 271M OpenAlex works | Jinha extrapolation; OpenAlex |

## (d) Pre-1665 context — Buringh & van Zanden 2009 (J. Econ. Hist. 69:409)

Manuscript copies, W. Europe (per century): 6th 13k · 7th 11k · 8th 44k · 9th 202k ·
10th 137k · 11th 212k · 12th 769k · 13th 1.76M · 14th 2.75M · 15th 5.0M.
Printed copies: 1454–1500 ~12.6M · 16th c. ~217M · 17th c. ~518M · 18th c. ~1,030M.
(Per-century cells reproduce OWID/Wikipedia renderings of Tables 1–2; aggregates verified.)

## (e) Caveats

1. "A paper" is not a stable unit — counts at the same year differ up to 3× by document-type
   definition (Scopus S&E vs. citable vs. Dimensions vs. OpenAlex "works").
2. Pre-1900 per-year database counts measure digitization, not output; growth *rates* are
   more robust than levels (Dimensions holds only 288 articles for 1798 vs. ~850 implied).
3. "Doubling every 9 years" is reference-based (2015 paper); publication growth is ~4.1%/yr.
4. Recent years are indexing-lag undercounts; mega-journal/paper-mill growth inflates
   post-2016 counts (Hanson et al. 2024: 6.7%/yr 2016–22).
5. Pre-1665 numbers count book *copies* in Western Europe only, not papers.

## Key citations

- Bornmann & Mutz 2015, JASIST 66(11):2215. doi:10.1002/asi.23329
- Bornmann, Haunschild & Mutz 2021, Humanit Soc Sci Commun 8:224. nature.com/articles/s41599-021-00903-w
- de Solla Price 1961 *Science Since Babylon*; 1963 *Little Science, Big Science*
- Jinha 2010, Learned Publishing 23(3):258. doi:10.1087/20100308
- Björk, Roos & Lauri 2009, Information Research 14(1):391
- Buringh & van Zanden 2009, J. Econ. Hist. 69(2):409. doi:10.1017/S0022050709000837
- Mabe 2003, Serials 16(2):191 · Thelwall & Sud 2022, QSS 3(1):37 · Hanson et al. 2024, QSS 5(4):823
- Alperin et al. 2024 arXiv:2404.17663 · Priem et al. 2022 arXiv:2205.01833
- Khabsa & Giles 2014, PLOS ONE 9(5):e93949 · Kronick 1976 · NSB S&E Indicators (ncses.nsf.gov)
- Royal Society, Catalogue of Scientific Papers 1800–1900
