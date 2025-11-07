class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        if n <= 0:
            return True

        # 长度为 1 的特判
        if m == 1:
            if flowerbed[0] == 0:
                n -= 1
            return n <= 0

        # 处理开头
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
            if n <= 0:
                return True

        # 处理结尾
        if flowerbed[m - 1] == 0 and flowerbed[m - 2] == 0:
            flowerbed[m - 1] = 1
            n -= 1
            if n <= 0:
                return True

        # 处理中间
        i = 1
        while i < m - 1 and n > 0:
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
                i += 2   # 种完一朵跳过下一格，避免多余判断
            else:
                i += 1

        return n <= 0