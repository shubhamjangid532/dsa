class Solution:
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    sol = Solution()
    print(sol.searchInsert(nums, 5)) # Expected: 2 (Found)
    print(sol.searchInsert(nums, 2)) # Expected: 1 (Insert)
    print(sol.searchInsert(nums, 7)) # Expected: 4 (End)