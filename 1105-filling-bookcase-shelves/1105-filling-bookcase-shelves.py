class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            current_h = 0
            current_w = 0
            for j in range(i, 0, -1):
                w, h = books[j-1]
                current_w += w
                if current_w > shelfWidth:
                    break
                current_h = max(current_h, h)
                dp[i] = min(dp[i], dp[j-1] + current_h)
        return dp[n]
