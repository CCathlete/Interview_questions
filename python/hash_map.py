# https://leetcode.com/problems/two-sum/

"""
    Solving the two sum problem using a hash map (dicionary in 
    py)
1. Rephrasing:
    - We're given an array of integers and a target (int).
    - We need to numbers that add up to target and return their indices.
    
2. Complexity:
    - Time: O(n).
    - Space: O(n).
    
3. Follow up questions:
    - What should I return if there are no compatible numbers?
        - Return an empty tuple.
    
4. Example + Approcah:
    - nums = [2, 7, 1, 15], target = 9
    --> returns (0, 1)

    - We'll use a hash map (dictionary) that stores each
    number as key and its index as value.
    - We'll iterate over nums, after creating the hash map
    and check if (target - num) is in the hash map. 
    - If it is, we can lookup both indices in O(1) time 
    and return them as a tuple.
"""


# Helpers.


# Implementation.


def sum_two_hashmap(
    nums: list[int],
    target: int,
) -> tuple[int, int]:
    """Gets a list of ints and a target and returns indices of
    two numbers that add up to the target or -1 if there are
    none.
    """
    hashmap: dict[int, int] = {nums[i]: i for i in range(len(nums))}

    for num in nums:
        difference: int = target - num
        if difference in hashmap:  # O(1) on average.
            return hashmap[num], hashmap[difference]

    return (-1, -1)


# Test case skeleton.


class TestCase:
    """A frame for each test case."""

    name: str
    nums: list[int]
    target: int
    expected: tuple[int, int]

    def __init__(
        self,
        name: str,
        nums: list[int],
        target: int,
        expected: tuple[int, int],
    ) -> None:
        self.name = name
        self.nums = nums
        self.target = target
        self.expected = expected


# Main function.


def main() -> None:
    """Entry point for the program."""
    test_cases: list[TestCase] = [
        TestCase(
            name="Happy case.",
            nums=[2, 7, 1, 15],
            target=9,
            expected=(0, 1),
        )
    ]

    for case in test_cases:
        print(f"Running case: {case.name}")
        print(f"Nums: {case.nums}")
        print(f"Target: {case.target}")
        print(f"Expected: {case.expected}")
        print(
            f"Result: {sum_two_hashmap(
                case.nums,
              case.target,
              )}"
        )


if __name__ == "__main__":
    main()
