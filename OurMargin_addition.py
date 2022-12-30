
import heapq as heap
from  LRM_addition import LRM
from DistanceToPi_addition import distanceToPi
from BlomLB_addition import blomLB
from OurLB_addition import OurLB
from distanceToExact_addition import distanceToPiExact

class OurMargin:
    def __init__(self):
        self.nodeExplored = 0
        self.numLP = 0
        self.lbNotEq = 0

    def marginOurs(self,C,B,cw):
        Q = []
        U = LRM(B,C)
        print("upper bound = ",U)
        C_w = set(C)-{cw}
        for c in C_w:
            self.nodeExplored = self.nodeExplored + 1
            pi = [c]
            l = blomLB(B,C,pi)
            if l < U:
                heap.heappush(Q, [l,pi])

        while(len(Q) != 0 ):
            l,pi = heap.heappop(Q)
            if l < U:
                U = min(U,self.expandMOurs(l,pi,U,Q,C,B))

        return U

    def expandMOurs(self,l,pi,U,Q,C,B):
        if len(pi) == len(C):
            m = OurLB(B, pi)
            if m >= U:
                return U
            self.numLP = self.numLP + 1
            #m = OurLB(B, pi)
            m1 = distanceToPi(B, pi)
            m2 = distanceToPiExact(B,pi)
            if m2 != m1:
                print("not equal")
                self.lbNotEq = self.lbNotEq + 1
            return m2
        else:
            C_pi = set(C) - set(pi)
            for c in C_pi:
                self.nodeExplored = self.nodeExplored + 1
                pi_prime = list(pi)
                pi_prime.insert(0,c)
                l_new = blomLB(B,C,pi_prime)
                l_prime = max(l,l_new)
                if l_prime < U:
                    m = OurLB(B, pi_prime)
                    m1 = distanceToPi(B, pi_prime)
                    m2 = distanceToPiExact(B,pi_prime)
                    if m2 != m1:
                        print("not equal")
                        self.lbNotEq = self.lbNotEq + 1
                    l_prime = max(l_prime,m2)
                if l_prime < U:
                    heap.heappush(Q,[l_prime,pi_prime])
        return U
