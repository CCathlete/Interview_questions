# Leetcode Patterns

##

### **1. Two Pointers**

**What it is:** A technique where two pointers (indices) are used to traverse an array or string, often from opposite ends or at different speeds.

**When to use:**

- Problems involving arrays or strings.
- Finding pairs, triplets, or subarrays that satisfy certain conditions.
- Reversing or manipulating strings/arrays.

**Example Problem:** [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

- Given a sorted array, find two numbers that add up to a target.

**Approach:**

- Use two pointers, one at the start (`left`) and one at the end (`right`).
- Move the pointers towards each other based on whether the sum is less than or greater than the target.

**Code:**

```python
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # 1-based indexing
        elif current_sum < target:
            left += 1
        else:
            right -= 1
```

---

### **2. Sliding Window**

**What it is:** A technique where a "window" (subarray or substring) is moved through the array or string to solve problems efficiently.

**When to use:**

- Problems involving subarrays or substrings.
- Finding the maximum/minimum sum, longest/shortest substring, or counting occurrences.

**Example Problem:** [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

- Find the contiguous subarray with the largest sum.

**Approach:**

- Use a window to track the current subarray.
- Expand the window when the current sum is positive, and shrink it when the sum becomes negative.

**Code:**

```python
def maxSubArray(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
```

---

### **3. Binary Search**

**What it is:** A divide-and-conquer algorithm used to efficiently search for an element in a sorted array or solve optimization problems.

**When to use:**

- Searching in sorted arrays.
- Finding the minimum/maximum value that satisfies a condition.

**Example Problem:** [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

- Search for a target value in a rotated sorted array.

**Approach:**

- Use binary search to divide the array into halves and eliminate the half where the target cannot be.

**Code:**

```python
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

---

### **4. Depth-First Search (DFS) / Breadth-First Search (BFS)**

**What it is:** Algorithms for traversing or searching tree or graph structures.

**When to use:**

- Tree or graph traversal.
- Finding paths, connected components, or cycles.

**Example Problem (DFS):** [Number of Islands](https://leetcode.com/problems/number-of-islands/)

- Count the number of islands in a 2D grid.

**Approach (DFS):**

- Traverse the grid, and for each "1" (land), perform DFS to mark all connected land cells.

**Code (DFS):**

```python
def numIslands(grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'  # Mark as visited
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
```

**Example Problem (BFS):** [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

- Traverse a binary tree level by level.

**Approach (BFS):**

- Use a queue to process nodes level by level.

**Code (BFS):**

```python
from collections import deque

def levelOrder(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

---

### **5. Dynamic Programming (DP)**

**What it is:** A technique to solve problems by breaking them into smaller subproblems and storing the results to avoid redundant computations.

**When to use:**

- Problems with overlapping subproblems (e.g., Fibonacci, knapsack).
- Optimization problems.

**Example Problem:** [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

- Find the number of ways to climb `n` stairs, taking 1 or 2 steps at a time.

**Approach:**

- Use DP to store the number of ways to reach each step.

**Code:**

```python
def climbStairs(n):
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

---

### **6. Greedy Algorithms**

**What it is:** A technique where the best local choice is made at each step to achieve a global optimum.

**When to use:**

- Problems where local optima lead to a global optimum (e.g., scheduling, coin change).

**Example Problem:** [Coin Change](https://leetcode.com/problems/coin-change/)

- Find the minimum number of coins to make a given amount.

**Approach:**

- Use a greedy strategy to pick the largest coin first (if applicable).

**Code:**

```python
def coinChange(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count if amount == 0 else -1
```

---

### **7. Hash Maps**

**What it is:** A data structure that stores key-value pairs for efficient lookups, insertions, and deletions.

**When to use:**

- Counting, frequency analysis, or lookups.
- Problems involving duplicates or unique elements.

**Example Problem:** [Two Sum](https://leetcode.com/problems/two-sum/)

- Find two numbers that add up to a target.

**Approach:**

- Use a hash map to store numbers and their indices for quick lookup.

**Code:**

```python
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
```

---

### **8. Stack/Queue**

**What it is:** Data structures that store elements in a specific order (LIFO for stack, FIFO for queue).

**When to use:**

- Problems involving order or levels (e.g., parentheses, BFS).

**Example Problem (Stack):** [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

- Check if a string of parentheses is valid.

**Approach:**

- Use a stack to track opening parentheses and match them with closing ones.

**Code:**

```python
def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
```

---

### **Summary**

Each of these patterns is a powerful tool for solving specific types of problems. By understanding when and how to use them, you can tackle a wide range of LeetCode questions effectively. Let me know if you'd like further clarification or examples! 😊
