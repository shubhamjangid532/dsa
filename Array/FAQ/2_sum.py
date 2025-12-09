class Solution:
    def twoSum(self, nums, target):
        # get the lenght of the array
        n = len(nums)
        hash_map = {}
        for idx in range(n):
            rem = target - nums[idx]
            if rem in hash_map:
                return [hash_map.get(rem), idx]
            hash_map[nums[idx]] = idx
  
# main method
if __name__ == "__main__":
    nums = [1, 6, 2, 10, 3]
    target = 7

    # Create an instance of Solution class
    sol = Solution()

    ans = sol.twoSum(nums, target)

    # Print the result
    print(f"Indices of the two numbers that sum up to {target} are: [{ans[0]}, {ans[1]}]")