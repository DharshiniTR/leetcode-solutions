class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c=0
        for cost in costs:
            if cost<=coins:
                coins-=cost
                c+=1
            else:
                break
        return c

        