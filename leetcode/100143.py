class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ret = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] - ret > 0:
                ret+=1
        return ret 
