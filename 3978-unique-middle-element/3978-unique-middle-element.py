class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)
        mid = n // 2

        count = 0

        for i in range(n):
            if nums[i] == nums[mid]:
                count += 1

        return count == 1