# https://leetcode.com/problems/merge-sorted-array/

"""
1. Rephrasing:
    - We get two SORTED arrays (ascending) + the lengths of each.
    - we want to merge the second array into the first one, creating a merged array that is still sorted in ascending order.

2. Complexity analysis:
    - Time: O(n)
    - Space: O(n) (if we're not padding arr1 ahead of time)

3. Follow-up questions:
    - What if the arrays are not sorted?
        - Assume they are.
    - What if the arrays are not of the same type?
        - We'll use a helper function that'll convert them to the same type.

4. Example + approach:
        arr1=[1, 2, 3, 5, 10], m = 5
        arr2=[1, 3, 7, 15], n = 4
    We're going to replace the last element in arr1 with the closest SMALLER element in arr2.
    Then, we're going to append the number we took out of arr1.
        arr1=[1, 2, 3, 5, 7, 10]

"""

# ------------------ Data normalisation ----------------------


def bubble_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def enforce_type(arr1: list[int], arr2: list) -> tuple[list[int], list[int]]:

    if type(arr1[0]) != type(arr2[0]):
        if type(arr1[0]) == int:
            arr2 = [int(x) for x in arr2]
        elif type(arr1[0]) == float:
            arr2 = [float(x) for x in arr2]
        elif type(arr1[0]) == str:
            arr2 = [str(x) for x in arr2]
        else:
            raise ValueError("Unsupported type.")

    return arr1, arr2


# -------------------- Implementation ------------------------


def merge_arrays(
    arr1: list[int],
    arr2: list[int],
) -> list[int]:

    return arr1


# ---------------------- Test Cases --------------------------


class Test_Case:
    name: str
    arr1: list[int]
    arr2: list[int]
    expected_result: list[int]
    arr1_len: int
    arr2_len: int

    def __init__(
        self,
        name: str,
        arr1: list[int],
        arr2: list[int],
        expected_result: list[int],
    ) -> None:
        self.name = name
        self.arr1 = arr1
        self.arr2 = arr2
        self.expected_result = expected_result
        self.arr1_len = len(arr1)
        self.arr2_len = len(arr2)


# ---------------------- Main Function -----------------------


def main() -> None:
    test_cases: list[Test_Case] = [
        Test_Case(
            name="Happy Case",
            arr1=[1, 2, 3, 5, 10],
            arr2=[1, 3, 7, 15],
            expected_result=[1, 1, 2, 3, 3, 5, 7, 10, 15],
        ),
    ]

    for test_case in test_cases:
        print(f"arr1: {test_case.arr1}")
        print(f"arr2: {test_case.arr2}")
        print(f"expected_result: {test_case.expected_result}")
        print(f"result: {merge_arrays(test_case.arr1, test_case.arr2)}")


if __name__ == "__main__":
    main()
