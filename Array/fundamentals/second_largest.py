class Solution:
    def secondLargestElement(self, nums):
        # assign first largest and second largest with minimum values
        first_largest =  float('-inf')
        second_largest =  float('-inf')
    	
		# get the lenght of the array
        n = len(nums)
    	
        # if lenght of array is less then 2 there is no second largest element
        if n < 2:
           return - 1
        
        for idx in range(n):
            if nums[idx] > first_largest:
                second_largest = first_largest
                first_largest = nums[idx]
            
            elif nums[idx] > second_largest and nums[idx] != first_largest :
                second_largest = nums[idx]
        
        return second_largest if second_largest != float('-inf') else -1
             
          
# main function 
if __name__ == "__main__":
    # nums = [1, 2, 4, 6, 7, 5, 9, 9]

    # nums= [8, 8, 7, 6, 5]
    nums = [10, 10, 10, 10, 10]
    # craete insnace of the Solution class
    sol = Solution()

    second_largest = sol.secondLargestElement(nums)
    print(second_largest)
