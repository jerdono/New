# Research memo — Long-run human interconnectedness: data & composite design

> Compiled by a web-research pass on 2026-07-06. OWID GitHub data mirrors were directly
> readable; values from those files are exact as published. "≈" = corroborated from
> literature summaries, not re-extracted from primary tables.

## (a) Component data

### 1. Trade openness (world exports+imports, % of world GDP)
OWID "Globalization over 5 centuries" world series (Estevadeordal, Frantz & Taylor 2003
bounds 1500–1820; Klasing & Milionis 2014 "own estimates" 1870–1949; PWT/World Bank after).

| Year | Openness % | Series |
|---|---|---|
| 1500 | 0.5–2.25 | EFT bounds |
| 1600 | 1.25–5.5 | EFT |
| 1700 | 1.25–5.5 | EFT |
| 1820 | 2.0–9.5 | EFT |
| 1870 | 17.57 | K&M |
| 1900 | 24.36 | K&M |
| 1913 | 29.01 | K&M (first-globalization peak) |
| 1929 | 18.75 | K&M |
| 1938 | 12.96 | K&M (interwar collapse) |
| 1949 | 16.35 | K&M |
| 1950 | 19.87 | PWT |
| 1973 | 29.61 | PWT (regains 1913 level) |
| 2000 | 47.30 | PWT/WB |
| 2008 | 61.49 | PWT/WB (pre-GFC peak) |
| 2019 | 55.85 | PWT/WB |
| 2022 | 63 | WB WDI |

O'Rourke & Williamson (NBER w7632): no intercontinental price convergence before the
1820s — the "globalization big bang" is the 1820s.

### 2. Urbanization (world urban share, %) — HYDE 3.1 / UN WUP (exact)
10000 BCE 0.0 · 5000 BCE 0.1 · 1 CE 1.0 · 500 1.7 · 1000 2.6 · 1500 4.1 · 1600 5.2 ·
1700 5.1 · 1800 7.3 · 1900 16.4 · 1950 29.1 · 2000 46.8 · 2007 49.6 (urban majority) ·
2023 56.6 · 2024 57.9

### 3. Morris Social Development Index (validation only)
Four traits (energy capture, largest city, war-making, information), West 2000 = 906;
agrarian "hard ceiling" ≈ 43 points (Rome ~1 CE, Song ~1100 both stall there).
Measures leading-core capability, includes war-making → used for validation, not as a
component.

### 4. KOF Globalisation Index (1970–2023)
42 variables, 1–100. World average ≈38 (1970) → ≈44 (1990) → 61.3 (2023). Post-1970
validation series only.

### 5. Communication
World literacy (OWID exact): 1820 12.0 · 1870 18.7 · 1900 21.4 · 1930 32.5 · 1950 36.0 ·
1990 74.9 · 2000 81.0 · 2010 84.2 · 2023 87.4.
Internet users % (ITU/OWID): 1990 0.05 · 2000 6.7 · 2005 15.6 · 2010 28.4 · 2015 39.9 ·
2020 60.1 · 2023 69.2 · 2025 73.6.

### 6. Population substrate (OWID exact) & rationale
10000 BCE 4.5M · 5000 BCE 19.2M · 1000 BCE 110.5M · 1 CE 232M · 1000 323M · 1500 503M ·
1700 595M · 1800 983M · 1870 1.34B · 1913 1.80B · 1950 2.49B · 1973 3.92B · 2000 6.17B ·
2023 8.09B.
Muthukrishna & Henrich 2016 (Phil Trans R Soc B 371:20150192): innovation emerges from the
"collective brain" — sociality (population × interconnectedness), transmission fidelity,
cultural variance; literacy/radio/internet as interconnectivity multipliers.

### 7. Inequality (penalty)
Milanovic, Lindert & Williamson 2011: pre-industrial extraction ratios average ≈75% of the
feasible maximum (Rome 14 CE Gini ≈ 39 at income near subsistence). Global citizen-level
Gini (Bourguignon & Morrisson 2002; Milanovic 2024): 0.50 (1820) → 0.61 (1910) → 0.64
(1950) → ~0.657 (1980) → ~0.69–0.70 plateau (1988–2005) → 0.60–0.62 (2018, first sustained
fall since industrialization).

## (c) Composite: Human/Global Interconnectedness Index

**HII(t) = S^0.20 · T^0.25 · C^0.25 · U^0.15 · E^0.15**, rescaled so present = 100.

| Component | Definition | Normalization |
|---|---|---|
| S | log of connected world population | log(N/10⁴)/log(N_now/10⁴) |
| T | world trade openness | ÷70pp, cap 1 |
| C | 0.6·literacy + 0.4·internet share | 0–1 |
| U | world urban share | ÷100 |
| E | 1−global Gini (1820–); 1−0.9·extraction ratio (pre-1820) | 0–1 |

Geometric mean makes components complements — no dimension can buy the score alone.
Classical Greece: world urban ~1%, trade <1%, literacy <10%, extraction near frontier
⇒ HII ≈ 5/100. Illustrative values (2023=100): 1000 BCE ≈3.6 · 1 CE ≈4.9 · 1000 ≈5.6 ·
1500 ≈10.2 · 1820 ≈21.9 · 1870 ≈35.4 · 1913 ≈45.7 · 1950 ≈48.2 · 1973 ≈62.9 · 2000 ≈79.1 ·
2008 ≈89.2 · 2023 = 100. Reproduces the known narrative (1820s take-off, 1913 peak,
interwar stall, post-1950 surge, post-2008 flattening); tracks KOF post-1970.

## (d) Caveats

1. Pre-1500 T and C are educated floors (T=0.1–0.5%, literacy 1–2%); report pre-1500 HII
   with ±50% bands.
2. Morris SDI decimals are secondary-source approximations.
3. Splices at 1870/1950 (trade), 1800/1950 (population), ~1950 (literacy), 1820/1990
   (inequality) — ratio-link at overlaps.
4. Global Gini mixes within/between-country inequality; pre-1820 ER proxy rests on ~14
   societies.
5. K&M PPP-vs-market choice moves interwar openness up to 38%.
6. KOF cannot be spliced in (relative 1–100); validation only.
7. Post-1990 acceleration is partly definitional via the internet term; telegraph/telephone/
   mail densities for 1850–1990 would be the highest-value extension.

## (b) Citations

- Klasing & Milionis 2014, J. Int. Econ. 92(1):185. doi:10.1016/j.jinteco.2013.10.010
- Estevadeordal, Frantz & Taylor 2003, QJE 118(2); OWID globalization-over-5-centuries
- O'Rourke & Williamson 2002, "When Did Globalization Begin?", NBER w7632
- Federico & Tena-Junguito, World Trade Historical Database (CEPR/VoxEU)
- Klein Goldewijk et al. 2017 (HYDE 3.2), ESSD 9:927
- Morris 2013, *The Measure of Civilization*, Princeton UP
- Gygli, Haelg, Potrafke & Sturm 2019, Rev. Int. Organizations 14:543 (KOF)
- OWID literacy (van Zanden et al. 2009 / UNESCO); Buringh & van Zanden 2009
- ITU via World Bank IT.NET.USER.ZS
- Maddison Project Database 2020 (Bolt & van Zanden)
- Muthukrishna & Henrich 2016, Phil Trans R Soc B 371:20150192
- Milanovic, Lindert & Williamson 2011, Econ. J.; NBER w13550
- Bourguignon & Morrisson 2002, AER 92(4):727
- Milanovic 2024, "The three eras of global inequality, 1820–2020" (Stone Center)
