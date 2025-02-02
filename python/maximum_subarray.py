# https://leetcode.com/problems/maximum-subarray/

"""
1. Rephrasing:
    - We get an array num and we need to find the subarray with the max sum of values.
    - We return the sum of that subarray.

2. Complexity Analysis:
    - Time: O(n)
    - Space: O(1)
    
3. Follow up questions:
    - Is the array sorted? Should I sort if not?
        - No need for soring it's ok. 
    - What should I return if the array is empty?
        - Return 0.
    - Should the sum be in absolute value?
        - No.
    - What should I return if the values are not numbers?
        - Raise an error.

4. Example + Approach:
    - We're treating the subarray as a sliding window.
    - We'll increase the window size as long as the sum of values in the window still increases after adding the next number. If it doesn't increase, it means that it's not the max sum since the next number itself is bigger. In this case we're resetting the window starting from the next number.
    --> i = 0
    nums = [(i)1, 5, 0, 9], max_sum = 1
    --> i = 1
    nums = [1, (i)5, 0, 9], max_sum = 6
    --> i = 2
    nums = [1, 5, (i)0, 9], max_sum = 6
    --> i = 3
    nums = [1, 5, 0, (i)9], max_sum = 15
"""

# ------------------ Normalisation ---------------------------


def validate_type(arr: list) -> None:
    if isinstance(type(arr[0]), int):
        raise ValueError("Array must be ot integers.")


# ------------------ Implementation --------------------------


def max_subarray(nums: list[int]) -> int:
    validate_type(nums)
    max_sum: int = 0
    for num in nums:
        max_sum_will_decrease: bool = max_sum + num < num

        max_sum = num if max_sum_will_decrease else max_sum + num

    return max_sum


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
            nums=[1, -5, 9, 0],
            expected_result=9,
        ),
    ]

    for test_case in test_cases:
        print(f"\nRunning test case: {test_case.name}")
        print(f"nums: {test_case.nums}")
        print(f"Expected result: {test_case.expected_result}")
        print(
            f"Result: {max_subarray(
            test_case.nums,
            )}",
        )


if __name__ == "__main__":
    main()
