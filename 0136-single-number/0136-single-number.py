class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number = 0

        for number in nums:
            single_number = single_number ^ number

        return single_number