#!/usr/bin/python3
"""Ypologismos Perimetrou Nisiou se Pinaka - ALX Interview"""

def elegxos_orio(x):
    """Elegxei an ena kelio tou pinaka einai se orio i nero.

    Parametroi:
        x (int): H timi se ena kelio tou pinaka (0 i 1).

    Epistrofi:
        int: Epistrefei 1 an to kelio einai nero (0) i exei vgei apo ta oria, alliws epistrefei 0.
    """
    if x == 0:
        return 1
    return 0


def perimetros_nisiou(pinakas):
    """Ypologizei to perimetro enos nisiou sto pinaka.

    O pinakas periexei 1 (xora) kai 0 (nero). H sinartisi ypologizei
    to perimetro mesw tou ypologismou twn orion twn kelion xoras pou
    einai konta sto nero i sta oria tou pinaka.

    Parametroi:
        pinakas (list of list of int): 2D pinakas pou antistixe me to nisi, 
                                       opou to 1 antistixe to xora kai to 0 to nero.

    Epistrofi:
        int: To synoliko perimetro tou nisiou.
    """
    
    # Labbete ton arithmo twn grammon kai twn stilwn tou pinaka
    grammes = len(pinakas)
    stiles = len(pinakas[0])

    # Elegxos mihanismou gia tis diastaseis tou pinaka
    assert 1 <= grammes <= 100 and 1 <= stiles <= 100, "Oi diastaseis tou pinaka prepei na einai meta xoris 1 kai 100."

    perimetro = 0
    for i in range(grammes):
        for j in range(stiles):
            # Elegxos gia mono 0 kai 1 sto pinaka
            assert pinakas[i][j] == 0 or pinakas[i][j] == 1, "Oi times tou pinaka prepei na einai mono 0 i 1."

            # Monon ypologizoume perimetro gia kelia xoras (1)
            if pinakas[i][j] == 1:
                # Elegxos gia oria tou pinaka i nero konta sto kelio xoras
                if i == 0 or pinakas[i-1][j] == 0:  # Elegxos panw
                    perimetro += 1
                if i == grammes - 1 or pinakas[i+1][j] == 0:  # Elegxos katw
                    perimetro += 1
                if j == 0 or pinakas[i][j-1] == 0:  # Elegxos aristera
                    perimetro += 1
                if j == stiles - 1 or pinakas[i][j+1] == 0:  # Elegxos deksia
                    perimetro += 1

    return perimetro

