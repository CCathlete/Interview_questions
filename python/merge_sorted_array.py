# https://leetcode.com/problems/merge-sorted-array/

"""
1. Rephrasing:
    - We get two SORTED arrays (ascending) + the lengths of each.
    - we want to merge the second array into the first one, creating a merged array that is still sorted in ascending order.

2. Complexity analysis:
    - Time: O(n)
    - Space: O(n + m) (if we're not padding arr1 ahead of time, we're creating new cells depending on the length of the second array and appending to the first arry so we're also recreating it)

3. Follow-up questions:
    - What if the arrays are not sorted?
        - Assume they are.
    - What if the arrays are not of the same type?
        - We'll use a helper function that'll convert them to the same type.

4. Example + approach:
        arr1=[1, 2, 3, 5, 10], m = 5
        arr2=[1, 3, 7, 15], n = 4
    - We'll pad with zeros the first array to length of m + n.
    - We'll modify the new arr1 starting from the end.
    - We'll use three pointers:
        - i: starts at the last element of the original arr1
            (n-1) and moves to the left when the value it points to is moved to the right.
        - j: starts at the last element of the original arr2
            (m-1) and moves to the left.
        - k: starts at the last element of the new arr1
            (n+m-1) and moves to left at every iteration.
        -->
        arr1 = [1,2,3,5,(i)10, 0, 0, 0, (k)0]
        arr2 = [1, 3, 7, (j)15]

        --> 15 >= 10; j -= 1, k -= 1
        arr1 = [1, 2, 3, 5, (i)10, 0, 0, (k)0, 15]
        arr2 = [1, 3, (j)7, 15]

        --> 7 < 10; i -= 1, k -= 1
        arr1 = [1, 2, 3, (i)5, 10, 0, (k)0, 10, 15]
        arr2 = [1, 3, (j)7, 15]

        --> 7 >= 5; j -= 1, k -= 1
        arr1 = [1, 2, 3, (i)5, 10, (k)0, 7, 10, 15]
        arr2 = [1, (j)3, 7, 15]

        --> 3 < 5; i -= 1, k -= 1
        arr1 = [1, 2, (i)3, 5, (k)10, 5, 7, 10, 15] 
        arr2 = [1, (j)3, 7, 15]

        --> 3 >= 3; j -= 1, k -= 1
        arr1 = [1, 2, (i)3, (k)5, 3, 5, 7, 10, 15]
        arr2 = [(j)1, 3, 7, 15]

        --> 1 < 3; i -= 1, k -= 1
        arr1 = [1, (i)2, (k)3, 3, 3, 5, 7, 10, 15]
        arr2 = [(j)1, 3, 7, 15]

        --> 1 < 2; i -= 1, k -= 1
        arr1 = [(i)1, (k)2, 2, 3, 3, 5, 7, 10, 15]
        arr2 = [(j)1, 3, 7, 15]
        
        --> 1 >= 1; j -= 1, k -= 1
        arr1 = [(1, k)1, 1, 2, 3, 3, 5, 7, 10, 15]
        arr2 = (j)[1, 3, 7, 15]

        --> Done.
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


# Merges two sorted ascending arrays in-place into the first array. The merged array is also ascending.
def merge_arrays(
    arr1: list[int],
    arr2: list[int],
    n: int,
    m: int,
) -> list[int]:

    i: int = n - 1 if n > 0 else 0
    j: int = m - 1 if m > 0 else 0
    k: int = n + m - 1 if n + m > 0 else 0
    arr1 += [0] * (m)  # Padding arr1 with zeros to the right.

    while j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1

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
            name="Happy Case.",
            arr1=[1, 2, 3, 5, 10],
            arr2=[1, 3, 7, 15],
            expected_result=[1, 1, 2, 3, 3, 5, 7, 10, 15],
        ),
        Test_Case(
            name="arr1 shorter than arr2.",
            arr1=[1, 2],
            arr2=[1, 3, 3, 5, 7, 10, 15],
            expected_result=[1, 1, 2, 3, 3, 5, 7, 10, 15],
        ),
        Test_Case(
            name="arr1 is empty.",
            arr1=[],
            arr2=[1, 3, 7, 15],
            expected_result=[1, 3, 7, 15],
        ),
    ]

    for test_case in test_cases:
        print(f"Running test case: {test_case.name}")
        print(f"arr1: {test_case.arr1}")
        print(f"arr2: {test_case.arr2}")
        print(f"expected_result: {test_case.expected_result}")
        print(
            f"result: {merge_arrays(
                test_case.arr1,
                test_case.arr2,
                test_case.arr1_len,
                test_case.arr2_len,
                )}",
        )


if __name__ == "__main__":
    main()
