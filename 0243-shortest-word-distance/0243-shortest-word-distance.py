class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        for i in range(0, len(wordsDict)):
            if wordsDict[i] == word1:
                pos1 = i
                break
        for i in range(0, len(wordsDict)):
            if wordsDict[i] == word2:
                pos2 = i
                break
        output = abs(pos1 - pos2)
        s1, s2 = pos1, pos2
        for j in range(min(pos1, pos2), len(wordsDict)):
            if wordsDict[j] == word1:
                s1 = j
                output = min(output, abs(s1 - s2))
            if wordsDict[j] == word2:
                s2 = j
                output = min(output, abs(s1 - s2))
        return output
