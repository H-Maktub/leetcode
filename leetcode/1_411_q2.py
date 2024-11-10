from typing import List
from functools import cache
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        temp = [energyDrinkA,energyDrinkB]
        res = [[0,0] for _ in range(n)]
        res[0] = [energyDrinkA[0],energyDrinkB[0]]
        for i in range(1,n):
            res[i][0] = max(res[i-1][0]+energyDrinkA[i],res[i-1][1])
            res[i][1] = max(res[i-1][1]+energyDrinkB[i],res[i-1][0])
            # if i > 1:
            #     res[i][0] = max(res[i-2][1]+energyDrinkA[i],res[i][0])
        return max(res[-1])
    

a = Solution()
# b = a.maxEnergyBoost([4,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1],[4,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1])
b = a.maxEnergyBoost([1801,60716,37726,68357,81497,93047,51014,72664,25041,63261,82051,44136,24746,49775,39970,20604,31542,40100,55637,96719,56595,31142,77691,82164,53571,15442,95027,49323,76569,47341,20653,68722,49053,29387,11164,13307,23164,46559,50155,85669,57631,31633,30033,45109,21089,96791,29291,73574,48852,67340,83198,2637,34596,87978,82634,32677,18544,26605,10359,50515,90720,14290,5836,63192,86348,51730,14873,62180,70882,54944,13626,96508,48080,47597,53356,66227,14753,47986,89858,30075,40395,98629,17142,73763,41998,51960,14163,12808,33186,72197,62342,64482,39815,25881,69880,12308,25338,69446,95197,70375]
,[87762,48631,29496,98673,82273,70847,91496,47327,27175,66668,93200,97212,71224,6825,66542,46198,62742,98507,19460,60154,89480,72347,97455,49196,91136,30641,52875,10239,11773,20744,20997,75931,42517,25594,87335,86965,87538,15071,10099,21836,89541,83028,84120,47402,52302,50255,95583,10530,65406,14632,30141,60801,97478,51898,69088,95343,51984,47046,52653,74222,76970,51471,48726,20043,12519,71411,31124,89924,6212,224,47824,39655,99606,49848,49694,67176,72858,88032,67789,86604,35969,63301,50995,76069,12816,88380,27420,89934,65464,44451,54694,21096,13210,89821,5536,23074,92064,82735,11068,45899])
print(b)