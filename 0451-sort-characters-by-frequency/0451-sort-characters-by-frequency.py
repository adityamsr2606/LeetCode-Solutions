class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        result = ""

        for char, freq in sorted(count.items(), key=lambda x: x[1], reverse=True):
            result += char * freq

        return result