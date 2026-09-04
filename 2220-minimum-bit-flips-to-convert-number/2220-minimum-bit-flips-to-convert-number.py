class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_binary = bin(start)[2:]
        goal_binary = bin(goal)[2:]

        max_length = max(len(start_binary), len(goal_binary))

        start_binary = start_binary.zfill(max_length)
        goal_binary = goal_binary.zfill(max_length)

        flips = 0

        for i in range(max_length):
            if start_binary[i] != goal_binary[i]:
                flips += 1

        return flips