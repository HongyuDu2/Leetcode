class Solution:
    def reorganizeString(self, s):
        # 统计每个字符的频率
        count = Counter(s)
        # 创建最大堆，用负值来表示频率，以便频率最高的字符在堆顶
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)
        
        result = []
        prev_freq, prev_char = 0, ''
        
        # 构建结果字符串
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            # 将字符添加到结果
            result.append(char)
            
            # 如果之前的字符还有剩余频次，重新放回堆中
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            
            # 更新当前字符的频率和字符，用于下一轮的比较
            prev_freq, prev_char = freq + 1, char  # 因为频率为负数，所以加1使其减少
            
        result_str = ''.join(result)
        
        # 检查生成的字符串是否符合要求
        if len(result_str) != len(s):
            return ""
        
        return result_str