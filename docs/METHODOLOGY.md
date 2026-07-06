# Methodology — The Expanding Human Toolkit

**Version 1.0 · built 2026-07-06 · pipeline: `src/build_dataset.py` · research memos: `docs/research/`**

This document specifies, for each plotted series, exactly how every value was constructed,
what it rests on, and how wrong it could be. The guiding principle is the one an
interdisciplinary reconstruction team would use: *never present interpolation as
measurement*. Every year-value carries a provenance flag, and the chart renders the flags
(solid = annual source data underlies the curve; dashed = model reconstruction between
literature anchors; dots = the anchors themselves; bands = uncertainty/definitional range).

## 0. What "annual granularity over all of history" can honestly mean

A yearly series from 10,000 BCE is not an observation set — no such records exist.
What *can* be built rigorously is:

1. **Observed segments** where the scholarly literature provides annual (or near-annual)
   accounts: chemical compounds 1800–2015 (Reaxys, via Llanos et al. 2019), material flow
   accounts 1900–2024 (Krausmann/UNEP-IRP), publication databases ~1900–2025, and
   post-1950 component series for the interconnectedness index.
2. **Anchored reconstructions** elsewhere: literature anchor points joined by published
   growth models or by geometric interpolation, with wide uncertainty bands.

The full annual table (`data/series_annual.csv`, 12,027 rows) therefore has yearly
*resolution* everywhere but yearly *information* only where flagged `observed`.

## 1. Series: Substances & materials known (cumulative count)

**Definition.** Distinct chemical substances/materials known to humanity; from 1800 the
operational definition is "compounds reported in the scientific literature" (the Reaxys
compound sense used by Llanos et al.), which we extend backward to "distinct materials in
documented use".

**1800–2015 (observed).** Llanos, Leal, Luu, Jost, Stadler & Restrepo (2019, *PNAS*
116(26):12660) find new-compound reports growing at a stable ≈4.4 %/yr across the whole
period (undisturbed by both World Wars), cumulating to **14,341,955** distinct compounds
by 2015. We reproduce that model:

    N_new(t) = N₀ · 1.044^(t−1800),  N₀ chosen so Σ_{1800}^{2015} N_new = 14,341,955
    (⇒ N₀ ≈ 58 new compounds in 1800)
    C(t) = C(1800) + Σ N_new

The paper's three regimes (proto-organic to 1860, organic 1861–1980, organometallic
1981–) are changes in year-to-year *variance*, not in the mean rate, so a single-rate
reproduction is faithful to its central finding.

**2016–2026 (reconstructed).** The 4.4 %/yr trend extended; upper band widened to 2×
because the definitional gap to registry counts grows (see below).

**Pre-1800 (reconstructed, anchored).** Geometric interpolation through historians'
order-of-magnitude anchors (bounds in parentheses): Paleolithic material kit ≈15 (10–30);
Bronze Age ≈25 (15–40) — the seven metals of antiquity, bronze, glass, pigments;
Pliny the Elder's era ≈60 (30–100); ~1500 CE ≈120 (60–250); 1700 ≈350 (150–800);
Lavoisier 1789 (33 "simple substances", 23 true elements) era ≈700 (300–1500);
1800 ≈1,000 (300–2,000; Berzelius tabulated ~2,000 compounds by 1818). These are
*illustrative censuses of named lists*, not bibliometry — hence the dashed line and wide
bands.

**The definitional spread (hollow dots).** CAS REGISTRY counts *registered substances*
(incl. polymers, mixtures, protein/DNA sequences): 50 M (2009-09-07) → 100 M (2015-06) →
150 M (2019-05-08) → 250 M (2021-04) → >290 M (2024–26, ~15,000 new/day). PubChem holds
119 M unique structures (2024); Reaxys ~268–353 M substances. The ~20× gap between
"literature compounds" and "registry substances" is definitional, not a contradiction;
the chart shows CAS milestones as context dots rather than splicing incompatible
definitions into one line.

**Elements cross-check** (in `data/payload.json`): cumulative known elements 9 (antiquity)
→ 13 (medieval) → 23–34 (1800, criterion-dependent) → 84 (1899) → 118 (2016) — a *finite*
curve, deliberately not conflated with the combinatorially open compound space.

## 2. Series: Global material extraction (Gt/yr)

**Definition.** Global domestic extraction of biomass, fossil energy carriers, metal ores
and non-metallic minerals — the standard economy-wide material flow accounting (ew-MFA)
boundary. This answers the user-brief's "(combined?) quantities".

**1900–2024 (observed).** Spliced canonical series, log-interpolated between published
values: Krausmann et al. (2009, *Ecol. Econ.* 68:2696): ~7 Gt/yr (1900) → ~59 Gt (2005),
with Depression-era dip; Krausmann et al. (2018, *Glob. Environ. Change* 52:131):
~89 Gt (2015); UNEP IRP Global Material Flows Database / Schandl et al. (2024,
*J. Ind. Ecol.*): ~92 Gt (2017) → ~105 Gt (2024). Overlap years reconciled to the later
vintage. Note: the sources publish annual accounts; our curve interpolates their
published anchor values, so year-to-year wiggles below the anchor density are smoothed.

**Pre-1900 (reconstructed, anchored ranges).** Population × sociometabolic per-capita
rates (Fischer-Kowalski & Haberl: hunter-gatherer ≈0.5–1 t/cap/yr; agrarian ≈3–6;
industrial ≈15–25): 1500 ≈2.0 (1.4–2.9) Gt/yr; 1700 ≈2.6 (1.8–3.6); 1800 ≈4.8 (3–7);
1850 ≈6.2 (4–9); deep-time values scale with population (10,000 BCE ≈0.003 Gt/yr).
Cross-checks: coal and pig-iron/steel production statistics; HANPP biomass series
(Krausmann et al. 2013, *PNAS* 110:10324: 6.9 → 14.8 PgC/yr over 1910–2005).

**Context (not plotted):** accumulated anthropogenic mass crossed living biomass at
≈1.1 Tt in 2020 ± 6 yr (Elhacham et al. 2020, *Nature* 588:442), from ~35 Gt in 1900.

## 3. Series: Research publications per year

**Definition.** Journal-article-type scholarly publications worldwide. "A paper" is not a
stable unit: at 2020, Scopus S&E articles ≈3.0 M, "citable documents" ≈4.2 M, Dimensions
articles ≈4.7 M, OpenAlex "works" ≈10.2 M. The plotted line tracks the *article* sense;
the band spans the definitional spread (×0.55 to ×1.9).

**Model.** Piecewise exponential, seeded at ~100 items/yr in 1665 (*Philosophical
Transactions* + *Journal des Sçavans*), with segment rates from the growth-of-science
literature (Bornmann, Haunschild & Mutz 2021, *Humanit. Soc. Sci. Commun.* 8:224 —
overall 4.10 %/yr, doubling 17.3 yr; segments 1675–1809: 2.87 %, 1815–1881: 5.62 %,
1881–1952: 3.78 %, post-1952: 5.08 %; WWII slowdown 2.62 %/yr 1940–48; Mabe 2003 journal
growth 3.46 %/yr; Hanson et al. 2024: 6.7 %/yr 2016–22), then passed through a smooth
log-space correction so it exactly hits the hard calibration counts:

| Year | Calibration | Source |
|---|---|---|
| 1665 | ~100/yr | founding volumes |
| 1800 | ~850/yr | backcast of Royal Society *Catalogue of Scientific Papers* (~780 k papers for 1800–1900) |
| 1850 | ~5,500/yr | same catalogue, 3.5 %/yr |
| 1900 | ~30,000/yr | catalogue endpoint; ~10,000 journals (Price) |
| 1950 | ~200,000/yr | segment model, WWII-adjusted |
| 2006 | 1.35 M/yr | Björk, Roos & Lauri 2009 |
| 2010 | 2.0 M/yr | NSB *S&E Indicators* (Scopus) |
| 2022 | 3.3 M/yr | NSB *S&E Indicators* |

Provenance: `observed` from 1900 (dense annual database coverage; model calibrated to
it), `reconstructed` 1665–1899 (pre-1900 database levels measure digitization, not
output). Cumulative cross-checks: ~0.8–0.9 M articles by 1900; ~50 M by 2009 (Jinha
2010); ~110–120 M by 2025 (extrapolation; OpenAlex holds 271 M works of all types).

## 4. Series: Global Interconnectedness Index (GII, 0–100, 2026 = 100)

**Motivation.** The user brief asks for "total group interconnectedness": Greek
city-states low, high-inequality societies low, low global cohesion / resource sharing /
specialization low. No published series does this over the full span (Morris's Social
Development Index measures leading-core *capability* and includes war-making; the KOF
Globalisation Index starts 1970). We therefore construct a documented composite grounded
in the collective-brain literature (Muthukrishna & Henrich 2016, *Phil. Trans. R. Soc. B*
371:20150192: innovation scales with sociality = population size × interconnectedness,
transmission fidelity, and breadth of participation).

**Formula.**

    GII(t) = 100 · [ S^0.20 · T^0.25 · C^0.25 · U^0.15 · E^0.15 ](t) / [same](2026)

| Component | Meaning | Normalization | Main sources |
|---|---|---|---|
| S | network scale | log(pop/10⁴)/log(pop₂₀₂₆/10⁴) | HYDE 3.3, Gapminder, UN WPP |
| T | exchange density | world (X+M)/GDP ÷ 70 pp, cap 1 | Estevadeordal-Frantz-Taylor 2003; Klasing & Milionis 2014; PWT/WB |
| C | communication reach | 0.6·literacy + 0.4·internet share | van Zanden et al./UNESCO (OWID); ITU |
| U | agglomeration/specialization | world urban share ÷ 100 | HYDE 3.1; UN WUP |
| E | equality of participation | 1 − global Gini (1820–); 1 − 0.9·extraction ratio (pre-1820) | Bourguignon & Morrisson 2002; Milanovic 2024; Milanovic-Lindert-Williamson 2011 |

The **geometric mean makes the components complements**: a society cannot buy a high
score on one dimension. This delivers the brief's desiderata mechanically — classical
Greece (world urban ~1 %, trade <1 % of GDP, literacy <10 %, extraction ratio near the
feasible frontier) scores ≈5/100 despite its cultural brilliance; the 1913–1950
de-globalization/War/Depression era appears as a visible plateau; rising within-era
inequality lowers E and the score.

**Key component anchors** are tabulated in `docs/research/interconnectedness.md`
(trade: 17.6 % in 1870, 29.0 % peak 1913, 13.0 % trough 1938, 61.5 % peak 2008;
urbanization: 1.0 % at 1 CE → 4.1 % (1500) → 16.4 % (1900) → 57.9 % (2024); literacy:
12 % (1820) → 87.4 % (2023); internet: 0 (1989) → 73.6 % (2025); global Gini: 0.50
(1820) → 0.70 plateau (1988–2005) → ~0.61 (2018)).

**Resulting trajectory** (validated against the research memo's independent hand
computation): 1 CE ≈ 4.6 · 1000 ≈ 5.3 · 1500 ≈ 8.9 · 1820 ≈ 21 · 1870 ≈ 33 · 1913 ≈ 45 ·
1950 ≈ 48 · 1973 ≈ 61 · 2000 ≈ 77 · 2008 ≈ 87 · 2026 = 100. Post-1970 the shape tracks
the KOF world average (partly by shared inputs). Pre-1500 values carry ±50 % bands
(components are educated floors); 1500–1820 ±35 %; 1820–1950 ±15 %; after 1950 ±8 %.

**This series is an index we constructed** — labeled as such everywhere it appears. Its
value is ordinal shape, not the third decimal. Weight perturbations of ±0.05 do not
change the ordinal history (memo, §c).

## 5. Provenance taxonomy & uncertainty

| Flag | Meaning | Drawn as |
|---|---|---|
| `observed` | an annual (or near-annual) published record underlies the curve; our line reproduces or interpolates it | solid 2 px |
| `anchored` | a literature anchor point | dot with surface ring |
| `reconstructed` | model/geometric interpolation between anchors | dashed, 85 % opacity |

Bands are low–high envelopes: source bounds where published (EFT trade bounds, MLW
extraction ratios, sociometabolic rate ranges, pre-1800 substance-count ranges),
definitional spread where that dominates (publications ×0.55–×1.9; substances upper band
→ registry sense), and stated percentage envelopes for the GII.

## 6. Known limitations (read before citing)

1. **Units are definition-dependent.** "Substance", "paper", "material" each have ≥2
   live definitions differing by 2–20×; we plot one consistently and band the rest.
2. **Pre-1800 anchors are order-of-magnitude.** No Reaxys of antiquity exists; Pliny and
   Lavoisier's lists are proxies for "documented knowledge".
3. **Smoothing below anchor density.** Between published values the curves are smooth;
   real year-to-year variance (wars, depressions) is only represented where the sources
   quantify it (e.g., WWII publication slowdown, 1930s materials dip, interwar trade
   collapse).
4. **The GII is a constructed index.** Component splices (trade 1870/1950; literacy
   ~1950; inequality 1820) create level uncertainty absorbed into the bands; the
   pre-1820 equality term rests on ~14 societies (MLW 2011).
5. **Web-research provenance.** Primary PDFs were often gateway-blocked during the
   research pass; figures were cross-corroborated across ≥2 independent sources where
   possible and flagged in `docs/research/*.md` otherwise. Before academic reuse,
   re-verify single-source items against the primary tables listed there.
6. **Recent years are provisional.** Publication counts 2023–25 are indexing-lag
   undercounts; 2025–26 materials and substances values are short trend extensions.

## 7. Bibliography (primary quantitative sources)

- Llanos, Leal, Luu, Jost, Stadler & Restrepo (2019). *PNAS* 116(26):12660. doi:10.1073/pnas.1816039116
- CAS milestone announcements: ScienceDaily 2009-09-10; PR Newswire 2011, 2015; C&EN 97(22) 2019, 99(17) 2021; cas.org/cas-data/cas-registry
- PubChem statistics (NAR 53(D1):D1516); Elsevier Reaxys product documentation
- Lavoisier (1789), *Traité élémentaire de chimie*; ACS National Historic Chemical Landmarks
- Krausmann, Gingrich, Eisenmenger, Erb, Haberl & Fischer-Kowalski (2009). *Ecol. Econ.* 68(10):2696. doi:10.1016/j.ecolecon.2009.05.007
- Krausmann, Lauk, Haas & Wiedenhofer (2018). *Glob. Environ. Change* 52:131. doi:10.1016/j.gloenvcha.2018.07.003
- Krausmann et al. (2013). *PNAS* 110(25):10324 (HANPP). doi:10.1073/pnas.1211349110
- UNEP International Resource Panel, *Global Resources Outlook* 2019 & 2024; Schandl et al. (2024) *J. Ind. Ecol.* doi:10.1111/jiec.13593; materialflows.net
- Elhacham, Ben-Uri, Grozovski, Bar-On & Milo (2020). *Nature* 588:442. doi:10.1038/s41586-020-3010-5
- Fischer-Kowalski & Haberl (2007–2011), sociometabolic regimes. *Hum. Ecol. Rev.* 18(2); *J. Ind. Ecol.* doi:10.1111/j.1530-9290.2008.00065.x
- Bornmann & Mutz (2015). *JASIST* 66(11):2215. doi:10.1002/asi.23329
- Bornmann, Haunschild & Mutz (2021). *Humanit. Soc. Sci. Commun.* 8:224. doi:10.1057/s41599-021-00903-w
- de Solla Price (1961) *Science Since Babylon*; (1963) *Little Science, Big Science*
- Royal Society, *Catalogue of Scientific Papers 1800–1900*; Kronick (1976)
- Björk, Roos & Lauri (2009). *Information Research* 14(1):391
- Jinha (2010). *Learned Publishing* 23(3):258. doi:10.1087/20100308
- Mabe (2003). *Serials* 16(2):191; Thelwall & Sud (2022) *QSS* 3(1):37; Hanson et al. (2024) *QSS* 5(4):823
- Khabsa & Giles (2014). *PLOS ONE* 9(5):e93949; Priem, Piwowar & Orr (2022) arXiv:2205.01833
- NSB, *Science & Engineering Indicators* (NCSES)
- Buringh & van Zanden (2009). *J. Econ. Hist.* 69(2):409. doi:10.1017/S0022050709000837
- Estevadeordal, Frantz & Taylor (2003). *QJE* 118(2); Klasing & Milionis (2014). *J. Int. Econ.* 92(1):185
- O'Rourke & Williamson (2002). NBER w7632; Federico & Tena-Junguito, World Trade Historical Database
- Klein Goldewijk et al. (2017), HYDE 3.2. *ESSD* 9:927; UN World Urbanization Prospects
- Morris (2013). *The Measure of Civilization*, Princeton UP (validation only)
- Gygli, Haelg, Potrafke & Sturm (2019). *Rev. Int. Org.* 14:543 (KOF; validation only)
- Muthukrishna & Henrich (2016). *Phil. Trans. R. Soc. B* 371:20150192
- Milanovic, Lindert & Williamson (2011). *Econ. J.*; Bourguignon & Morrisson (2002). *AER* 92(4):727; Milanovic (2024), Stone Center WP
- Maddison Project Database 2020 (Bolt & van Zanden); Our World in Data compilations (population, literacy, trade, urbanization, internet)
