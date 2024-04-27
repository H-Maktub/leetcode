from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        total = total = sum(c for c, g in zip(customers, grumpy) if g == 0)
        mmax = increase = sum(c * g for c, g in zip(customers[:minutes], grumpy[:minutes]))
        for i in range(minutes,n):
            increase += customers[i] * grumpy[i] - customers[i - minutes] * grumpy[i - minutes]
            mmax = max(mmax,increase)
        return total+mmax