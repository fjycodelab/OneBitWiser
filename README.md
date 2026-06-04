# One Bit Wiser

> A daily, executable proof of one small computing idea.

Most notes ask you to trust an explanation. This repository asks the explanation
to run.

Each entry contains:

- one precise claim;
- one small, deterministic Python experiment;
- a short explanation of what the result means;
- links to primary or official sources.

There are no empty commits and no filler notes. If an idea cannot be verified,
it is not published.

## Latest Proof

| Date | Idea | Entry | Experiment |
| --- | --- | --- | --- |
| 2026-06-04 | Stable sorts can compose multi-key ordering | [Read](entries/2026/2026-06-04-stable-sorts-compose.md) | [Run](experiments/2026/2026-06-04-stable_sorts_compose.py) |

## Run Every Experiment

```powershell
python scripts/verify.py
```

The experiments use only the Python standard library so they stay easy to run
and easy to inspect.

## Repository Map

- `entries/`: short explanations, observations, and sources.
- `experiments/`: executable evidence for each entry.
- `TOPICS.md`: the queue of ideas worth testing next.
- `CONTRIBUTING.md`: the quality bar for every daily update.

## The Point

Small facts become useful when they are testable. Over time, this repository
will become a compact library of computing ideas that can be learned in a few
minutes and verified in a few seconds.
