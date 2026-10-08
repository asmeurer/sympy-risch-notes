# sympy-risch-notes

Working notes for completing the Risch algorithm in
[SymPy](https://github.com/sympy/sympy) (`sympy/integrals/risch.py`,
`rde.py`, `prde.py` and friends), following Bronstein, *Symbolic
Integration I: Transcendental Functions*.  Plans, status, open
decisions, errata found in the book, and the logs of running the work
against large integration corpora.

These files started life as gists; they moved here on 2026-10-08
because the run logs outgrew what gists handle.  The gists stay up,
frozen, since sympy PRs link to them.

## Layout

| path | what |
|---|---|
| [docs/RISCH_PLAN.md](docs/RISCH_PLAN.md) | the plan and status for the transcendental case, phase by phase (Phases 0-4 done, Phase 5 hypertangent done through 5e, Phase 6 pending), plus the experimental algebraic track |
| [docs/RISCH_DECISIONS.md](docs/RISCH_DECISIONS.md) | decisions the work needs from Aaron, with the ones already taken marked |
| [docs/RISCH_ALGEBRAIC_PLAN.md](docs/RISCH_ALGEBRAIC_PLAN.md) | the branch-correctness plan for the algebraic (radical) experiment and its corpus testing, with the session notes of implementing it |
| [docs/BRONSTEIN_ERRATA.md](docs/BRONSTEIN_ERRATA.md) | errata for Bronstein's book found while implementing it |
| [runs/README.md](runs/README.md) | **current state**: each corpus x each branch, latest measurement, what is open, what has not been measured |
| [runs/](runs/) | the write-ups behind those numbers and the chronological run log |
| [runs/data/](runs/data/README.md) | per-case JSONL results |

## The branches

All on [asmeurer/sympy](https://github.com/asmeurer/sympy), stacked:

- `risch-gaps`, PR [sympy/sympy#30180](https://github.com/sympy/sympy/pull/30180)
  (merged): Phase 0, the correctness fixes.
- `risch-rde-cancellation`, PR [#30221](https://github.com/sympy/sympy/pull/30221):
  Phases 1-4, the remaining exp-log cases, and the principal-branch
  fixes.
- `risch-hypertangent`: Phase 5, tan/atan towers (stacked on
  rde-cancellation; no PR yet).
- `risch-algebraic`, draft PR [#30239](https://github.com/sympy/sympy/pull/30239):
  the experimental radicals-as-exp-log-towers mode (stacked on
  rde-cancellation).

The corpora and the runner are
[sympy/integration-test-suites](https://github.com/sympy/integration-test-suites).

## Updating

The `docs/` files are the working copies: the sympy checkout's untracked
`RISCH_*.md` / `BRONSTEIN_ERRATA.md` are symlinks into a clone of this
repository.  Commit and push in the same turn as any edit; see
[runs/README.md](runs/README.md#adding-a-run) for how to record a run.

## Frozen gists

- run logs: https://gist.github.com/asmeurer/b4b8ceb7c364566f5e7a3d07ce133300
  (also holds the pre-fix Rubi tables and raw results that were not
  carried over)
- RISCH_PLAN.md + RISCH_DECISIONS.md: https://gist.github.com/asmeurer/bed00aa257ef69b2688bbc9333da9a0d
- BRONSTEIN_ERRATA.md: https://gist.github.com/asmeurer/eb4c9d3e6253372d2b3e1bd4438721d3
- RISCH_ALGEBRAIC_PLAN.md: https://gist.github.com/asmeurer/5ad380f4ed1cdd573e6328ffd0d8a947

Much of the text here was written with AI assistance (Claude); the
measurements come from the runs described in each file.
