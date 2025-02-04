# https://leetcode.com/problems/valid-anagram/

"""
1. Rephrasing:

2. Complexity:
    - Time: O(n)
    - Space: O(1), both dictionaries can have max of 26 keys.

3. Follow up questions:
    - Should I return False if one of the strings is empty?
        - Yes that's ok.
    - Should I validate the input?
        - No need, it's ok.
    - What if the strings have different lengths?
        - Return False.
    - Does the anagram have to be a real word?
        - No it's ok.

4. Example + Approach:
    - s = "cat", t = "act".
    - We'll count the frequency of each character both in s 
    and t.
    - We'll do that using hash maps (dictionaries), where the
    characters will be the keys and the frequencies would be 
    the values.
    --> 
    s_map = {'a': 1, 'c': 1, 't': 1}
    t_map = {'a': 1, 'c': 1, 't': 1}
    => s_map == t_map => True.

"""

# Helpers.


# Implementation.
def valid_anagram(s: str, t: str) -> bool:
    """Checks if s and t are anagrams."""
    different_length: bool = len(s) != len(t)
    empty_string: bool = s == "" or t == ""
    none_string: bool = s is None or t is None

    if different_length or empty_string or none_string:
        return False

    # Counting the frequencies of characters in s and t.
    s_map: dict[str, int] = {char: 0 for char in s}
    for char in s:
        s_map[char] += 1

    t_map: dict[str, int] = {char: 0 for char in t}
    for char in t:
        t_map[char] += 1

    return s_map == t_map


# Test case skeleton.
class TestCase:
    """Frame for a test case."""

    name: str
    s: str
    t: str
    expected: bool

    def __init__(
        self,
        name: str,
        s: str,
        t: str,
        expected: bool,
    ) -> None:
        self.name = name
        self.s = s
        self.t = t
        self.expected = expected


# Main function.
def main() -> None:
    """Entry point to the program."""
    test_cases: list[TestCase] = [
        TestCase(
            "Happy case.",
            "cat",
            "act",
            True,
        ),
        TestCase(
            "A bit less happy case.",
            "cat",
            "agt",
            False,
        ),
        TestCase(
            "Different lengths.",
            "cat",
            "satchel",
            False,
        ),
    ]

    for case in test_cases:
        print(f"Running case: {case.name}")
        print(f"s: {case.s}")
        print(f"t: {case.t}")
        print(f"Expected: {case.expected}")
        print(f"Result: {valid_anagram(case.s, case.t)}")


if __name__ == "__main__":
    main()
