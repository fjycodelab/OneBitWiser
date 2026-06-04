# Stable Sorts Can Compose Multi-Key Ordering

## Claim

A stable sort can build a multi-key ordering by sorting the least significant
key first, then sorting the more significant key.

## Why It Matters

Real data is often ordered by more than one field: group first, score second,
original arrival order last. A stable sort preserves the relative order of
records whose current keys compare equal, so separate sorting steps can work
together instead of undoing one another.

## Experiment

The experiment starts with records that have a team, a score, and an arrival
order. It compares two strategies:

1. Sort once with the tuple key `(team, -score)`.
2. Sort by descending score, then sort by team.

The second strategy works because Python's sort is stable. Records with the same
team keep the score order established by the first pass. Records tied on both
team and score keep their original arrival order.

Run it:

```powershell
python experiments/2026/2026-06-04-stable_sorts_compose.py
```

## Observation

Both strategies produce the same sequence:

```text
blue:90:ada, blue:90:linus, blue:80:grace, red:95:alan, red:80:barbara
```

The two blue records with score `90` remain in their original order, which is
the visible effect of stability.

## Sources

- [Python Sorting HOW TO: Sort Stability and Complex Sorts](https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts)
- [Python Library Reference: `list.sort`](https://docs.python.org/3/library/stdtypes.html#list.sort)
