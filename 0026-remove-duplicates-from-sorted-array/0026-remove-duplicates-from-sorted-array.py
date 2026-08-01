class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        my_dict = {}
        for i in range (n):
            my_dict[nums[i]] = 0

        j = 0
        for k in my_dict:
            nums[j] = k
            j+=1
        return j        
        