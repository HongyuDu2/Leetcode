class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        result = ''.join(char * freq for char, freq in sorted_items)
        return result