"""
1. Rephrasing:
    - We get an array of unique numbers, sorted (ascending) but rotated (cyclic shift) by some unknown number.
    - This means that only one half of the array is ascending.

2. Complexity:
    - Time: O(log n)
    - Space: O(1)

3. Folow up questions:
    - Do I know the rotation number?
        - No.
    - Do I know the length of the array?
        - In Python and Java, the length is stored as a parameter of the list so getting it is O(1).
        

4. Example + Approach:
    - nums = [(L)4, 5, 6, (M)7, 8, 1, (R)2], target = 1
    -->
    - Left half is sorted, so we'll check if target is in it.
    - Target is not in the left half so know that target is in the right half.
    - We're "dumping" the left half and left with:

    - nums = [(L)8, (M)1, (R)2]
    nums[middle] = 1 = target.
    - Done, returning middle = 5 (we're not really dumping the array, just changing the bounds so original indices stay).
"""

# Helper functions / Normalisation.


# Implementation.


def search_rotated_sorted_array(
    nums: list[int],
    target: int,
) -> int:
    """Binary search on a ROTATED sorted array.

    Args:
        nums (list[int]): Sorted ascending array.
        target (int): The number we want to find.

    Returns:
        int: The index of target if it's in nums, (-1) otherwise.
    """
    value_not_found: int = -1
    left: int = 0
    right: int = len(nums) - 1

    while left <= right:
        # Floor division.
        middle: int = (left + right) // 2
        if nums[middle] == target:
            return middle
        # Left half is sorted.
        if nums[left] <= nums[middle]:
            # Target in left half.
            if nums[left] <= target < nums[middle]:
                right = middle - 1
            # Target in right half, so left boundary is one after middle.
            else:
                left = middle + 1
        # Right half is sorted.
        else:
            # Target in right half.
            if nums[middle] < target <= nums[right]:
                left = middle + 1
            # Target in left half, so right boundary is one before middle.
            else:
                right = middle - 1

    return value_not_found


# Test cases.


class Test_Case:
    name: str
    nums: list[int]
    target: int
    expected_result: int

    def __init__(self, name: str, nums: list[int], target: int, expected_result: int):
        self.name = name
        self.nums = nums
        self.target = target
        self.expected_result = expected_result


# Main function


def main() -> None:
    test_cases: list[Test_Case] = [
        Test_Case(
            name="Happy case.",
            nums=[4, 5, 6, 7, 8, 1, 2],
            target=1,
            expected_result=5,
        ),
        Test_Case(
            name="Empty array.",
            nums=[],
            target=1,
            expected_result=-1,
        ),
    ]

    for case in test_cases:
        print(f"Running {case.name}")
        print(f"Target: {case.target}")
        print(f"Nums: {case.nums}")
        print(
            f"Result: {search_rotated_sorted_array(
            case.nums,
            case.target,
            )}"
        )
        print(f"Expected result: {case.expected_result}")


if __name__ == "__main__":
    main()
