# https://leetcode.com/problems/product-of-array-except-self/

"""

1. Rephrasing:
    - We're given an array nums and we need to create an array 
    (list) answer so that answer[i] = 
    answer[0] * ... * answer[i-1] * answer[i+1] * ... 
    * answer[len(nums)-1]
    - Time complexity must be O(n).
    - We can't use the division operation.

2. Complexity:
    - Time: O(n).
    - Space: ?

3. Follow up questions:
    - Should I validate the input's type?
        - No it's ok.
    - Should I return [] if nums is empty?
        - Yes.

4. Example + Approach:
    - nums = [5, 4, 3, 2, 1]
    -->
        answer[0] = (4 * 3 * 2 * 1)
        answer[1] = (5) * (3 * 2 * 1)
        answer[2] = (5 * 4) * (2 * 1)
        answer[3] = (5 * 4 * 3) * (1)
        answer[4] = (5 * 4 * 3 * 2)
    - We're going to split each product to a product of all 
    numbers to the left of nums[i] and the same for the right 
    side.

    - To avoid a nested loop for multiplication, we'll use
    a rolling product as we iterate over the left sub array
    and calculate left_side_prod for all num[i] and then
    do the same for the right side.

    - Finally we'll do an element wise multiplication of 
    left_side_prod and right_side_prod.

"""


# Imports.
# Helpers.
# Implementation.
def prod_except_self(nums: list[int]) -> list[int]:
    """Gets an array num and calculates the non self product of each cell's value."""

    if nums == []:
        return []

    n: int = len(nums)

    def left_side_prod() -> list[int]:
        prods: list[int] = [1] * n

        # prods[0] = 1
        for i in range(1, len(nums)):
            # Starting from 1.
            prods[i] = prods[i - 1] * nums[i - 1]

        return prods

    def right_side_prod() -> list[int]:
        prods: list[int] = [1] * n

        # prods[n-1] = 1
        for i in range(n - 2, -1, -1):
            # Starting from n-2.
            prods[i] = prods[i + 1] * nums[i + 1]

        return prods

    left: list[int] = left_side_prod()
    right: list[int] = right_side_prod()

    return [left[i] * right[i] for i in range(n)]


# Test case skeleton.


class TestCase:
    """Frame for a test case."""

    name: str
    nums: list[int]
    expected: list[int]

    def __init__(
        self,
        name: str,
        nums: list[int],
        expected: list[int],
    ):
        self.name = name
        self.nums = nums
        self.expected = expected


# Main function.


def main() -> None:
    """Entry point for the program."""
    cases: list[TestCase] = [
        TestCase(
            "Happy case.",
            [5, 4, 3, 2, 1],
            [24, 30, 40, 60, 120],
        ),
        TestCase(
            "Happy case 2.",
            [5, 4, 3, 5],
            [60, 75, 100, 60],
        ),
    ]

    for case in cases:
        print(f"Running case: {case.name}")
        print(f"Nums: {case.nums}")
        print()
        print(f"Expected: {case.expected}")
        print(f"Result: {prod_except_self(case.nums)}")
        print()


if __name__ == "__main__":
    main()
