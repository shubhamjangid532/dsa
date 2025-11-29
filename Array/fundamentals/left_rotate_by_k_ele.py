class Solution:
    
    def reverse_array(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    def rotateArray(self, nums, k: int) -> None:
        # lenght of nums 
        n = len(nums)
        
        # to get the number of rotation
        k = k % n
        
        # first roate the array by k place
        self.reverse_array(nums, 0, k-1)

        # revers element from k to lenght of the array
        self.reverse_array(nums, k, n-1)

        # now rotate the complete array
        self.reverse_array(nums, 0, n-1)

    
# main class
    
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    k = 2

    nums_2 = [3, 4, 1, 5, 3, -5]
    k_2 = 8

    sol = Solution()

    sol.rotateArray(nums, k)
    sol.rotateArray(nums_2, k_2)

    print(f"Array after rotating elements by {k} places:- {nums}")
    print(f"Array after rotating elements by {k_2} places:- {nums_2}")


