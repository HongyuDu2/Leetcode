class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word_merge = []
        # 遍历两者长度的较小值，交替添加字符
        for i in range(min(len(word1), len(word2))):
            word_merge.append(word1[i])
            word_merge.append(word2[i])
        
        # 将剩余部分追加到结果中
        if len(word1) < len(word2):
            word_merge.extend(word2[i+1:])  # 使用 extend 添加剩余部分
        else:
            word_merge.extend(word1[i+1:])
        
        return ''.join(word_merge)
        