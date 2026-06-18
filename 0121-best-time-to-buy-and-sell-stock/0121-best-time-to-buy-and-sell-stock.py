class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Profit=0
        mp=prices[0]
        for price in prices:
            mp=min(mp,price)
            p=price-mp
            Profit=max(Profit,p)
        return Profit
        