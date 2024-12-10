#!/usr/bin/python3
"""
Module for calculating the perimeter of an island.
"""

def tanhua_pangyuan(grid):
    """
    Calculate the perimeter of the island described in a grid.

    Parameters:
        grid: list of list of int

    Returns:
        int: The perimeter of the island.
    """
    lihn = len(grid)  # Number of rows in the grid
    kah = len(grid[0])  # Number of columns in the grid
    pangyuan = 0  # Variable to store the perimeter

    for i in range(lihn):
        for j in range(kah):
            if grid[i][j] == 1:  # If it's part of the island

                # Check if it's on the top edge or adjacent cell is water
                if i == 0 or grid[i - 1][j] == 0:
                    pangyuan += 1

                # Check if it's on the bottom edge or adjacent cell is water
                if i == lihn - 1 or grid[i + 1][j] == 0:
                    pangyuan += 1

                # Check if it's on the left edge or adjacent cell is water
                if j == 0 or grid[i][j - 1] == 0:
                    pangyuan += 1

                # Check if it's on the right edge or adjacent cell is water
                if j == kah - 1 or grid[i][j + 1] == 0:
                    pangyuan += 1

    return pangyuan  # Return the calculated perimeter

