


def IRV(B, C):
    n = len(C)
    pi = []
    C_pi = set(C) - set(pi)
    round = 0
    while (len(C_pi) != 1):
        round = round + 1
        print("round = ",round)
        B_prime = projectedBallots(B, C_pi)
        T = findTally(B_prime, C_pi)
        print("Tally = ",T)
        e = min(T, key=T.get)
        pi.append(e)
        C_pi = set(C) - set(pi)
    pi.extend(C_pi)
    return pi



def projectedBallots(ballots,pi):
    newBallots = {}
    for signature,count in ballots.items():
        newSignature = []
        for candidate in signature:
            if candidate in pi:
                newSignature.append(candidate)
        if tuple(newSignature) in newBallots:
            newBallots[tuple(newSignature)] = newBallots[tuple(newSignature)]  + count
        else:
            newBallots[tuple(newSignature)] = count
    return newBallots


def projectedBallotsAndTally(ballots,pi,e):
    newBallots = {}
    T = {}
    for i in pi:
        T[i] = 0
    for signature,count in ballots.items():
        newSignature = []
        for candidate in signature:
            if candidate in pi:
                T[candidate] = T[candidate] + count
                break
            if candidate == e:
                break
    return T

def findTally(B,C):
    T = {}
    for i in C:
        T[i] = 0
    for s,c in B.items():
        if len(s) == 0:
            continue
        w = s[0]
        T[w] = T[w] + c
    return T


def finAllSignature(pi):
    pi = list(pi)
    pi.reverse()
    allSig = []
    for i in range(0,len(pi)):
        c = pi[i]
        newSig = []
        for s in allSig:
            sl = list(s)
            sl.insert(0,c)
            newSig.append(tuple(sl))
        allSig.extend(newSig)
        allSig.append(tuple([c]))
    return allSig

def createEquivalenceClasses(B,pi):
    pi = list(pi)
    pi.reverse()
    B_new = {}
    for b in B.keys():
        b_new = []
        if len(b) == 0:
            continue
        c = b[0]
        b_new.append(c)
        i = pi.index(c)
        for c in b:
            j = pi.index(c)
            if j < i:
                i = j
                b_new.append(c)
        b_new = tuple(b_new)
        if b_new in B_new:
            B_new[b_new] = B_new[b_new] + B[b]
        else:
            B_new[b_new] = B[b]

    return B_new