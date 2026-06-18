class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for num in digits:
            s+=str(num)
        s=int(s)+1
        l=[]
        s=str(s)
        for i in range(len(s)):
            l.append(int(s[i]))
        return l