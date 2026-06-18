class Solution:
    def reverseWords(self, s: str) -> str:
        r=""
        for word in s.split():
            r=word+" "+r
        return r.strip()
        