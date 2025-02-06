""" Write a function that finds the second largest number in a
given unsorted array in the most efficient way. What is the
efficiency of your solution? For example,
the outcome of [1,4,6,20,3,7] will be 7

1. Rephrasing:
	- We're given an array nums (unsorted), we want to find 
 the second largest number in the most efficient way.

2. Complexity:
	- Time: O(n).
    - Space: O(1) (check).

3. Follow up Q:
	- Input check: only that nums != []

4. Example + Approach:
	- nums = [1,4,6,20,3,7], result = 7

"""

# Helpers.
# Implementation.


def second_largest(nums: list[int]) -> int:
    """
    Gets an array of int and returns the second largest number.
    """
    if nums == []:
        raise ValueError("nums can't be empty")

    n: int = len(nums)
    left: int = 0
    right: int = n - 1
    first_max: int = nums[0]
    second_max: int = nums[0]

    while left < right:
        if nums[left] <= nums[right]:
            left += 1
        if nums[right] >= first_max:
            first_max = nums[right]
        else:
            if nums[right] >= second_max:
                second_max = nums[right]

        if nums[left] >= nums[right]:
            right -= 1
        if nums[left] >= first_max:
            first_max = nums[left]
        else:
            if nums[left] >= second_max:
                second_max = nums[left]

    return second_max


# Test case skeleton.
class TestCase:
    """
    Frame for a test case.
    """

    name: str
    nums: list[int]
    expected: int

    def __init__(
        self,
        name: str,
        nums: list[int],
        expected: int,
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
    ]

    for case in cases:
        print()
        print(f"Running case: {case.name}")
        print(f"Expected result: {case.expected}")
        print(f"Result: {second_largest(case.nums)}")


if __name__ == "__main__":
    main()
