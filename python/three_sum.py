# https://leetcode.com/problems/3sum/

"""
    1. Rephrasing: 
        We get an array and we want to return all of the three number combinations that their sum is zero.

    2. We'll use a sorted array to reduce the number of scans required, reducing the complexity.

    3. We'll scan the array from both directions to reduce the number of loops (multiple reference approach).

    4. Since the array is sorted, we know that as we progress we've collected all possible triplets.

    5. We want to skip duplicates, so we'll skip the current value we're scanning if it's the same as the previous one.
"""


# A helper function that sorts the array Prior to our run.
def sort_array(arr: list[int]) -> list[int]:
    """Scans the array, putting the smallest number in the i'th position.

    Args:
        arr (list[int]): Array of numbers.

    Returns:
        list[int]: The sorted array.
    """
    # Creating a slice of the array starting at i.
    for i in range(len(arr)):
        # Scanning the slice for the smallest number, putting it in the i'th position.
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


def three_sum(arr: list[int]) -> list[list[int]]:
    triplets: list[list[int]] = []

    for i in range(len(arr) - 2):
        current_num: int = arr[i]
        # Handling duplicates for the first reference (i).
        if i > 0 and current_num == arr[i - 1]:
            continue

        # The unexplored section of arr.
        sub_array: list[int] = arr[i + 1 :]

        from_start: int = sub_array[0]
        from_end: int = sub_array[-1]
        sum: int = current_num + from_start + from_end

        # The array is sorted, so if both values are equal everything in between is equal or they are at the same index.
        while from_start != from_end:
            if sum < 0:
                from_start += 1
            elif sum > 0:
                from_end -= 1
            elif sum == 0:
                triplets.append([current_num, from_start, from_end])
                # Handling duplicates for the second reference (from_start).
                while (
                    from_start < from_end
                    and sub_array[from_start] == sub_array[from_start + 1]
                ):
                    # If we added from_start to a triplet, we want to skip all other steps that has that values in them. Since the array is sorted, all values of from_start are adjacent.
                    from_start += 1

                # Handling duplicates for the third reference (from_end).
                while (
                    from_end < from_end
                    and sub_array[from_end] == sub_array[from_end - 1]
                ):
                    # Similar to the previous while loop, we want to skip all other steps that has that values in them.
                    from_end -= 1

    return triplets


class Test_case:
    name: str
    arr: list[int]

    def __init__(self, name: str, arr: list[int]) -> None:
        self.name = name
        self.arr = arr


def main() -> None:
    test_cases: list[Test_case] = [
        Test_case(
            "Happy case: One triplet without any repetitions.",
            arr=[3, -1, 0, 1, 4],
        ),
        Test_case(
            "Case 1: one triplet, repeating numbers.",
            arr=[0, 1, -1, 3, 1],
        ),
        Test_case(
            "Case 2: two triplets, repeating numbers.",
            arr=[0, 1, -1, 3, 1],
        ),
        Test_case(
            "Edge case 1: Empty list.",
            arr=[],
        ),
        Test_case(
            "Edge case 2: No triplets.",
            arr=[1, 2, 3, 4, 5],
        ),
        Test_case(
            "Edge case 3: No triplets, one zero.",
            arr=[0, 2, 3, 4, 5],
        ),
    ]

    for test_case in test_cases:
        print(f"Running test case: {test_case.name}")
        print(f"Array: {test_case.arr}")
        print(f"Result: {three_sum(sort_array(test_case.arr))}")


if __name__ == "main":
    main()
