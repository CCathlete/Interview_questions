# https://leetcode.com/problems/binary-tree-level-order-traversal/

"""
1. Rephrasing:
    - We're given a binary tree and must traverse it from left
    to right, root to leaves and return the values of nodes,
    level by level.

2. Complexity:
    - Time: O(n), n = amount of nodes.
    - Space: O(n), We're returning a list of size 2^h, 
    where h is the number of levels, h is proportional to n.

3. Follow up questions:
    - Should I return one list or a list of lists (a list for
    each level)?
        - It should be a list of lists.
    - Should I return an empty list if I have an empty tree? or a list with a single None?
        - Empty list is ok.

4. Example + Approach:
    - values = [3, 9, 20, None, None, 15, 7]
    - We're going to use a queue (deque that we'll use as a
    regular queue), we'll first take out the current node from
    the left, add it's value to the current level's list.
    Then, we'll push both children (if not None) to the queue,
    and proceed to the next level.

"""

from __future__ import annotations
from collections import deque
from typing import cast


# Helpers.
class TreeNode:
    """
    Defines a single node of a binary tree.
    """

    val: int
    # Children of the node.
    left: TreeNode | None
    right: TreeNode | None

    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def init_tree(values: list[int | None]) -> TreeNode | None:
    """Gets an ordered list of values, links all values as a
    binary tree and returns the root.

    Args:
        values (list[int  |  None]): values of all nodes according to level order (left to right).

    Returns:
        The root of the tree.
    """
    if values is None:
        return None
    if values[0] is None:
        return None

    root: TreeNode = TreeNode(values[0])
    nodes_to_link: deque[TreeNode] = deque([root])
    i = 1  # Pointer to traverse the list starting left child of root.

    while nodes_to_link and i < len(values):
        node: TreeNode = (
            nodes_to_link.popleft()
        )  # Get the next node to assign children.

        # Assign left child if available.
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(cast(int, values[i]))
            nodes_to_link.append(node.left)
        i += 1

        # Assign right child if available.
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(cast(int, values[i]))
            nodes_to_link.append(node.right)
        i += 1

    return root


# Implementation.


def traverse_level_order(root: TreeNode | None) -> list[list[int]]:
    """Utilises BFS to traverse tree and collect the value of
    each node (null if there is no node) from left to right
    and root to leaves.

    Args:
        root (TreeNode): Root node of an initialised binary tree.

    Returns:
        list[list[int]]: A list that each cell is a list vith the values of nodes in the corrseponding level.
    """

    if root is None:
        return []

    levels: list[list[int]] = []
    node_handling_queue: deque[TreeNode] = deque([root])

    while node_handling_queue:
        level: list[int] = []
        nodes_in_level: int = len(node_handling_queue)

        for _ in range(nodes_in_level):
            current_node: TreeNode = node_handling_queue.popleft()
            # Adding the value of current node to the values of this current level.
            level.append(current_node.val)

            # Adding the next level of nodes to the queue.
            if current_node.left:
                node_handling_queue.append(current_node.left)

            if current_node.right:
                node_handling_queue.append(current_node.right)

        levels.append(level)

    return levels


# Test case structure.


class TestCase:
    """Structure of a single test case."""

    name: str
    root: TreeNode | None
    expected: list[list[int]]

    def __init__(
        self,
        name: str,
        values: list[int | None],
        expected: list[list[int]],
    ):
        self.name = name
        self.root = init_tree(values)
        self.expected = expected


# Main function.


def main() -> None:
    """Entry point for the program."""

    test_cases: list[TestCase] = [
        TestCase(
            name="Happy case.",
            values=[3, 9, 20, None, None, 15, 7],
            expected=[[3], [9, 20], [15, 7]],
        )
    ]

    for case in test_cases:
        print(f"Running case: {case.name}")
        print(f"Expected: {case.expected}")
        print(f"Result: {traverse_level_order(case.root)}")


if __name__ == "__main__":
    main()
