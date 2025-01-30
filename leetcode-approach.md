<h1>Common Problem-Solving Patterns</h1>
<h3>Here are some common patterns and techniques to keep in mind:</h3>

<h3>Two Pointers:</h3> Useful for problems involving arrays or strings (e.g., finding pairs, reversing strings).

<h3>Sliding Window:</h3> Ideal for subarray or substring problems (e.g., maximum sum, longest substring).

<h3>Binary Search:</h3> Efficient for searching in sorted arrays or solving optimization problems.

<h3>Depth-First Search (DFS) / Breadth-First Search (BFS):</h3> Essential for tree and graph traversal.

<h3>Dynamic Programming (DP):</h3> Useful for problems with overlapping subproblems (e.g., Fibonacci, knapsack).

<h3>Greedy Algorithms:</h3> Work for problems where local optima lead to a global optimum (e.g., scheduling, coin change).

<h3>Hash Maps:</h3> Great for counting, frequency analysis, or lookups.

<h3>Stack/Queue:</h3> Useful for problems involving order or levels (e.g., parentheses, BFS).

<h1>Example: Applying the Pattern</h1>
Let’s apply this approach to a classic LeetCode problem: Two Sum.

Problem Statement:
Given an array of integers nums and an integer target, return the indices of the two numbers that add up to the target.

Steps:
Understand the Problem:

Input: nums = [2, 7, 11, 15], target = 9

Output: [0, 1] (because nums[0] + nums[1] = 9)

Explore Examples:

Test case 1: nums = [3, 2, 4], target = 6 → [1, 2]

Test case 2: nums = [3, 3], target = 6 → [0, 1]

Break Down the Problem:

We need to find two numbers that add up to the target.

We can use a hash map to store numbers we've seen so far and their indices.

Choose an Approach:

Brute Force: Check every pair of numbers (O(n²) time).

Optimized: Use a hash map to store and look up numbers (O(n) time).

Write Pseudocode:

Copy
Create an empty hash map.
For each number in nums:
    Calculate the complement (target - number).
    If the complement is in the hash map:
        Return the indices.
    Else:
        Add the number and its index to the hash map.
Implement the Solution:

python
Copy
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
Test the Solution:

Test with the provided examples and edge cases.

Analyze Complexity:

Time: O(n) (single pass through the array).

Space: O(n) (hash map stores up to n elements).

Refactor and Improve:

The solution is already optimal, so no further improvements are needed.

Practice Similar Problems:

Try solving Three Sum, Four Sum, or Subarray Sum Equals K.
