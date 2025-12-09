class Solution:
    
    def reverse_matrix(self, row):
        low = 0
        high = len(row)-1
        while low < high:
            # perform the swap operation
            temp = row[low]
            row[low] = row[high]
            row[high] = temp
            low += 1
            high -= 1
    
    def rotateMatrix(self, matrix):
        # get the numbers of rows and columns

        rows = len(matrix)
        columns = len(matrix[0])
        
        # transpose of matrix

        for row in range(rows):
            for col in range(row):
                if row != col: # as the digonal will be at the same place
                    # perform the swap operation
                    temp = matrix[row][col]
                    matrix[row][col] = matrix[col][row]
                    matrix[col][row] = temp
        
        for row in matrix:
            self.reverse_matrix(row)
    

# main mehtod

if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Create an instance of the Solution class
    sol = Solution()
    
    # Rotate the matrix
    sol.rotateMatrix(arr)
    
    # Print the rotated matrix
    print("Rotated Image:")
    for row in arr:
        print(" ".join(map(str, row)))