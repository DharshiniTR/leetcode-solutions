from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        q=deque()
        v=set()
        q.append((beginWord,1))
        v.add(beginWord)
        while q:
            state,steps=q.popleft()
            if state==endWord:
                return steps
            for i in range(len(state)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    nw=state[:i]+ch+state[i+1:]
                    if nw in wordList and nw not in v:
                        v.add(nw)
                        q.append((nw,steps+1))
        return 0
            
        