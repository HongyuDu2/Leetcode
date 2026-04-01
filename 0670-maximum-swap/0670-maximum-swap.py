class Solution:
    def maximumSwap(self, num: int) -> int:
        A = list(str(num))
        max_pos = {int(x):i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for j in range(9, int(x), -1):
                if max_pos.get(j,-1) > i:
                    A[i], A[max_pos[j]] = A[max_pos[j]], A[i]
                    return int("".join(A))
        return num