# https://leetcode.com/problems/container-with-most-water/description/

"""
1. Rephrasing:
    - We get a list of hights of vertical lines representing
    bucket sides.
    - We want to find the two line that would form a bucket
    with the most water.

2. Complexity:
    - Time: O(n)
    - Space: O(1)

3. Follow up questions:
    - Should I return 0 if the height list is empty?
        - Yes.
    - Should I validate the input?
        - No there's no need.

4. Example + Approach:
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    - We'll use two pointers to traverse the list from both
    directions (to not use nested loops).
    - Since we can't tilt the bucket, the volume of water is
    limited by the side with the lower height.
    - water = 
        (x_right - x_left) * min(height[right], hight[left])
    - We'll start from both ends of the array, so that
    (x_right - x_left) is maximal.
"""

# Imports.


# Helpers.


def valid_input(height: list[int]) -> bool:
    """Checks that height is the right type and not empty."""
    wrong_input_type: bool = not isinstance(height, list) and all(
        [isinstance(element, int) for element in height]
    )

    empty_list: bool = height == []

    if wrong_input_type or empty_list:
        return False

    return True


def water_area(
    left_side: tuple[int, int],
    right_side: tuple[int, int],
) -> int:
    """Gets (x1, y1) and (x2, y2) and returns
    delta(x) * min(y)
    """

    return (right_side[0] - left_side[0]) * min(left_side[1], right_side[1])


# Implementation.


def container_most_water(height: list[int]) -> int:
    """Gets a list of hights of vertical lines and calculates
    the maximum surface area that we can get from two lines.
    """
    if not valid_input(height):
        return 0

    left: int = 0
    right: int = len(height) - 1
    max_vol: int = water_area(
        (left, height[left]),
        (right, height[right]),
    )

    while left < right:
        water_left: int = water_area(
            (left + 1, height[left + 1]),
            (right, height[right]),
        )
        water_right: int = water_area(
            (left, height[left]),
            (right - 1, height[right - 1]),
        )

        # We keep the side that give the higher volume and move
        # the side that give the lower volume.
        if water_left >= water_right:
            right -= 1
            max_vol = max(max_vol, water_left)
        else:
            left += 1
            max_vol = max(max_vol, water_right)

    return max_vol


# Test case skeleton.


class TestCase:
    """Frame for a test case."""

    name: str
    height: list[int]
    expected: int

    def __init__(
        self,
        name: str,
        height: list[int],
        expected: int,
    ):
        self.name = name
        self.height = height
        self.expected = expected


# Main function.


def main() -> None:
    """Entry point to the program."""
    cases: list[TestCase] = [
        TestCase(
            "Happy case.",
            [1, 8, 6, 2, 5, 4, 8, 3, 7],
            49,
        ),
    ]

    for case in cases:
        print(f"Running case: {case.name}")
        print()
        print(f"Expected: {case.expected}")
        print(f"Result: {container_most_water(case.height)}")


if __name__ == "__main__":
    main()
