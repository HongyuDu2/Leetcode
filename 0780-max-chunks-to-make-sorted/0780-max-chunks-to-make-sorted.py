class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        number = 0
        list = []
        for i in range(len(arr)):
            list.append(arr[i])
            if max(list) == i:
                number += 1
        return number
