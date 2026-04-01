'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        begin = -1
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                begin = i
                break
        
        if begin == -1:
            return -1

         # 初始化油量
        tank = 0
        n = len(gas)

        # 尝试从找到的起点验证是否可以完成一圈
        for i in range(n):
            curr = (begin + i) % n  # 环形路径索引
            tank += gas[curr] - cost[curr]  # 更新当前油量

            if tank < 0:  # 如果油量不足，返回 -1
                return -1
        
        return begin
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        curr = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            if curr < 0:
                start = i + 1
                curr = 0
        return start if total >=0 else -1