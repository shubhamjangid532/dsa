class Solution:
    def leaders(self, nums):
        leaders = []
        for idx in range(len(nums)-1, -1, -1):
            if not len(leaders):
                leaders.append(nums[idx])
            elif leaders[0] < nums[idx]:
                leaders.insert(0, nums[idx])
        return leaders
        
# main method
if __name__ == "__main__":
    nums = [1, 2, 5, 3, 1, 2]
    # nums= [11]
    # nums = [-3, 4, 5, 1, -4, -5]

    # Create an instance of the Solution class
    finder = Solution()

    # Get leaders using class method
    ans = finder.leaders(nums)

    print("Leaders in the array are: ", end="")
    for leader in ans:
        print(leader, end=" ")
    print()