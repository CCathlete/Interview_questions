# https://leetcode.com/problems/two-sum/

"""
    1. Rephrasing:
        We get an array and a number, the array has zero or one couple of numbers that their sum is equal to the input number.
        We want to return the indices of these two numbers.
        
    2. Approach:
        - We'll use a sorted array which we'll sort ahead of time.
        - We'll use two references and scan the array with them from both directions (to reduce complexity).
        - Since the array is sorted we'll progress left or right according to where we are relatively to the target number.
        - If we encounter a duplicaate we'll move one step to the right/left accorging to the reference we're moving.
"""

# -------------------------- Helper functions --------------------------


def bubble_sort(arr: list[int]) -> list[int]:
    """
    Why does it work?
    In every iteration of i, the (len - i)'th largest number is bubbled up to the rightmost position. At the 0 th iteration, the max number is bubbled to the end, etc.

    Example:
    i = 0, arr: [3, 2, 5, 10, 1], 0 <= j < len - 1 (=4)
    j=0, [*3, 2, 5, 10, 1] >> [*2, 3, 5, 10, 1]
    j=1, [2, *3, 5, 10, 1] >> [2, *3, 5, 10, 1] (do nothing)
    j=2, [2, 3, *5, 10, 1] >> [2, 3, *5, 10, 1] (do nothing)
    j=3, [2, 3, 5, *10, 1] >> [2, 3, ,5, *1, 10]

    i = 1, arr: [2, 3, 5, 10, 1], 0 <= j < len - 1 - i (=3)
    j=0, [*2, 3, 5, 10, 1] >> [*2, 3, 5, 10, 1] (do nothing)
    j=1, [2, *3, 5, 10, 1] >> [2, *3, 5, 10, 1] (do nothing)
    j=2, [2, 3, *5, 10, 1] >> [2, 3, *5, 10, 1] (do nothing)
    j=3, [2, 3, 5, *10, 1] >> [2, 3, 5, *1, 10]

    i = 2, arr: [2, 3, 5, 1, 10], 0 <= j < len - 1 - i (=2)
    j=0, [*2, 3, 5, 1, 10] >> [*2, 3, 5, 1, 10] (do nothing)
    j=1, [2, *3, 5, 1, 10] >> [2, *3, 5, 1, 10] (do nothing)
    j=2, [2, 3, *5, 1, 10] >> [2, 3, *1, 5, 10]

    i = 3, arr: [2, 3, 1, 5, 10], 0 <= j < len - 1 - i (=1)
    j=0, [*2, 3, 1, 5, 10] >> [*2, 3, 1, 5, 10] (do nothing)
    j=1, [2, *3, 1, 5, 10] >> [2, *1, 3, 5, 10]

    i = 4, arr: [2, 1, 3, 5, 10], 0 <= j < len - 1 - i (=0)
    j=0, [*2, 1, 3, 5, 10] >> [*1, 2, 3, 5, 10]
    """
    for i in range(len(arr)):
        # We want range of len -i -1 because we take care of the last element in the interation before the last.
        for j in range(len(arr) - (i + 1)):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# -------------------------- Implementation ----------------------------


def two_sum(arr: list[int], target: int) -> list[int]:
    index_couple: list[int] = []
    left_index: int = 0
    right_index: int = len(arr) - 1

    while left_index != right_index:
        sum: int = arr[left_index] + arr[right_index]
        if sum < target:  # We need to move to the right.
            left_index += 1
        elif sum > target:  # We need to move to the left.
            right_index -= 1
        else:  # sum == target
            return [left_index, right_index]

    raise ValueError("No couple of numbers in the array sums up to the target.")


# ---------------------------- Test cases ------------------------------


class TestCase:
    test_name: str
    arr: list[int]
    target: int

    def __init__(
        self,
        test_name: str,
        arr: list[int],
        target: int,
    ) -> None:

        self.test_name = test_name
        self.arr = arr
        self.target = target


# --------------------------- Main function ----------------------------


def main() -> None:
    test_cases: list[TestCase] = [
        TestCase(
            test_name="Happy case: One couple of numbers.",
            arr=[0, 10, 300, 1, 3, 7],
            target=1,
        ),
        TestCase(
            test_name="Edge case 1: Empty array.",
            arr=[],
            target=1,
        ),
        TestCase(
            test_name="Edge case 2: No matchine couple.",
            arr=[0, 10, 300, 1, 3, 7],
            target=50,
        ),
    ]

    for test_case in test_cases:
        print(f"Running test case: {test_case.test_name}\n")
        print(f"Array: {test_case.arr}\n")
        print(f"Target: {test_case.target}\n")
        print(f"Result: {two_sum(test_case.arr, test_case.target)}\n")


if __name__ == "__main__":
    main()
