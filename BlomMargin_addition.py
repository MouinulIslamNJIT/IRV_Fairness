import heapq as heap
from  LRM_addition import LRM
from DistanceToPi_addition import distanceToPi
from BlomLB_addition import blomLB


class BlomMargin:
    def __init__(self):
        self.nodeExplored = 0
        self.numLP = 0

    def marginBlom(self,C,B,cw):


        Q = []
        U = LRM(B,C)
        C_w = set(C)-{cw}
        for c in C_w:
            pi = [c]
            l = blomLB(B,C,pi)
            self.nodeExplored = self.nodeExplored + 1
            if l < U:
                heap.heappush(Q, [l,pi])

        while(len(Q) != 0 ):
            l,pi = heap.heappop(Q)
            if l < U:
                U = min(U,self.expandBlom(l,pi,U,Q,C,B))

        return U


    def expandBlom(self,l,pi,U,Q,C,B):

        if len(pi) == len(C):
            return l
        else:
            C_pi = set(C) - set(pi)
            for c in C_pi:
                self.nodeExplored = self.nodeExplored + 1
                pi_prime = list(pi)
                pi_prime.insert(0,c)
                if len(pi_prime) == len(C):
                    self.numLP = self.numLP + 1
                    l_prime = distanceToPi(B, pi_prime)
                else:
                    l_new = blomLB(B,C,pi_prime)
                    l_prime = max(l,l_new)
                    if l_prime < U:
                        self.numLP = self.numLP + 1
                        m =  distanceToPi(B,pi_prime)
                        l_prime = max(l_prime,m)
                if l_prime < U:
                    heap.heappush(Q,[l_prime,pi_prime])
        return U

