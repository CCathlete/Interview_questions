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
    - Do I need to validate the input (nums, k)?
        - No it's ok.
    - Should I return as many numbers as possible if k > len(set(nums))?
        - Yes, sounds good.
    Should I return None if k <= 0 or nums = []?
        - Yes.

4. Example + Approach:
    - nums = [1,1,1,2,2,3], k = 2
    - We're going to create a frequency hash map (dictionary).
    - Each number in nums will be a key and the frequency will 
    be the value.
    - Then, we will add the k most frequent numbers to the result and return it.
    -->
    freq_map = {1: 3, 2: 2, 3: 1}
    => Result = [1, 2]
"""
from typing import Union, Callable

# Helpers.


def create_freq_map(nums: list[int]) -> dict[int, int]:
    """Gets an array (list) of integers and returns a hash map
    with the frequency of each number in nums.
    """
    freq_map: dict[int, int] = {num: 0 for num in nums}
    for num in nums:
        freq_map[num] += 1

    return freq_map


def decending_values_from_dict(di: dict[int, int]) -> list[tuple[int, int]]:
    """Gets a dictionary and returns it as a list of key,
    value pairs from the pair with largest value to smallest."""

    sorted_tuples: list[tuple[int, int]] = sorted(
        # list[tuple[int,int]]
        di.items(),
        # A rule to apply on each item from items.
        # The sorting is of these keys.
        # item[0] = dict key(num), item[1] = dict value(freq).
        key=lambda item: item[1],
        reverse=True,
    )

    return sorted_tuples


# Implementation.


def top_k_frequent(
    nums: list[int],
    k: int,
) -> Union[list[int], None]:
    """Gets nums: list[int] and k: int and returns the
    most frequent numbers from top most to kth."""
    empty_input: bool = nums == []
    bad_k: bool = k <= 0

    if empty_input or bad_k:
        return None

    # Considering the case k > len(nums).
    k = min(k, len(set(nums)))

    freq_map: dict[int, int] = create_freq_map(nums)
    descending_tuples: list[tuple[int, int]] = decending_values_from_dict(freq_map)

    num: Callable = lambda i: descending_tuples[i][0]

    result: list[int] = [num(i) for i in range(k)]

    return result


# Test case skeleton.


class TestCase:
    """Frame for a test case."""

    name: str
    nums: list[int]
    k: int
    expected: list[int]

    def __init__(
        self,
        name: str,
        nums: list[int],
        k: int,
        expected: list[int],
    ) -> None:
        self.name = name
        self.nums = nums
        self.k = k
        self.expected = expected


# Main fonction.


def main() -> None:
    """Entry point to the program."""
    cases: list[TestCase] = [
        TestCase(
            name="Happy case.",
            nums=[1, 1, 1, 2, 2, 3],
            k=2,
            expected=[1, 2],
        ),
        TestCase(
            name="Happy case 2.",
            nums=[1, 1, 1, 2, 3, 3],
            k=3,
            expected=[1, 3, 2],
        ),
        TestCase(
            name="k > len(set(nums)), number of unique values.",
            nums=[1, 1, 1, 2, 3, 3],
            k=5,
            expected=[1, 3, 2],
        ),
    ]

    for case in cases:
        print(f"Running case: {case.name}")
        print(f"Params: nums = {case.nums}, k = {case.k}")
        print(f"Expected: {case.expected}")
        print(f"Result: {top_k_frequent(case.nums, case.k)}")
        print()


if __name__ == "__main__":
    main()
