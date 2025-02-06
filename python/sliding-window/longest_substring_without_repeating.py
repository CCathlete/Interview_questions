# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

"""
1. Rephrasing:

2. Complexity
    - Time:
    - Space:

3. Follow up Q:
    - Should I validate the input?
        - No need.
    - Should I return 0 if the  input string is empty?
        - Yes.

4. Example + Approach:
"""


# Imports.
# Helpers.
def valid_input(s: str) -> bool:
    """Checks that s is a srting and not empty."""
    empty_string: bool = s == ""
    wrong_type: bool = isinstance(s, str)

    return not (empty_string or wrong_type)


# Implementation.
def length_of_longest_non_repeat(s: str) -> int:
    """Gets a string s and returns the length of the longest
    substring with no repeating letters.
    """
    longest_sub: str = s
    max_len: int = 0

    return max_len


# Test case skeleton.
class TestCase:
    """Frame for a test case."""

    name: str
    s: str
    expected: int

    def __init__(
        self,
        name: str,
        s: str,
        expected: int,
    ):
        self.name = name
        self.s = s
        self.expected = expected


# Main function.
def main() -> None:
    """Entry point to the program."""
    cases: list[TestCase] = [
        TestCase(
            "Happy case.",
            "aghhhthttoosdosdosod_abcdefg",
            6,
        ),
    ]

    for case in cases:
        print()
        print(f"Running case: {case.name}")
        print(f"expected: {case.expected}")
        print(f"Result: {length_of_longest_non_repeat(case.s)}")


if __name__ == "__main__":
    main()
