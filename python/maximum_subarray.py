# https://leetcode.com/problems/maximum-subarray/

"""
1. Rephrasing:
    - We get an array num and we need to find the subarray with the max sum of values.
    - We return the sum of that subarray.

2. Complexity Analysis:
    - Time:
    - Space:
    
3. Follow up questions:
    - Is the array sorted?
        - No. 
    - What should I return if the array is empty?
        - Return 0.
    - Should the sum be in absolute value?
        - No.
    - What should I return if the values are not numbers?
        - Raise an error.

4. Example + Approach:
"""

# ------------------ Normalisation ---------------------------


def bubble_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# ------------------ Implementation --------------------------


def max_subarray(nums: list[int]) -> int:
    pass


# ------------------ Test cases ------------------------------


class Test_Case:
    name: str
    nums: list[int]
    expected_result: int

    def __init__(
        self,
        name: str,
        nums: list[int],
        expected_result: int,
    ) -> None:
        self.name = name
        self.nums = nums
        self.expected_result = expected_result


# ------------------ Main function ---------------------------


def main() -> None:
    test_cases: list[Test_Case] = [
        Test_Case(
            name="Happy case.",
            nums=[1, 5, 9, 0],
            expected_result=15,
        ),
    ]

    for test_case in test_cases:
        print(f"\nRunning test case: {test_case.name}")
        print(f"nums: {test_case.nums}")
        print(f"Expexted result: {test_case.expected_result}")
        print(
            f"Result: {max_subarray(
            bubble_sort(test_case.nums)),
            }",
        )


if __name__ == "__main__":
    main()
