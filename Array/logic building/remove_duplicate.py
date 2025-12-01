class Solution:
    def removeDuplicates(self, nums) -> int:
        # get the lenght of the array
        # n = len(nums)

        # i = 0
        # j = i+1

        # while j < n:
        #     if nums[i] == nums[j]:
        #         j += 1
        #     else:
        #         nums[i+1] = nums[j]
                
        #         i += 1
        #         j += 1
        # return i+1

        last_index = 0
        for i in range(1, len(nums)):
            if nums[last_index] != nums[i]:
                last_index += 1
                nums[last_index] = nums[i]
        return last_index+1
        





# main class
if __name__ == "__main__":
    nums_1 = [0, 0, 3, 3, 5, 6]
    
    print(f"Original Array: {nums_1}")
    
    # Create an instance of the Solution class
    sol = Solution()
    
    # Function call to remove duplicates from array
    k = sol.removeDuplicates(nums_1)
    
    print(f"Array after removing the duplicates: {nums_1[:k]}")
    