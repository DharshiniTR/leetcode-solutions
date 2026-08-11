class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        h=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                h+=customers[i]
        g=0
        for i in range(minutes):
            if grumpy[i]==1:
                g+=customers[i]
        m=g
        for i in range(minutes,len(customers)):
            if grumpy[i]==1:
                g+=customers[i]
            if grumpy[i-minutes]==1:
                g-=customers[i-minutes]
            m=max(m,g)
        return m+h
                
        