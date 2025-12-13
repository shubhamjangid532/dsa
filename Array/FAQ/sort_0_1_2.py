class Solution:
    def sortZeroOneTwo(self, nums):
        # brute 
        # nums.sort()

        # Better => as instrcted the nums only have 0,1 and 2
        # n = len(nums)
        # zeros = []
        # onces = []
        # twos = []
        # for idx in range(n):
        #     if nums[idx] == 0:
        #         zeros.append(0)
        #     elif nums[idx] == 1:
        #         onces.append(1)
        #     else:
        #         twos.append(2)

        # idx = 0
        # for _ in zeros:
        #     nums[idx] = 0
        #     idx += 1
        # for _ in onces:
        #     nums[idx] = 1
        #     idx += 1
        # for _ in twos:
        #     nums[idx] = 2
        #     idx += 1

        # Optimal

        # using dutch man flag algoritham
        pass
            



# main method
if __name__ == "__main__":
    nums = [2, 0, 1, 1, 0, 2]
    
    # Create an instance of Solution class
    sol = Solution()
    
    sol.sortZeroOneTwo(nums)
    
    # Print the array elements
    print(" ".join(map(str, nums)))



