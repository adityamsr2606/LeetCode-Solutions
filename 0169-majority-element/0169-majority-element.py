class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        occur = 0

        for i in nums:
            if count == 0:
                occur = i
            if i == occur:
                count += 1
            else:
                count -= 1
        return occur