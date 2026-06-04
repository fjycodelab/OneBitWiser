# Topic Queue

The next entry should take the first unchecked idea that can be explained
clearly and verified with a small standard-library experiment. New ideas may be
added when the queue gets short, but they must be precise enough to test.

## Algorithms And Data

- [x] Stable sorts can compose multi-key ordering.
- [ ] Binary search needs an explicit boundary convention.
- [ ] A heap guarantees the smallest item, not a fully sorted collection.
- [ ] Breadth-first search finds shortest paths in an unweighted graph.
- [ ] A set removes duplicates but does not preserve duplicate counts.
- [ ] A generator can process a sequence without storing the whole result.
- [ ] Memoization trades memory for repeated computation time.
- [ ] A prefix sum turns range-sum queries into constant-time lookups.

## Python And Representation

- [ ] Decimal text and binary floating-point values are not always identical.
- [ ] Mutable default arguments are shared across function calls.
- [ ] Shallow copies do not recursively copy nested objects.
- [ ] Dictionary insertion order and sorted key order are different ideas.
- [ ] Hash equality requires equal objects to have equal hashes.
- [ ] Unicode code points and user-perceived characters are not the same unit.
- [ ] Iterators are consumed as they are traversed.
- [ ] `is` tests identity while `==` tests equality.

## Systems And Reliability

- [ ] Atomic file replacement prevents readers from seeing a partial write.
- [ ] A monotonic clock is safer than wall time for measuring duration.
- [ ] Exponential backoff spreads repeated retries over time.
- [ ] Checksums detect accidental changes but do not prove authenticity.
- [ ] Compression can make repeated data dramatically smaller.
- [ ] Buffering changes when written data becomes visible.
- [ ] Path normalization is not the same as authorization.
- [ ] Idempotent operations can be retried without changing the final result.

## Networking And Text

- [ ] URL encoding distinguishes data from URL syntax.
- [ ] JSON numbers do not carry an integer-versus-float type promise.
- [ ] Newline conventions differ across operating systems.
- [ ] CSV needs quoting when a field contains a delimiter.
- [ ] A byte length and a character length can differ.
- [ ] Case folding is broader than lowercasing for caseless comparison.
