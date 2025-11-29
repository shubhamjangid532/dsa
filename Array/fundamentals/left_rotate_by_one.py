class Solution:
    def rotateArrayByOne(self, nums):
        # get the length of the array
        n = len(nums)

        # if length less then 2, array can not be rotated
        if n < 2:
            return nums
        
        # as it should be the last element
        first_item = nums[0]

        for idx in range(n-1):
            nums[idx] = nums[idx+1]

        nums[n-1] = first_item
            
    
# Main method for testing
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    nums_2 = [-1, 0, 3, 6]
    
    solution.rotateArrayByOne(nums)
    solution.rotateArrayByOne(nums_2)
    
    print(f"First array:- {nums}")  # Output the rotated array
    print(f"Second Array{nums_2}")  # Output the rotated array