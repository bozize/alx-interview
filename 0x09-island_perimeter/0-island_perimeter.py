#!/usr/bin/python3
"""
Module for calculating the perimeter of an island described in a grid.
"""

def perimetros_nisou(diktio):
    """
    Calculate the perimeter of the island described in a grid.

    Parameters:
        diktio: list of list of int
            A 2D grid where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    # Get the number of rows and columns in the grid
    grammes = len(diktio)
    stiloi = len(diktio[0])
    perimetros = 0

    # Iterate through each cell in the grid
    for grammh in range(grammes):
        for stilos in range(stiloi):
            # If the current cell is land (1)
            if diktio[grammh][stilos] == 1:
                # Check the four neighbors (top, bottom, left, right)

                # Check the top (if we're on the first row or the cell above is water)
                if grammh == 0 or diktio[grammh - 1][stilos] == 0:
                    perimetros += 1

                # Check the bottom (if we're on the last row or the cell below is water)
                if grammh == grammes - 1 or diktio[grammh + 1][stilos] == 0:
                    perimetros += 1

                # Check the left (if we're on the first column or the cell to the left is water)
                if stilos == 0 or diktio[grammh][stilos - 1] == 0:
                    perimetros += 1

                # Check the right (if we're on the last column or the cell to the right is water)
                if stilos == stiloi - 1 or diktio[grammh][stilos + 1] == 0:
                    perimetros += 1

    return perimetros
