class Solution:
    def spiralOrder(self, matrix):
        ans = []
        no_rows = len(matrix)
        no_columns = len(matrix[0])

        top, bottom = 0, no_rows - 1

        left, right = 0, no_columns - 1

        while top <= bottom and left <= right:
            
            # travers left to right
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top += 1

            # travers top to bottom
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right -= 1

            # travers right to left
            if top <= bottom:
                for i in range(right, left-1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            
            # travers bottom to top
            if left <= right:
                for i in range(bottom, top-1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans

# main method
if __name__ == "__main__":
    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    
    # Create an instance of the Solution class
    finder = Solution()
    
    # Get spiral order using class method
    ans = finder.spiralOrder(mat)

    print("Elements in spiral order are:", ans)