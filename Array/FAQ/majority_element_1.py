class Solution:
    def majorityElement(self, nums):
        majority_element  = None
        count = 0
        for item in nums:
            if count == 0:
                majority_element = item
            if majority_element == item:
                count += 1
            else:
                count -= 1
        return majority_element
                


if __name__ == "__main__":
    arr = [2, 2, 1, 1, 1, 2, 2]
    
    # Create an instance of Solution class
    sol = Solution()
 
    ans = sol.majorityElement(arr)
    
    # Print the majority element found
    print("The majority element is:", ans)
