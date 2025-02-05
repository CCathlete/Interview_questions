# https://leetcode.com/problems/valid-parentheses/
"""
1. Rephrasing:

2. Complexity:
    - Time:
    - Space:
    
3. Follow up questions:
    - Do I need to validate the input? Should I return False 
    if the input is not valid?
        - No need for validation, just return False in that 
        case.

4. Example + Approach:
    - s = "([{[{()}]}])"
    -->
    - Stripping ( ) from both sides.
    - s = "[{[{()}]}]"
    --> Repeating for every left-right pair ...
    - s = ()
    - If we encounter an incompatible pair, one side is empty
    or if the pairs are in thw wrong direction we return False.
"""

# Helpers.


# Implementation.
from collections import deque


def valid_parentheses(s: str) -> bool:
    """Getting a string of parentheses and checks if it
    consists of pairs in the right order (left-right).
    """
    left_side: set[str] = set("([{")
    right_side: set[str] = set(")]}")
    pairs: dict[str, str] = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    s_queue: deque[str] = deque(s)

    while s_queue:
        left: str = s_queue.popleft()
        try:
            right: str = s_queue.pop()
        # In case that there was an assymetrical number of
        # parentheses.
        except IndexError:
            return False

        wrong_order: bool = left not in left_side or right not in right_side
        mismatch: bool = pairs[left] != right

        if wrong_order or mismatch:
            return False

    return True


# Test case skeleton.
class TestCase:
    """Frame for a test case."""

    name: str
    s: str
    expected: bool

    def __init__(
        self,
        name: str,
        s: str,
        expected: bool,
    ) -> None:

        self.name = name
        self.s = s
        self.expected = expected


# Main function.
def main() -> None:
    """Entry point for the program."""
    test_cases: list[TestCase] = [
        TestCase(
            "Happy case",
            r"([{[{()}]}])",
            True,
        ),
    ]

    for case in test_cases:
        print(f"Running test: {case.name}")
        print(f"Input srting: {case.s}")
        print(f"Expected: {case.expected}")
        print(f"Result: {valid_parentheses(case.s)}")


if __name__ == "__main__":
    main()
