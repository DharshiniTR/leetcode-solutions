class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cl=[]
        for num in nums:
            c=0
            while num>0:
                d=num%10
                c=c+1
                num=num//10
            cl.append(c)
        C=0
        for num in cl:
            if num%2==0:
                C+=1
        return C

            

        