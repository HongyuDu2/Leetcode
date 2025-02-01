class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0
        max_diagonal = 0
        
        for rect in dimensions:
            length, width = rect
            diagonal = length ** 2 + width ** 2
            
            if diagonal > max_diagonal:
                max_diagonal = diagonal
                max_area = length * width
            elif diagonal == max_diagonal:
                current_area = length * width
                if current_area > max_area:
                    max_area = current_area
        
        return max_area


        