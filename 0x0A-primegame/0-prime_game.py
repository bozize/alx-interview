#!/usr/bin/python3
"""
Prime Game top
"""


def findMultiples(ani, ana):
    """
    Finds
    """
    for i in ana:
        if i % ani == 0:
            ana.remove(i)
    return ana


def isPrime(i):
    """
    Prime.
    """
    if i == 1:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


def findPrimes(n):
    """
    Find.
    """
    counter = 0
    ana = list(n)
    for i in range(1, len(ana) + 1):
        if isPrime(i):
            counter += 1
            ana.remove(i)
            ana = findMultiples(i, ana)
        else:
            pass
    return counter


def isWinner(x, ani):
    """
    Winner.
    """
    players = {'Maria': 0, 'Ben': 0}
    cluster = set()
    for elem in range(x):
        nums.sort()
        ani = nums[elem]
        for i in range(1, ani + 1):
            cluster.add(i)
            if i == ani + 1:
                break
        temp = findPrimes(cluster)

        if temp % 2 == 0:
            players['nona'] += 1
        elif temp % 2 != 0:
            players['abdi'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None
