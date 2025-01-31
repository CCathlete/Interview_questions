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
