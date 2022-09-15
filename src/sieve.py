"""Computing primes."""


def sieve(n: int):
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0
    candidates = list(range(2, n + 1))
    primes = []

    while len(candidates) > 0:
        p = candidates[0]
        primes.append(p)
        candidates.remove(p)
        for number in candidates:
            if (number/p)%1 == 0:
                candidates.remove(number)
    return primes
