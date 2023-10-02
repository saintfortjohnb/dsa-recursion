"""Produce new square adding two inputs squares.

Two simple squares can be added::

    >>> s1 = 0
    >>> s2 = 1

    >>> add(s1, s2)
    1

A simple square and a split square can be added::

    >>> s1 = 0
    >>> s2 = [1, 0, 1, 0]

    >>> add(s1, s2)
    [1, 0, 1, 0]

Two split squares can be added::

    >>> s1 = [0, 0, 0, 1]
    >>> s2 = [0, 1, 0, 1]

    >>> add(s1, s2)
    [0, 1, 0, 1]

Nested squares can be added::

    >>> s1 = [0, [1, 1, 1, [0, 0, 0, 0]], [0, 0, 0, 0], 1]
    >>> s2 = [1, [1, 0, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    >>> add(s1, s2)
    [1, [1, 1, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

Unevenly-nested squares can be added::

    >>> s1 = [0, [1, 1, 1, 0           ], [0, 0, 0, 0], 1]
    >>> s2 = [1, [1, 0, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    >>> add(s1, s2)
    [1, [1, 1, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    >>> s1 = [0, [1, 1, 1, 1                      ], [0, 0, 0, 0], 1]
    >>> s2 = [1, [1, 0, 1, [0, [0, 0, 0, 0], 1, 1]], [1, 0, 1, 0], 1]

    >>> add(s1, s2)
    [1, [1, 1, 1, [1, [1, 1, 1, 1], 1, 1]], [1, 0, 1, 0], 1]
"""


def upgrade_to_split(s):
    """Upgrade a simple square to a split square."""
    return [s, s, s, s]

def add(s1, s2):
    """Produce new split square adding two input squares."""

    # If both are simple squares
    if isinstance(s1, int) and isinstance(s2, int):
        return 1 if s1 == 1 or s2 == 1 else 0

    # If s1 is a simple square but s2 is split
    if isinstance(s1, int) and isinstance(s2, list):
        s1 = upgrade_to_split(s1)

    # If s2 is a simple square but s1 is split
    if isinstance(s2, int) and isinstance(s1, list):
        s2 = upgrade_to_split(s2)

    # Recursively add corresponding values of s1 and s2
    return [add(sub_s1, sub_s2) for sub_s1, sub_s2 in zip(s1, s2)]


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS; YOU'RE A RECURSION WIZARD!\n")

