class Solution:
    def pascalTriangleII(self, r):
        
        ans = [0] * r # to store the answers
        ans[0] = 1 # as every row in pascal triangle start with 1
        # Compute each element in the rth row
        for i in range(1, r):
            ans[i] = (ans[i-1] * (r - i)) // i
        
        return ans  # return the result

# main method
if __name__ == "__main__":
    # row number
    r = 6 

    # Create an instance of the Solution class
    sol = Solution()  

    # Function call to return the rth row of Pascal's triangle
    ans = sol.pascalTriangleII(r)

    # Output
    print(f"Row {r}: ", end="")
    print(*ans)
