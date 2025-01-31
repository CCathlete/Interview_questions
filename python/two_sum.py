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
    Example:
    i = 0, arr: [3, 2, 1]
    j=0, [2, 3, 1] >> j=1, [2, 1, 3]
    i = 1, arr: [2, 1, 3]
    j=0, [1, 2, 3]
    i = 2
    do nothing.
    """
    for i in range(len(arr)):
        # We want range of len -i -1 because we take care of the last element in the interation before the last.
        for j in range(len(arr) - (i + 1)):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# -------------------------- Implementation ----------------------------


def two_sum(arr: list[int], target: int) -> list[int]:
    couple: list[int] = []

    return couple


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
