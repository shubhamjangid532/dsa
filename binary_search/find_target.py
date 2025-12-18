class Solution:
    def search(self, nums, target):
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low+high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    

if __name__ == "__main__":
    nums = [-9109, -6888, -5296, -3183, -1570, -1423, -1186, -380, 813, 2988, 3213, 3497, 3695, 4774, 5519, 6119, 6708, 9245, 9371, 9434, 9517]
    target = -3183
    sol = Solution()
    print(sol.search(nums, target)) # Expected: 4