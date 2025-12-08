class Solution:
    def pascalTriangleII(self, row):
        
        ans = [0] * row # to store the answers
        ans[0] = 1 # as every row in pascal triangle start with 1
        # Compute each element in the rth row
        for col in range(1, row):
            ans[col] = (ans[col-1] * (row - col)) // col
        
        return ans  # return the result

# main method
if __name__ == "__main__":
    # row number
    row = 6 

    # Create an instance of the Solution class
    sol = Solution()  

    # Function call to return the rth row of Pascal's triangle
    ans = sol.pascalTriangleII(row)

    # Output
    print(f"Row {row}: ", end="")
    print(*ans)
