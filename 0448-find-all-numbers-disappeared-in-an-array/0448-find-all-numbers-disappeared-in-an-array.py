class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        my_set = set(nums)
        res = []
        for i in range(1,n + 1):
            if i not in my_set:
                res.append(i)
        return res