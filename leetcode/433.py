from typing import List,Deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        if endGene not in bank:
            return -1
        bank = set(bank)
        q = Deque([(startGene,0)])
        while q:
            cur,step = q.popleft()
            for i,x in enumerate(cur):
                for y in "ACGT":
                    if y!=x:
                        next = cur[:i]+y+cur[i+1:]
                        if next in bank:
                            if next == endGene:
                                return step+1
                            bank.remove(next)
                            q.append((next,step+1))
        return -1