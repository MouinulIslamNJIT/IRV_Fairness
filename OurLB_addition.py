from Utils import projectedBallots, findTally
import math

def  OurLB(B,pi):

    B = projectedBallots(B, pi)
    pi = list(pi)
    LB = 0
    removed = []
    added = {}
    for c in pi:
        added[c] = 0
    while len(pi) != 1:
        sumlb = 0
        Tally = {}
        for c in pi:
            Tally[c] = 0
        for s, count in B.items():
            if len(s) == 0:
                continue
            u = [x for x in s if x in pi]
            if len(u) > 0:
                w = u[0]
                Tally[w] = Tally[w] + count
        e = pi[0]
        pi.remove(e)

        allci = []
        for c in pi:
            #LB = math.ceil(max(LB, (Tally[e] - Tally[c]) / 2))
            if Tally[e] >= Tally[c]:
                allci.append(Tally[c])
                if (c,) in B.keys():
                    B[(c,)] = B[(c,)] + Tally[e] - Tally[c]
                else:
                    B[(c,)] =  Tally[e] - Tally[c]
                added[c] = added[c]  + Tally[e] - Tally[c]
                sumlb = sumlb  + Tally[e] - Tally[c]
        removed.append(e)

        for i in range(0,len(removed)-1):
            e = removed[i]
            sumlb = sumlb - added[e]
            if sumlb < 0:
                added[e] = sumlb * (-1)
                break
            else:
                added[e] = 0



        if sumlb >0:
            LB = LB + sumlb
        #         #allci.sort()

        #if len(allci) != 0:

            #minCi = min(allci)

            # LB_t = 999999999999
            # lo = minCi
            # hi = Tally[e]
            #
            # # while lo<hi:
            #     t = math.floor((hi + lo)/2)
            #     lb_t1 = Tally[e] - t
            #     lb_t2 = sum([t - x for x in allci if x < t])
            #     LB_t = max(lb_t1, lb_t2)
            #
            #     t = t + 1
            #     lb_t1 = Tally[e] - t
            #     lb_t2 = sum([t - x for x in allci if x < t])
            #     LB_t_1 = max(lb_t1, lb_t2)
            #
            #     if LB_t < LB_t_1:
            #         hi = t - 1
            #     else:
            #         lo = t

            # for t in allci:
            #     sumlb = sumlb + Tally[e] - t

            #LB = max(LB,sumlb)
    sumAdd = sum(added.values())
    if sumAdd != LB:
        print("wrong")

    return sumAdd


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