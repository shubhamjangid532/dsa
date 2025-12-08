class Solution:
    def pascalTriangleRow(self, row):
        ans = [0] * row # to store the answers
        ans[0] = 1 # as every row in pascal triangle start with 1
        # Compute each element in the rth row
        for col in range(1, row):
            ans[col] = (ans[col-1] * (row - col)) // col
        
        return ans  # return the result
    
    def pascalTriangleIII(self, n):
        pascalTriangle = []
        for row in range(1, n+1):
            pascalTriangle.append(self.pascalTriangleRow(row))
        return pascalTriangle
            
        

# main method
if __name__ == "__main__":
    # row number
    n =  6

    # Create an instance of the Solution class
    sol = Solution()  

    # Generate Pascal's Triangle with n rows
    pascalTriangle = sol.pascalTriangleIII(n)

    # Output the Pascal's Triangle
    for row in pascalTriangle:
        for element in row:
            print(element, end=" ")
        print()
