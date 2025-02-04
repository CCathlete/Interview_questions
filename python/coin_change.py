# https://leetcode.com/problems/coin-change/
"""
1. Rephrasing:
    - We're given a list of available coins and an amount we need to reach.
    - Our objective is to find the fewest number of coins 
    needed to reach the amount and return that number of coins.

2. Complexity:
    - Time: ?
    - Space: ?

3. Follow up questions:
    - We don't care about the actual coins I've used? only the 
    nuber of coins is relevant?
        - Yes.
    - What should I return if there are no available coins?
        - Return -1 like you can't reach the amount.
    - Do I need to validate the input (that nothing is str, 
    numbers are positive int etc.)?
        - No it's ok.

4. Example + Approach:
    - available_coins = [2, 5, 10, 20], amount = 50
    --> We'll use the highest coin possible in every step.
    - 20 + 20 + 20 > 50
    => 20 + 20 + 10 = 50 --> 3 coins.

    - We'll use a greedy algorithm in which we're adding the
    highest possible coint unless we're above the amount.
    - If we're above the amount, we'll try adding the second
    larget coin and so on.

"""

# Helpers.

# Implementation.


def coin_change(
    available_coins: list[int],
    amount: int,
) -> int:
    """Returns fewest num of coins needed to reach amount (using greedy algo)."""

    fewest_num_of_coins: int = 0
    total: int = 0

    i: int = 1
    while i <= len(available_coins):
        largest_coin: int = available_coins[-i]
        if total == amount:
            break
        if total + largest_coin <= amount:
            total += largest_coin
            fewest_num_of_coins += 1
        else:
            i += 1

    if total != amount:
        fewest_num_of_coins = -1

    return fewest_num_of_coins


# Test case skeleton.


class TestCase:
    """Frame for each test case."""

    name: str
    available_coins: list[int]
    amount: int
    expected: int

    def __init__(
        self,
        name: str,
        available_coins: list[int],
        amount: int,
        expected: int,
    ) -> None:
        self.name = name
        self.available_coins = available_coins
        self.amount = amount
        self.expected = expected


# Main function.


def main() -> None:
    """Entry point for the program."""
    test_cases: list[TestCase] = [
        TestCase(
            name="Happy case.",
            available_coins=[2, 5, 10, 20],
            amount=50,
            expected=3,
        )
    ]

    for case in test_cases:
        print(f"Running case: {case.name}")
        print(f"Available coins: {case.available_coins}")
        print(f"Amount: {case.amount}")
        print(f"Expected result: {case.expected}")
        print(
            f"Result: {coin_change(
            case.available_coins,
            case.amount,
            )}"
        )


if __name__ == "__main__":
    main()
