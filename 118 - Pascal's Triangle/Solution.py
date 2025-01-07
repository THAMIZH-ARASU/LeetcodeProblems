class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        triangle = [[1]]
        
        for i in range(1, numRows):
            prev_row = triangle[-1]
            new_row = [1] + [prev_row[j-1] + prev_row[j] for j in range(1, len(prev_row))] + [1]
            triangle.append(new_row)
        
        return triangle
    
if __name__ == '__main__':
    solution = Solution()
    result = solution.generate(6)
    for row in result:
        print(row)