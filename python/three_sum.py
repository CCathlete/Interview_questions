# https://leetcode.com/problems/3sum/

"""
    1. Rephrasing: 
        We get an array and we want to return all of the three number combinations that their sum is zero.

    2. We'll use a sorted array to reduce the number of scans required, reducing the complexity.

    3. We'll scan the array from both directions to reduce the number of loops (multiple pointers approach).

    4. Since the array is sorted, we know that as we progress we've collected all possible triplets.

    5. We want to skip duplicates, so we#ll skip the current value we're scanning if it's the same as the previous one.
"""