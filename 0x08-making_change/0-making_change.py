#!/usr/bin/python3 
"""
This Python program solves the coin change problem using recursion.
It calculates the minimum number of coins required to make a specific total value.
"""

def makeChange(kahbin, chongkinia):
    """
    This function determines the smallest number of coins required to achieve the target total.
    If it is impossible to reach the target with the given coins, the function returns -1.

    Arguments:
    - kahbin: A list of integers representing the available coin denominations
    - chongkinia: The target total value we want to form with the minimum number of coins

    Returns:
    - int: The fewest number of coins needed to reach the target total, 
           or -1 if it's not achievable
    """
    if chongkinia <= 0:
        return 0
    elif chongkinia > 0:
        sinchian = sorted(kahbin[:])  # Create a sorted copy of the coin denominations
        sinchian = list(reversed(sinchian))  # Reverse the sorted list to start with the largest coin
        kiatshu = 0
        kinia = chongkinia + 0
        siongki = 0
        
        # Loop to check how many coins are needed
        while kinia >= 0 and (siongki < len(sinchian)):
            if kinia >= sinchian[siongki]:
                kinia = kinia - sinchian[siongki]
                kiatshu += 1
            elif kinia < sinchian[siongki]:
                siongki += 1

        if siongki == len(sinchian):
            if kinia != 0:
                return -1  # Return -1 if we cannot achieve the target value
            elif kinia == 0:
                return kiatshu  # Return the number of coins used when the target is achieved

