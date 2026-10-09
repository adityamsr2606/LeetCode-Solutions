class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        tot_sub = 1<<n
        result = []
        for num in range(0,tot_sub):
            lst = []
            for i in range(n):
                if num & (1<<i)!=0:
                    lst.append(nums[i])
            result.append(lst)
        return result            
        