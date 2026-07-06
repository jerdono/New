# Research memo — Growth of the known chemical space (antiquity → 2026)

> Compiled by a web-research pass on 2026-07-06. Primary-source full texts were often
> gateway-blocked; figures were obtained via search-index synthesis of the cited sources.
> Flags below are preserved from the research pass.

## (a) Anchor-point table: cumulative distinct substances/materials known

| Period / Year | Cumulative substances known (estimate) | Low–high bound | Basis / citation |
|---|---|---|---|
| Paleolithic | Handful of natural materials (stone, ochre, bone, fiber, shell, clay, hide) | ~5–20 | Qualitative; history-of-materials surveys (Ashby; no quantitative census exists) |
| Neolithic (~8000 BCE) | ~10–20 recognized materials (adds fired ceramic, dyes, native copper, gold) | ~10–30 | Copper working ~6000–5000 BCE; native gold ~9000 BCE |
| Bronze Age (~3000 BCE) | 7 metals of antiquity + bronze (first deliberate alloy) + glass (~3500 BCE) + pigments | ~15–30 | "Metals of antiquity" standard classification; Forbes, *Studies in Ancient Technology* |
| Classical antiquity (Pliny, ~77 CE) | Several dozen named metals/minerals/pigments in *Naturalis Historia* XXXIII–XXXVII | ~30–100 | No rigorous count exists; informal historians' estimate |
| Medieval/alchemical (~1000–1600) | Mineral acids, sal ammoniac, alcohol, distillates; zinc/arsenic/antimony/bismuth distinguished | ~40–80 | Weakest-sourced anchor; illustrative only |
| Lavoisier 1789 | 33 "simple substances" (23 true elements) | 23–33 | *Traité élémentaire de chimie*; ACS Landmark |
| ~1800 (compounds) | Low hundreds–low thousands; Berzelius (1818) tabulated ~2,000 compounds | ~300–2,000 | Synthesized range; consistent with Llanos et al. 1800 seed |
| 2015 (literature compounds) | 14,341,955 distinct compounds (Reaxys, 1800–2015) | — | Llanos et al. 2019 PNAS |
| 2024–2026 (registry sense) | CAS REGISTRY >290M substances (~204M organic/inorganic + 69M sequences); PubChem 119M unique compounds / 322M substance records (Sept 2024); Reaxys ~268–353M | 119M–353M | Definitional spread, not contradiction |

## (b) Llanos et al. (2019) growth parameters

Llanos, Leal, Luu, Jost, Stadler & Restrepo (2019). "Exploration of the chemical space and its
three historical regimes." *PNAS* 116(26):12660–12665. doi:10.1073/pnas.1816039116

- Dataset: Reaxys, 1800–2015: **14,341,955 distinct compounds**, 16,356,012 reactions.
- **New compounds/year grew at a stable ~4.4%/yr exponential** across the whole period,
  essentially undisturbed by both World Wars.
- Three regimes (change in year-to-year *variance*, not mean rate):
  1. Proto-organic, 1800–1860 (noisy exponential)
  2. Organic, 1861–1980 (variance drops after structural/valence theory)
  3. Organometallic, 1981–2015
- Reconstruction: N(t) ≈ N(1800)·1.044^(t−1800), normalized so Σ(1800–2015) ≈ 14.34M
  → N(1800) ≈ low tens/yr; ~10⁵–10⁶/yr by the 2010s.
- Caveat: exact per-year values live in the paper's figures; the reconstruction is an
  approximation from stated aggregate parameters.

## (c) CAS REGISTRY milestones

| Milestone | Date | Source |
|---|---|---|
| Registry launched | 1965 (experimental late 1964) | ACS Landmark; Weisgerber 1997 JASIS 48(4):349 |
| 3M substances | ~1975 | CAS/ACS historical material |
| 10M | 1990 | CAS History |
| ~25M | 2005 | CAS History |
| 40M | ~late 2008 | ScienceDaily 2009 |
| 50M | 2009-09-07 | ScienceDaily; EurekAlert |
| 60M | 2011-05-25 | PR Newswire 2011 |
| 70M | 2012-12-07 | knowledgespeak 2012 |
| 100M | 2015-06 | PR Newswire 2015; C&EN 93(28) |
| 150M | 2019-05-08 | C&EN 97(22) |
| 250M | 2021-04 | C&EN 99(17); CAS Insights |
| >290M (~15,000 new/day) | 2024–2026 | cas.org/cas-data/cas-registry |

## (d) Elements by era (cumulative count of known elements)

| Period | New | Cumulative |
|---|---|---|
| Antiquity → ~1400s | 13 | 13 |
| ~1400s → 1799 | 21 | 34 |
| 1800–1849 | 24 | 58 |
| 1850–1899 | 26 | 84 |
| 1900–1949 | 13 | 97 |
| 1950–1999 | 16 | 113 |
| 2000–present | 5 | 118 |

Cross-checks: Lavoisier 1789 = 23 true elements; ~49 by 1828; ~60–63 at Mendeleev 1869.
Phosphorus (Hennig Brand, 1669) = first element discovered by a named individual.

## (e) Caveats

1. "Substance" is not a fixed unit — literature-reported compounds (Llanos 14.3M) vs.
   registry entries incl. sequences/mixtures/polymers (CAS 290M+) differ by ~20×.
2. Elements (118, near-complete) and compounds (combinatorially open) are different curves.
3. Pre-1800 anchors are historians' order-of-magnitude estimates, not censuses.
4. Post-2010 registry growth partly reflects patent Markush disclosures and deposition
   practices, not purely newly synthesized substances.
5. The 1861/1980 regime boundaries mark variance changes, not rate changes.

## Sources

- Llanos et al. 2019, PNAS 116(26):12660. https://www.pnas.org/doi/10.1073/pnas.1816039116
- C&EN coverage: https://cen.acs.org/synthesis/Chemists-discovered-new-compounds-exponential/97/i25
- RSC Digital Discovery 1(5):568 (chemical space review): https://pubs.rsc.org/dd/article/1/5/568/311448/
- CAS History & Registry: https://www.cas.org/about/cas-history ; https://www.cas.org/cas-data/cas-registry
- CAS milestone press: ScienceDaily 2009-09-10; PR Newswire 2011-05-25 & 2015-06; C&EN 97(22), 99(17)
- PubChem statistics: https://pubchem.ncbi.nlm.nih.gov/docs/statistics ; NAR 53(D1):D1516
- Reaxys: https://www.elsevier.com/products/reaxys
- Lavoisier 1789 *Traité élémentaire de chimie*; ACS Landmark: https://www.acs.org/education/whatischemistry/landmarks/lavoisier.html
- Pliny, *Naturalis Historia* XXXIII–XXXVII (Perseus)
- Wikipedia: Timeline of chemical element discoveries; Metals of antiquity
- Weisgerber 1997, JASIS 48(4):349 (CAS Registry history)
