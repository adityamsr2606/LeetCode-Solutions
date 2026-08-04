class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        last_small = float("-inf")
        longest = 0
        for i in range (n):
            num = nums[i]
            if num -1 == last_small:
                count += 1
                last_small = num
            elif num!= last_small:   
                count = 1
                last_small = num
            longest = max(longest,count)    
            
        return longest      
        