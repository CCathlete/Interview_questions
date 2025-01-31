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


# ---------------------------- Test cases ------------------------------


class TestCase:
    test_name: str
    arr: list[int]
    target: int

    def __init__(
        self, test_name: str,
        arr: list[int],
        target: int
        ) -> None:
        self.test_name = test_name
        self.arr = arr
        self.target = target


# --------------------------- Main function ----------------------------


def main() -> None:
    test_cases: list[TestCase] = [
        TestCase{
            "Happy case: One couple of numbers.",
            
        }
    ]


if __name__ == "__main__":
    main()
