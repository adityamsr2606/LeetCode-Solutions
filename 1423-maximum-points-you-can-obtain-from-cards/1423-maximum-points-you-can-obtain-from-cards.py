class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        window = n - k
        if window == 0:
            return total
        left = 0
        right = 0
        curr_sum = 0
        mini = float('inf')
        while right < n:
            curr_sum += cardPoints[right]
            if right - left + 1 == window:
                mini = min(mini, curr_sum)
                curr_sum -= cardPoints[left]
                left += 1
            right += 1
        return total - mini