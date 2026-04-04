class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(S, left, right):
            if len(S) == 2*n:
                res.append(S)
                return
            if right < left:
                backtrack(S + ")", left, right+1)
            if left < n:
                backtrack(S + "(", left+1, right)
        backtrack("", 0, 0)
        return res

