class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1,1]]
        
        output = [[1], [1,1]]
        for i in range(2, numRows):
            res = []
            for j in range(0, i-1):
                res.append(output[i-1][j]+output[i-1][j+1])
            res.append(1)
            res.insert(0,1)
            output.append(res)
        
        return output
