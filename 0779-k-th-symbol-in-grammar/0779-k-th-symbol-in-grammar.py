class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        half = 1 << (n - 2)
        if k <= half:
            return self.kthGrammar(n - 1, k)           # 前半:位置不变
        else:
            return self.kthGrammar(n - 1, k - half) ^ 1  # 后半:位置减half,取反