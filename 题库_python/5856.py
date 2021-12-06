from typing import List
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort(reverse=True)
        def backpack(time,task):
            t = [[0]*(time+1) for _ in range(len(task)+1)]
            t1 = [[[]]*(time+1) for _ in range(len(task)+1)]
            for i in range(1,len(task)+1):
                for j in range(1,time+1):
                    t[i][j] = t[i-1][j]
                    t1[i][j] = t1[i-1][j]
                    if task[i-1]<=j:
                        if t[i][j]<t[i-1][j-task[i-1]]+task[i-1]:
                            t[i][j]= t[i-1][j-task[i-1]]+task[i-1]
                            t1[i][j]= t1[i-1][j-task[i-1]]+[task[i-1]]
            
            return t1[-1][-1]
        ret=0
        while len(tasks) > 0:
            ret+=1
            l = backpack(sessionTime,tasks)
            for i in l:
                tasks.remove(i)
        return ret
        

a = Solution()
b = a.minSessions([2,3,3,4,4,4,5,6,7,10],12)
print(b)