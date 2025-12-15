class Solution:
    def moveZeroes(self, nums):
        # n = len(nums)

        # j = -1

        # # check if we have zero in array or not
        # for i in range(n):
        #     if nums[i] == 0:
        #         j = i
        #         break
        
        # # if there is no zero in array return the array
        # if j == -1:
        #     return 

        # for i in range(j+1, n):
        #     if nums[i] != 0:
        #         nums[j] = nums[i]
        #         nums[i] = 0
        #         j+=1
        
        n = len(nums)
        pos = 0
        for idx in range(n):
            if nums[idx] != 0:
                nums[pos], nums[idx] = nums[idx], nums[pos]
                pos += 1
    

# main class
if __name__ == "__main__":
    nums = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

    # Create an instance of Solution class
    sol = Solution()
    sol.moveZeroes(nums)

    print("Array after moving zeroes:", nums)