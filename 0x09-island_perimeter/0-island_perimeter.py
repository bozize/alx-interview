#!/usr/bin/python3
"""Perimeter of an Island - ALX Technical Interview"""

def elegxos_aksiotitas(x):
    """Check if the value is 0 or 1.

    Args:
        x (int): The value to check.

    Returns:
        int: Returns 1 if the value is 0, otherwise returns 0.
    """
    if x == 0:
        return 1
    return 0


def perimetros_nisiou(pinakas):
    """Calculate the perimeter of an island in a grid.

    Args:
        pinakas (list of list of int): 2D grid representing the island where
                                       1's represent land and 0's represent water.

    Returns:
        int: The total perimeter of the island.
    """

    arithmos_grammes = len(pinakas)
    arithmos_stiles = len(pinakas[0])
    assert 1 <= arithmos_grammes <= 100 and 1 <= arithmos_stiles <= 100, "The dimensions must be between 1 and 100"

    perimetros = 0
    for i in range(arithmos_grammes):
        for j in range(arithmos_stiles):
            assert pinakas[i][j] == 0 or pinakas[i][j] == 1, "Grid values must be either 0 or 1"
            
            if pinakas[i][j] == 1:
                if i - 1 < 0:
                    perimetros += 1
                else:
                    perimetros += elegxos_aksiotitas(pinakas[i-1][j])

                if j - 1 < 0:
                    perimetros += 1
                else:
                    perimetros += elegxos_aksiotitas(pinakas[i][j-1])

                try:
                    perimetros += elegxos_aksiotitas(pinakas[i+1][j])
                except IndexError:
                    perimetros += 1

                try:
                    perimetros += elegxos_aksiotitas(pinakas[i][j+1])
                except IndexError:
                    perimetros += 1

    return perimetros

