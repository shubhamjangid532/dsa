class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_con_one = 0
        count = 0

        # find the length of array
        n = len(nums)
        if n < 1:
            return max_con_one
        
        for idx in range(n):
            if nums[idx] == 1:
                count += 1
                max_con_one = max(max_con_one, count)
            else:
                count = 0
        return max_con_one
        

# main funciton
        
if __name__ == "__main__":
    
    # array items
    test_case_1 = [1, 1, 0, 0, 1, 1, 1, 0]

    test_case_2 =[0, 0, 0, 0, 0, 0, 0, 0]
    
    # Craete Solution class Object
    sol = Solution()

    sol_1 = sol.findMaxConsecutiveOnes(test_case_1)

    sol_2 = sol.findMaxConsecutiveOnes(test_case_2)

    print(f"Result of test case 1: {sol_1}")
    print(f"Result of test case 2: {sol_2}")

