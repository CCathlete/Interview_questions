# https://leetcode.com/problems/top-k-frequent-elements/description/

"""
1. Rephrasing:
    - We're given an array of int and an int k.
    - We need to return all of the most frequent numbers from 
    the most frequent to the k frequent.
    - i.e. if k = 1 we return the most frequent, 
    if k = 2 we return the most frequent and the second most 
    frequent, etc.

2. Complexity:
    - Time:
    - Space:
    
3. Follow up questions:
    - 

4. Example + Approach:

"""

# Helpers.

# Implementation.


def top_k_frequent(inp: object) -> object:
    """_summary_"""


# Test case skeleton.


class TestCase:
    """Frame for a test case."""

    name: str
    expected: object
    inp: object

    def __init__(
        self,
        name: str,
        inp: object,
        expected: object,
    ) -> None:
        self.name = name
        self.inp = inp
        self.expected = expected


# Main fonction.


def main() -> None:
    """Entry point to the program."""
    cases: list[TestCase] = [TestCase(name="Happy case.", inp=[], expected=[])]

    for case in cases:
        print(f"Running case: {case.name}")
        print(f"Expected: {case.expected}")
        print(f"Result: {top_k_frequent(case.inp)}")


if __name__ == "__main__":
    main()
