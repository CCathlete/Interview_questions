""" Write a function that finds the second largest number in a
given unsorted array in the most efficient way. What is the
efficiency of your solution? For example,
the outcome of [1,4,6,20,3,7] will be 7

1. Rephrasing:
	- We're given an array nums (unsorted), we want to find 
 the second largest number in the most efficient way.

2. Complexity:
	- Time: O(n).
    - Space: O(1).

3. Follow up Q:
	- Input check: only that nums != []

4. Example + Approach:
	- nums = [1,4,6,20,3,7], result = 7

"""

from sys import maxsize
from typing import Union

# Helpers.
# Implementation.


def second_largest(nums: list[int]) -> int:
    """
    Gets an array of int and returns the second largest number.
    """
    empty_nums: bool = nums == []
    not_enough_numbers: bool = len(nums) < 2

    if empty_nums or not_enough_numbers:
        raise ValueError("incorrect input")

    n: int = len(nums)
    left: int = 0
    right: int = n - 1
    first_max: int = -(maxsize + 1)  # Int equivalent to - inf.
    second_max: int = -(maxsize + 1)

    while left <= right:
        if nums[right] >= first_max:
            second_max = first_max
            first_max = nums[right]
        else:
            if nums[right] > second_max:
                second_max = nums[right]

        if nums[left] >= first_max:
            second_max = first_max
            first_max = nums[left]
        else:
            if nums[left] > second_max:
                second_max = nums[left]

        right -= 1
        left += 1

    return second_max


# Test case skeleton.
class TestCase:
    """
    Frame for a test case.
    """

    name: str
    nums: list[int]
    expected: Union[int, None]

    def __init__(
        self,
        name: str,
        nums: list[int],
        expected: Union[int, None],
    ) -> None:

        self.name = name
        self.nums = nums
        self.expected = expected

    # Main function.


def main() -> None:
    """
    Entry point to the program.
    """
    cases: list[TestCase] = [
        TestCase("Happy case.", [1, 4, 6, 20, 3, 7], 7),
        TestCase("Ascending order.", [10, 20, 30, 40], 30),
        TestCase("Descending order.", [-10, -20, -30, -40], -20),
        TestCase("Minimal size.", [1, 4], 1),
        TestCase("Big numbers.", [10000000, 900, 4000000000], 10000000),
        TestCase("Empty nums.", [], None),
        TestCase("Nums too small.", [1], None),
    ]

    for case in cases:
        print()
        print(f"Running case: {case.name}")
        print(f"Expected result: {case.expected}")
        try:
            print(f"Result: {second_largest(case.nums)}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
