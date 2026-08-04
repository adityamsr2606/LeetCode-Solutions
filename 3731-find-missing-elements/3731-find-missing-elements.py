from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        new_list = []

        for i in range(n - 1):
            if nums[i] + 1 != nums[i + 1]:
                for j in range(nums[i] + 1, nums[i + 1]):
                    new_list.append(j)

        return new_list