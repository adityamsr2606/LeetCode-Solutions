from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)

        maxi = float("-inf")
        mini = float("inf")

        totalMax = 0
        totalMin = 0

        for i in range(n):
            totalMax = totalMax + nums[i]
            maxi = max(maxi, totalMax)

            if totalMax < 0:
                totalMax = 0

            totalMin = totalMin + nums[i]
            mini = min(mini, totalMin)

            if totalMin > 0:
                totalMin = 0

        return max(maxi, abs(mini))