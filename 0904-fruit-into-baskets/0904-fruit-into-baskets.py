class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = cur = 0
        last = secondlast = -1
        lastcount = 0
        for f in fruits:
            if f == last or f == secondlast:
                cur += 1
            else:
                cur = lastcount + 1
            if f == last:
                lastcount += 1
            else:
                lastcount = 1
                secondlast = last
                last = f
            ans = max(cur, ans)
        return ans
