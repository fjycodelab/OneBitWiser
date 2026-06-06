# Binary Search Needs An Explicit Boundary Convention

## Claim

Binary search stays correct only if its interval meaning and its update rules
match. A half-open interval `[lo, hi)` and a closed interval `[lo, hi]` can
both work, but mixing their updates can skip the correct position.

## Why It Matters

Binary search bugs are often off-by-one bugs. The comparison step is usually
simple; the fragile part is deciding whether `hi` is inclusive or exclusive,
and then shrinking the interval in a way that matches that choice.

## Experiment

The experiment checks three lower-bound implementations against
`bisect.bisect_left`:

1. A correct half-open search over `[lo, hi)`.
2. A correct closed-interval search over `[lo, hi]`.
3. A mixed version that starts with `[lo, hi)` but updates `hi` as if it were
   inclusive.

It runs these functions on several fixed arrays and targets. The two consistent
versions always match `bisect_left`. The mixed version disagrees on specific
cases, which is the visible cost of an unclear boundary convention.

Run it:

```powershell
python experiments/2026/2026-06-06-binary_search_boundaries.py
```

## Observation

The correct half-open and closed-interval versions match `bisect_left` on every
case. The mixed version fails on these searches:

```text
[1, 3] x=2 expected=1 got=0
[1, 3] x=3 expected=1 got=0
[2, 4, 4, 7, 9] x=8 expected=4 got=3
[2, 4, 4, 7, 9] x=9 expected=4 got=3
```

The issue is not "binary search is hard" in the abstract. The issue is that
the loop invariants have to match the chosen interval convention all the way
through.

## Sources

- [Python Standard Library: `bisect`](https://docs.python.org/3/library/bisect.html)
- [Go Standard Library: `sort.Search`](https://pkg.go.dev/sort#Search)
