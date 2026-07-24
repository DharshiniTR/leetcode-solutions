from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s=""
        for row in board:
            for num in row:
                s+=str(num)
        t="123450"
        moves={
            0:[1,3],
            1:[0,2,4],
            2:[1,5],
            3:[0,4],
            4:[1,3,5],
            5:[2,4]
        }
        q=deque()
        v=set()
        q.append((s,0))
        while q:
            state,steps=q.popleft()
            if state==t:
                return steps
            z=state.index("0")
            for np in moves[z]:
                ns=list(state)
                ns[z],ns[np]=(ns[np],ns[z])
                ns="".join(ns)
                if ns not in v:
                    v.add(ns)
                    q.append((ns,steps+1))
        return -1