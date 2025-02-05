# https://leetcode.com/problems/number-of-islands/

"""
1. Rephrasing:
    - We get a 'grid' which is a matrix of 1s and 0s.
    - 1 means land, 0 means water.
    - 1s that are adjacent orizontally or vertically mean connected pieces of land (island).
    - We need to return the number of islands in our grid.

2. Complexity:
    - Time: O(n * m), n = len(grid[0]), m = len(grid)
    - Space: O(n * m), using dfs we'll visit each cell at most once.

3. Follow up questions:
    - Diagonal 1s counts as connected?
        - No.
    - Do I need to validate the grid?
        - No.
    - Should I return 0 if the grid is empty?
        - Yes.

4. Example + Approach:
    - We'll scan the grid for unexplored pieces of land.
    - Once found, we'll use the point as a starting point for dfs that will run through all pieces of land connected to the initial piece and mark them as visited.
    - That way, we'll run dfs only one per island, so we can add 1 to the counter every dfs run.
"""

from typing import Callable
from itertools import product

# Helpers.


class Grid:
    """Holds metadata about the grid."""

    area: list[list[int]]
    visited: list[list[bool]]
    rows: int
    columns: int

    def __init__(
        self,
        area: list[list[int]],
    ) -> None:
        self.area = area
        self.rows = len(area)
        self.columns = len(area[0])
        # Setting all vertices to unvisited.
        self.visited = [[False] * self.columns for _ in range(self.rows)]

    def __str__(self) -> str:
        return f"Area: {self.area}\nVisited: {self.visited}"


def dfs(
    grid: Grid,
    i: int,
    j: int,
    visiting_action: Callable[[Grid, int, int], None],
) -> None:
    """Implements the depth first search algo on a connected component.
    Moves through connected pieces of land, marking them as visited.

    Args:
        grid (Grid): Topographical data.
        i (int): Row pointer of a vertex.
        j (int): Column pointer of a vertex.
    """
    # If we've passed the frame, we can start going back.
    out_of_borders: bool = i < 0 or j < 0 or i >= grid.rows or j >= grid.columns
    if out_of_borders:
        return

    # If we're inside the bounds but the are is water or already visited.
    dont_explore: bool = grid.area[i][j] == 0 or grid.visited[i][j]
    if dont_explore:
        return

    visiting_action(grid, i, j)
    # Scanning the area starting at i, j.
    dfs(grid, i + 1, j, visiting_action)
    dfs(grid, i - 1, j, visiting_action)
    dfs(grid, i, j + 1, visiting_action)
    dfs(grid, i, j - 1, visiting_action)


# Implementation.


def num_islands(grid: Grid) -> int:
    """Utilises DFS to count the number of 'islands'.

    Args:
        grid (Grid): Information about the area.

    Returns:
        int: Number of islands.
    """
    island_counter: int = 0

    if grid.area == []:
        return 0

    # Action to be performed when visiting land.
    def mark_visited(grid, i, j):
        grid.visited[i][j] = True

    for i, j in product(range(grid.rows), range(grid.columns)):
        # If we found an unexpolred piece of land, dfs will mark the entire connected land as visited.
        if grid.area[i][j] == 1 and not grid.visited[i][j]:
            dfs(grid, i, j, visiting_action=mark_visited)
            island_counter += 1

    return island_counter


# Test case.


class TestCase:
    """Holds metadata for each test case."""

    name: str
    grid: Grid
    expected: int

    def __init__(
        self,
        name: str,
        grid: Grid,
        expected: int,
    ) -> None:

        self.name = name
        self.grid = grid
        self.expected = expected


# Main function.
def main() -> None:
    """Entry point for counting the number of islands."""
    test_cases: list[TestCase] = [
        TestCase(
            name="Happy case.",
            grid=Grid(
                [
                    [1, 1, 0, 0, 0],
                    [1, 1, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 1],
                ]
            ),
            expected=3,
        ),
    ]

    for case in test_cases:
        print(f"Running case: {case.name}")
        print(f"Grid: {case.grid}")
        print(f"Expected: {case.expected}")
        print(f"Result: {num_islands(case.grid)}")


if __name__ == "__main__":
    main()
