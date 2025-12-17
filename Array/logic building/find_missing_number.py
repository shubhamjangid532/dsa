class Solution:
    def missingNumber(self, nums):
        # # find the length of the array
        # n = len(nums)
        
        # # get the sum of of given nnumbers
        # sum_of_nums = sum(nums)

        # # sum of first natural number's
        # natural_number_sum = (n * (n+1)) // 2

        # # reutrn the missing number
        # return natural_number_sum - sum_of_nums


        """
        Initialize two variables xor1, xor2 as 0. xor1 variable will calculate the XOR of 1 to N
        Calculate the XOR of all the elements in the array by xor2 = xor2 ^ arr[i]..
        Finally, the answer will be the XOR of xor1 and xor2.

        Understand that on calculating the XOR of all numbers from 1 to N we make sure that each number is included. 
        After that on calculating the XOR of all the elements in the array & then performing XOR these two results,
          all the numbers present in the final result will appear twice expect for the one which is missing. 
        Hence the number occurring twice turn out 0 satisfying first condition, 
          and then followed by 0 ^ missing number, leaving the missing number itself.
        
        """

        xor_1 = 0
        xor_2 = 0 

        for idx in range(len(nums)):
            xor_1 ^= (idx+1) # XOR upto [1,....,N]
            xor_2 ^= nums[idx] # XOR of Array Elements

        # reutrn of missing number
        return xor_1 ^ xor_2

# Main function to test the implementation
if __name__ == "__main__":
    nums = [0, 1, 2, 4]
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the missingNumber method to find the missing number
    ans = solution.missingNumber(nums)
    
    print(f"The missing number is: {ans}")
