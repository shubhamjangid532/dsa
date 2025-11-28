class Solution:
    def linearSearch(self, nums, target):
        # get the lenght of the array
        n = len(nums)
        if n == 0:
            return -1
        for idx in range(len(nums)):
            if target == nums[idx]:
                return idx
        return -1


# Main function
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    target = 4

    # Create an instance of the Solution class
    sol = Solution()

    # Call the linearSearch method and store the result
    result = sol.linearSearch(nums, target)
   
    print(result)

