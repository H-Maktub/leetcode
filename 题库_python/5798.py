from typing import List
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        c = min(m,n)//2
        temp = [[0]*n for _ in range(m) ]
        for i in  range(c):
            t = []
            for l in range(m-1-i*2):
                t.append(grid[l+i][i])
            for b in range(n-1-i*2):
                t.append(grid[m-1-i][i+b])
            for r in range(m-1-i*2):
                t.append(grid[m-1-i-r][n-1-i])
            for tt in range(n-1-i*2):
                print(i,m-1-i-tt,m,n)
                t.append(grid[i][n-1-i-tt])
            r = k%len(t)
            tt = []
            for j in range(len(t)):
                tt.append(t[j-r])
            for t in range(n-1-i*2):
                temp[i][i+1+t]=tt.pop()
            for r in range(m-1-i*2):
                temp[i+1+r][n-1-i]=tt.pop()
            for b in range(n-1-i*2):
                temp[m-1-i][n-2-i-b]=tt.pop()
            for l in range(m-1-i*2):
                temp[m-2-i-l][i] = tt.pop()
        return temp



a = Solution()
b = a.rotateGrid([[10,1,4,8],[6,6,3,10],[7,4,7,10],[1,10,6,1],[2,1,1,10],[3,8,9,2],[7,1,10,10],[7,1,4,9],[2,2,4,2],[10,7,5,10]],1)
a = Solution()
b = a.rotateGrid([[3970,1906,3608,298,3072,3546,1502,773,4388,3115,747,3937],[2822,304,4179,1780,1709,1058,3645,681,2910,2513,4357,1038],[4471,2443,218,550,2766,4780,1997,1672,4095,161,4645,3838],[2035,2350,3653,4127,3208,4717,4347,3452,1601,3725,3060,2270],[188,2278,81,3454,3204,1897,2862,4381,3704,2587,743,3832],[996,4499,66,2742,1761,1189,608,509,2344,3271,3076,108],[3274,2042,2157,3226,2938,3766,2610,4510,219,1276,3712,4143],[744,234,2159,4478,4161,4549,4214,4272,701,4376,3110,4896],[4431,1011,757,2690,83,3546,946,1122,2216,3944,2715,2842],[898,4087,703,4153,3297,2968,3268,4717,1922,2527,3139,1516],[1086,1090,302,1273,2292,234,3268,2284,4203,3838,2227,3651],[2055,4406,2278,3351,3217,2506,4525,233,3829,63,4470,3170],[3797,3276,1755,1727,1131,4108,3633,1835,1345,1293,2778,2805],[1215,84,282,2721,2360,2321,1435,2617,1202,2876,3420,3034]]
,405548684)
