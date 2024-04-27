class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ret = 10*mainTank
        t = (mainTank-1)//4
        ret += 10*min(t,additionalTank)
        return ret