class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # print((c-e)/(d-f),(c-a)/(d-b),a < min(e,f))
        if abs(c-e) == abs(d-f):
            if abs(a-e) == abs(b-f):
                if ((a-e)/abs((a-e)))/((b-f)/abs((b-f))) == ((c-e)/abs((c-e)))/((d-f)/abs((d-f))) and a > min(e,c) and a < max(e,c):
                    return 2
            return 1
        if a == e and ( c != e or (d < min(b,f) or d > max(b,f))):
            return 1
        if b == f and ( d != f or (c < min(a,e) or c > max(a,e))):
            return 1
        return 2
# class Solution:
#     def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
#         print((c-e)/(d-f),(c-a)/(d-b),a < min(e,f))
#         if abs(c-e) == abs(d-f) and ((c-e)/(d-f) != (c-a)/(d-b) or (a < min(e,c) or a > max(e,c))):
#             return 1
#         if a == e and ( c != e or (d < min(b,f) or d > max(b,f))):
#             return 1
#         if b == f and ( d != f or (c < min(a,e) or c > max(a,e))):
#             return 1
#         return 2 



a = Solution()
b = a.minMovesToCaptureTheQueen(1,1,1,4,1,8) #2
print(b)

b = a.minMovesToCaptureTheQueen(4,3,3,4,2,5) #1
print(b)

b = a.minMovesToCaptureTheQueen(4,3,3,4,5,2) #2
print(b)

b = a.minMovesToCaptureTheQueen(8,4,8,8,7,7) #1
print(b)

b = a.minMovesToCaptureTheQueen(4,3,1,5,5,3) #1
print(b)

b = a.minMovesToCaptureTheQueen(2,6,5,6,3,4) #1
print(b)