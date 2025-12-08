class Solution:
    def get_nCr(self, n, r):
        # Choose the smaller value for lesser iterations
        if r > n - r:
            r = n-r
         # base case
        if r == 1:
            return n
        
        res = 1  # to store the result 
        
        # Calculate nCr using iterative method avoiding overflow 
        for i in range(r):
            res = res * (n - i)
            res = res // (i + 1)
        
        return res

    def pascalTriangleI(self, r, c):
        return self.get_nCr(r-1, c-1)
    
# main method
if __name__ == "__main__":
    # row number
    r = 5 
    # col number
    c = 3

    # Create an instance of the Solution class
    sol = Solution()

    # Function call to print the element in rth row and cth column 
    ans = sol.pascalTriangleI(r, c)

    print("The element in the rth row and cth column in pascal's triangle is:", ans)
