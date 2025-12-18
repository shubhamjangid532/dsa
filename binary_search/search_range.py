class Solution:
    def searchRange(self, nums, target):
        
        def findFirst(nums, target):
            low = 0
            high = len(nums)
            first = -1

            while low <= high:
                mid = (low+high)//2
                if nums[mid] == target:
                    first = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first
            
        def findLast(nums, target):
            low = 0
            high = len(nums) - 1
            last = -1

            while low <= high:
                mid = (low+high)//2
                if nums[mid] == target:
                    last = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last
        
        start = findFirst(nums, target)
        if start == -1:
            return [-1, -1]
        end = findLast(nums, target)
        return [start, end]

if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    sol = Solution()
    print(sol.searchRange(nums, 8)) # Expected: [3, 4]
    print(sol.searchRange(nums, 6)) # Expected: [-1, -1]