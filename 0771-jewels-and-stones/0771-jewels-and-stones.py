class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        for ch in jewels:
            c+=stones.count(ch)
        return c

        