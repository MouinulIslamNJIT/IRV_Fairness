import sys
import math

def findTally(B,S):
    Tally = {}
    for c in S:
        Tally[c] = 0
    for s, count in B.items():
        u = [x for x in s if x in S]
        if len(u) > 0:
            w = u[0]
            Tally[w] = Tally[w] + count
    return Tally

def boundTree(B,S,c_w,UB):
    if len(S) != 1:
        Tally = findTally(B, S)

        temp = Tally[c_w]
        Tally[c_w] = sys.maxsize

        minval = min(Tally.values())
        allMin = [k for k, v in Tally.items() if v == minval]

        for loser in allMin:
            S_copy = S.copy()
            S_copy.remove(loser)
            Tally[c_w] = temp
            UB = max(UB, (Tally[loser] - Tally[c_w]))
            UB = max(UB,boundTree(B,S_copy,c_w,UB))
    return UB

def heuristic(B,C,c_w):

    S = list(C)
    UB = 0
    UB = boundTree(B,S,c_w,UB)

    return math.ceil((UB/2))