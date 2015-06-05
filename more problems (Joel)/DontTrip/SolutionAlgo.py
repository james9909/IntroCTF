"""Problem: Don't trip
James has dropped his wallet and scattered a lot of his coins. A good friend came up and recorded where each coin was, and gave this LIST to James. If James starts at a coin he dropped where he is standing, what area does his path enclo$
"""
import random
def doNotTrip(L):#List of tuples (coords)
    lX = []
    lY = []
    prod1 = 0
    prod2 = 0
    for n in L:
        lX.append(n[0])
        lY.append(n[1])
    lX.append(lX[0])
    lY.append(lY[0])
    i = 0
    while i < len(lX)-1:
        prod1 += lX[i]*lY[i+1]
        prod2 += lY[i]*lX[i+1]
        i += 1
    return .5 * abs(prod1-prod2)







