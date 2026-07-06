# The Expanding Human Toolkit — Materials, Knowledge, and Interconnectedness over History

An evidence-anchored, annually-resolved visualization of four long-run series:

1. **Known chemical space** — cumulative count of distinct substances/materials known to humanity (Paleolithic → CAS Registry era)
2. **Material throughput** — global material extraction, gigatonnes per year
3. **Scientific output** — research publications per year (1665 → present)
4. **Global Interconnectedness Index** — a documented composite (trade openness, urbanization, literacy/communication, effective connected population, inequality penalty)

## Structure

- `index.html` — the self-contained interactive chart (no external dependencies)
- `src/build_dataset.py` — reproducible pipeline: anchor points + published growth models → annual series
- `data/` — generated annual series (CSV + JSON) with per-point provenance flags
- `docs/METHODOLOGY.md` — full methodology, source citations, uncertainty discussion
- `docs/SOURCES.md` — complete bibliography

## Epistemic honesty

True *observed* annual data does not exist for most of history. Every point in the
dataset carries a provenance flag: `observed` (annual data from a primary source),
`anchored` (literature anchor point), or `reconstructed` (interpolated between anchors
via a published growth model). The chart renders these regimes distinctly. See
`docs/METHODOLOGY.md`.

## Reproducing

```bash
python3 src/build_dataset.py   # regenerates data/ and the JSON payload in index.html
```
