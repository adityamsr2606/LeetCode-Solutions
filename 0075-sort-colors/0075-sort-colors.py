class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        count = [0] * 3
        for i in range(n):
            if nums[i] == 0:
                count[0] += 1
            elif nums[i] == 1:
                count[1] += 1
            else:
                count[2] += 1
        i = 0
        for j in range(3):
            while count[j] > 0:
                nums[i] = j
                i += 1
                count[j] -= 1