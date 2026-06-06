"""Show that binary search needs a consistent boundary convention."""

from bisect import bisect_left


CASES = [
    ([1, 3], [0, 1, 2, 3, 4]),
    ([2, 4, 4, 7, 9], [0, 2, 3, 4, 5, 7, 8, 9, 10]),
]


def lower_bound_half_open(values, target):
    lo, hi = 0, len(values)
    while lo < hi:
        mid = (lo + hi) // 2
        if values[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def lower_bound_closed(values, target):
    lo, hi = 0, len(values) - 1
    answer = len(values)
    while lo <= hi:
        mid = (lo + hi) // 2
        if values[mid] >= target:
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return answer


def lower_bound_mixed(values, target):
    lo, hi = 0, len(values)
    while lo < hi:
        mid = (lo + hi) // 2
        if values[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo


def main():
    mismatches = []

    for values, targets in CASES:
        for target in targets:
            expected = bisect_left(values, target)
            assert lower_bound_half_open(values, target) == expected
            assert lower_bound_closed(values, target) == expected

            got = lower_bound_mixed(values, target)
            if got != expected:
                mismatches.append(
                    f"{values} x={target} expected={expected} got={got}"
                )

    assert mismatches == [
        "[1, 3] x=2 expected=1 got=0",
        "[1, 3] x=3 expected=1 got=0",
        "[2, 4, 4, 7, 9] x=8 expected=4 got=3",
        "[2, 4, 4, 7, 9] x=9 expected=4 got=3",
    ]

    print("correct_half_open == bisect_left on all cases")
    print("correct_closed == bisect_left on all cases")
    print("mixed_boundaries fail on:")
    for mismatch in mismatches:
        print(mismatch)


if __name__ == "__main__":
    main()
