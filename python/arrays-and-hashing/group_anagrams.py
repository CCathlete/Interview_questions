# https://leetcode.com/problems/group-anagrams/description/

"""
1. Rephrasing:
    - We're given a list of strings.
    - We need to group all anagrams of a same word in one list
    and return a list of all of the lists we've created.

2. Complexity:
    - Time: O(m * n), m = len(strs), n = max(len(str))
    - Space: O(m)

3. Follow up questions:
    - Should I return an empty list if strs = []?
        - Yes.
    - Should I include special characters or only letters?
        - Special characters is ok.
    - If strs = [""], should I return an empty list?
        - Yes.
    - If strs = ["one_str"] should I return [["one_str"]]?
        - Yes.

4. Example + Approach:
    - strs = ["cat", "act", "kata", "bing", "gnib", "boogie"]
    --> [["cat", "act"], ["kata"], ["bing", "gnib"], ["boogie]]
    - We'll create a list of frequency maps, each map
    corresponding to a string from str with the same index. 
    - For every two equal maps, we'll add the strings with the
    same index to the same group (list).
"""


# Helpers.
def create_freq_map(s: str) -> dict[str, int]:
    """Creates a frequency map for each character in s.

    Args:
        s (str): A string.

    Returns:
        dict[str, int]: {char: freq for char in s}
    """
    if not s or s == "":
        return {}

    freq_map: dict[str, int] = {char: 0 for char in s}

    for char in s:
        freq_map[char] += 1

    return freq_map


# Implementation.
def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Gets a list of strings and returns the list of grups
    of anagrams."""

    freq_maps: list[dict[str, int]] = [create_freq_map(s) for s in strs]

    def find_group(i: int, s: str) -> list[str]:
        """Gets a string s and its index in strs, i and
        compares the corresponding frequency map with all
        other frequency maps. All corresponding strings are
        then groups to a list and the list is returned."""
        anagrams: list[str] = [s]

        j: int = i + 1
        # If we find equal freq maps it means s should be in the current group.
        while j < len(strs):
            if freq_maps[i] == freq_maps[j]:
                anagrams.append(strs[j])
                strs[j] = ""
            j += 1

        return anagrams

    groups: list[list[str]] = [find_group(i, s) for i, s in enumerate(strs) if s != ""]

    return groups


# Test case skeleton.


class TestCase:
    """Frame for a test case."""

    name: str
    strs: list[str]
    expected: list[list[str]]

    def __init__(
        self,
        name: str,
        strs: list[str],
        expected: list[list[str]],
    ) -> None:
        self.name = name
        self.strs = strs
        self.expected = expected


# Main function.
def main() -> None:
    """Entry point to the program."""

    test_cases: list[TestCase] = [
        TestCase(
            "Happy case.",
            ["cat", "act", "kata", "bing", "gnib", "boogie"],
            [["cat", "act"], ["kata"], ["bing", "gnib"], ["boogie"]],
        ),
    ]

    for case in test_cases:
        print(f"Running case: {case.name}")
        print(f"strs: {case.strs}")
        print(f"Expected: {case.expected}")
        print(f"Result: {group_anagrams(case.strs)}")


if __name__ == "__main__":
    main()
