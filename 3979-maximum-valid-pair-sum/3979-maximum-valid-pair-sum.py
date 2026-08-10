class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxi = 0
        ans = 0
        for j in range(k, n):
            maxi = max(maxi, nums[j-k])
            ans = max(ans, maxi + nums[j])
        return ans