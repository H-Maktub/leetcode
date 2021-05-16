from typing import List
class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        t = 1
        while t<=memory1 or t <=memory2:
            if memory1 >= memory2:
                memory1 -=t
            else:
                memory2 -=t
            t+=1
        return [t,memory1,memory2]

a = Solution()
b =a.memLeak(2,2)
print(b)
b =a.memLeak(8,11)
print(b)


# class Solution:
#     def memLeak(self, memory1: int, memory2: int) -> List[int]:
#         t = 1
#         while t<=memory1+memory2:
#             if memory1 >= memory2:
#                 memory1 -=t
#             else:
#                 memory2 -=t
#             # if memory1 < 0:
#             #     memory2 -=memory1
#             # if memory2 < 0:
#             #     memory1 -=memory2
#             t+=1
#         return [t,memory1,memory2]