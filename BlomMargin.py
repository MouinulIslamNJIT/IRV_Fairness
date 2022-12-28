import heapq as heap
from  LRM import LRM
from DistanceToPi import distanceToPi
from BlomLB import blomLB,blomLBv1


class BlomMargin:
    def __init__(self):
        self.nodeExplored = 0
        self.numLP = 0
        self.branchExplored = 0

    def marginBlom(self,C,B,cw):


        Q = []
        U = 9999999999999
        self.nodeExplored = self.nodeExplored + 1
        pi = [cw]
        l = blomLBv1(B, C, pi)
        heap.heappush(Q, [l, pi])

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
                    self.branchExplored = self.branchExplored + 1
                    l_prime = distanceToPi(B, pi_prime)
                else:
                    l_new = blomLBv1(B,C,pi_prime)
                    l_prime = max(l,l_new)
                    if l_prime < U:
                        self.numLP = self.numLP + 1
                        m =  distanceToPi(B,pi_prime)
                        l_prime = max(l_prime,m)
                if l_prime < U:
                    heap.heappush(Q,[l_prime,pi_prime])
        return U

