# https://leetcode.com/problems/climbing-stairs/
"""
1. Rephrasing:
    - We're given 2 types of step sizes: 1 and 2.
    - We want to find all possible combinations of steps that
    would sum up to n (total number of stairs).

3. Complexity:
    - Time: ?
    - Space: ?
    
3. Follow up questions:
    - What return value should I return if my input is n <= 0?
        - 0 is good.
    
    - Should I validate the input? let's say, convert n to int 
    in case it's a float or returning 0 if it's a string?
        - No need, assume it's valid.

4. Example + Approach:
    - n = 3.
    --> 
    1 + 1 + 1
    1 + 2
    2 + 1
    => 3 possible combinations.

    - We're going to use dynamic programming.
    - This means, we'll split the problem to repeatable sub 
    problems, and store the result of every sub problem.
    - The final result will be the result of the last sub
    problem.
    - If the number of ways to climb n steps is ways(n), 
    then the number of ways to climb 1 step is ways(1) and
    to climb 2 steps is ways(2).
    => 
    Since we have only the options of climbing 1 step and 2 steps, to reach the nth step we could take 2 steps from 
    n-2 or 1 setp from n-1.
    => ways(n) = ways(n-1) + ways(n-2)
"""

# Helpers:

# Implementation:


def climbing_stairs(n: int) -> int:
    """Implementation using dynamic programming.

    Args:
        n (int): Number of stairs.

    Returns:
        int: Number of ways to climb n stairs using 1 step and 2 steps.
    """
    if n <= 0:
        return 0

    # We want to use index n so size should be n+1.
    ways: list[int] = [0] * (n + 1)
    ways[0], ways[1], ways[2] = 0, 1, 2
    for i in range(3, n + 1):
        # We can reach i by taking 1 step from i-1 or 2 steps from i-2.
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]


# Test case skeleton:


class TestCase:
    """Structure of a single test case."""

    name: str
    n: int
    expected: int

    def __init__(
        self,
        name: str,
        n: int,
        expected: int,
    ) -> None:
        self.name = name
        self.n = n
        self.expected = expected


# Main function:


def main() -> None:
    """Entry point for the program."""
    test_cases: list[TestCase] = [TestCase(name="Happy case", n=4, expected=5)]

    for case in test_cases:
        print(f"Running test case: {case.name}")
        print(f"Number of stairs: {case.n}")
        print(f"Expected result: {case.expected}")
        print(f"Result: {climbing_stairs(case.n)}")


if __name__ == "__main__":
    main()
