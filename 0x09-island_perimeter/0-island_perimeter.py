#!/usr/bin/python3
"""
Enas modylo: oρισmaei mia sinartisi pou ypologizei
to perimetro enos nisiou se ena dosmeno pinaka
"""

def perimetros_nisiou(pinakas):
    """
    Epistrefei to perimetro enos nisimou ston dosmeno pinaka

    Parametroi:
        pinakas (list of list of int): 2D pinakas me 0 (nero) kai 1 (xora).

    Epistrofi:
        int: To perimetro tou nisiou sto pinaka.
    """
    mikos = len(pinakas)
    pi = len(pinakas[0])  # 'breath' translated to Greek 'pi' for "width"
    perimetro = 0
    for x in range(mikos):
        for y in range(pi):
            if pinakas[x][y] == 1:
                perimetro += 4
                if (y < pi - 1 and pinakas[x][y + 1] == 1):
                    perimetro -= 2
                if (x < mikos - 1 and pinakas[x + 1][y] == 1):
                    perimetro -= 2
    return perimetro

