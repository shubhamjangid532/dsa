class Solution:
    def largestElement(self, nums):
        # lenght of the array
        n = len(nums)
        # let's assume first element is largest element 
        lar_ele = nums[0]
        
        # if len is 1 the first element is largest
        if n == 1:
            return lar_ele

        for idx in range(n):
            lar_ele = max(nums[idx], lar_ele)

        return lar_ele




# Main function
if __name__ == "__main__":
    nums = [3, 2, 1, 5, 2]

  # Create an instance of the Solution class
    sol = Solution()
    
    largest = sol.largestElement(nums)
    print(largest)