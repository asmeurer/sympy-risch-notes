# Per-case results

One JSON object per line, one line per corpus case.  All runs: 5 s per
case unless noted, `--isolate` (forked child killed at the limit),
oracle verification with 20 s per instantiation.  The `cls` field is
the classification (`SOLVED`, `partial`, `NIE`, `timeout`, `error:*`,
`CLAIMS-NE`); where present, `v`/`check` is the oracle verdict
(`DERIV-OK`, `DERIV-OK-PROVEN`, `DERIV-OK-SPLIT`, `WRONG`, ...) and
`s`/`secs` the per-case seconds.

| file | run | corpus slice | branch @ sympy commit | corpus commit | cases |
|---|---|---|---|---|---|
| `branch-cmp-heb-master.jsonl` | [branch comparison](../branch-comparison-2026-08-19.md), 2026-08-19 | hebisch, first 2,000 | master `bd4ee7fc6d` | `b0a1083` | 2,000 |
| `branch-cmp-heb-rdecancel.jsonl` | same | same | risch-rde-cancellation `bf88623d8e` (pre-fix) | `b0a1083` | 2,000 |
| `branch-cmp-heb-algebraic.jsonl` | same | same | risch-algebraic `757fa4fa7e` | `b0a1083` | 2,000 |
| `branch-cmp-blake-algebraic.jsonl` | same | blake, `--filter risch-algebraic`, first 1,500 | risch-algebraic `757fa4fa7e`, `algebraic=True` | `b0a1083` | 1,500 |
| `pretip-blake-abort-census.jsonl` | [run log, Blake sweep](../README.md#blake-algebraic-pseudo-elliptic-hyperelliptic-nested-radicals) | blake, all cases, plain `risch_integrate(f, x)`, 8 s | risch-algebraic, pre-relaxation tip (before `15e76e361e`) | — | 3,154 |
| `mitbee-risch-master.jsonl` | [MIT Bee](../mit-bee-2026-08-21.md), 2026-08-21 | mit_bee_official, `--filter risch-attemptable`, indefinite | master `8454607030`, engine `risch` | `4d1aacc` | 263 |
| `mitbee-risch-rdecancel.jsonl` | same | same | risch-rde-cancellation `d7dafa43c1`, engine `risch` | `4d1aacc` | 263 |
| `mitbee-risch-algbranch.jsonl` | same | same | risch-algebraic `3b072169b7`, engine `risch` | `4d1aacc` | 263 |
| `mitbee-rischalg-algbranch.jsonl` | same | same | risch-algebraic `3b072169b7`, engine `risch_algebraic` | `4d1aacc` | 263 |

The Hebisch and Blake files are compact (`cls`, `i`, `s`, `v`): the full
integrand/answer/expected strings are in the raw runner output, not
kept here.  The `pretip-blake-abort-census.jsonl` rows carry `cls`,
`index` and `integrand` only.

Not carried over from the gist (available in its
[frozen copy](https://gist.github.com/asmeurer/b4b8ceb7c364566f5e7a3d07ce133300)
and in this repository's import commit): the 2026-08-10/11 pre-fix Rubi
results (`zz-archive-rubi-alg-results.jsonl`, 3.4 MB, 40% of whose
SOLVED entries Run 12 found wrong), the Run 3 transcendental A/B
(`zz-archive-rubi-trans-wt-{master,rdecancel}.jsonl`), the Run 1 raw log
and the rendered per-chapter Rubi tables.
