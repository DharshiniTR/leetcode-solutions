class Solution:
    def nextGreatestLetter(self, l: List[str], target: str) -> str:
        a=[]
        for i in range(len(l)):
            if ord(l[i])>ord(target):
                a.append(ord(l[i]))
        if a:
            return chr(min(a))
        else:
            return l[0]
        