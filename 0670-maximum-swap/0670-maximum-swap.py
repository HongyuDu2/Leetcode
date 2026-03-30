class Solution:
    def maximumSwap(self, num: int) -> int:
        A = list(str(num))
        dist = {int(x) : i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for j in range(9, int(x), -1):
                if dist.get(j, -1) > i:
                    A[i], A[dist[j]] = A[dist[j]], A[i]
                    return int("".join(A))
        return num
