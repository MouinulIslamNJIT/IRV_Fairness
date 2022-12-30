

from Utils import projectedBallots, findTally


def distanceToPiExact(B,pi):
    addTally = {}
    for c in pi:
        addTally[c] = 0
    pi_prime = pi
    r = 1

    while len(pi_prime) > 1:
        if r == 1:
            prevElm = {}
        else:
            prevElm = pi[0:r-1]

        pi_prime = pi[r-1:]
        B_prime = projectedBallots(B,pi_prime)
        TotalAdd,AddTally = distanceSingleRound(B_prime,pi_prime,addTally)
        while TotalAdd > 0 and len(prevElm) > 0:
            e = prevElm.pop()
            if TotalAdd >= addTally[e]:
                TotalAdd = TotalAdd - addTally[e]
                addTally[e] = 0
            else:
                addTally[e] = addTally[e] - TotalAdd
                TotalAdd = 0
        r = r + 1
    return sum(addTally.values())


def distanceSingleRound(B,pi,addTally):
    TotalAdd = 0
    Tally = findTally(B,pi)
    c1 = pi[0]
    for c in pi[1:]:
        if Tally[c1] + addTally[c1] > Tally[c] + addTally[c]:
            diff = Tally[c1] + addTally[c1] - Tally[c] - addTally[c]
            TotalAdd = TotalAdd + diff
            addTally[c] = addTally[c] + diff
    return TotalAdd,addTally