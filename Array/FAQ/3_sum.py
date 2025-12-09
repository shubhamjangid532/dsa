class Solution:
    def threeSum(self, nums):
        # n = len(nums)
        # triplets = set()

        # for i in range(n-2):
        #     for j in range(i+1, n-1):
        #         for k in range(j+1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = [nums[i], nums[j], nums[k]]
        #                 triplet.sort()
        #                 triplets.add(tuple(triplet))
        # ans = [list(triplet) for triplet in triplets]
        # return ans
        
        # to store the result
        ans = []
        
        # lenght of the array
        n = len(nums)

        # sort the input array
        nums.sort()

        # iterate through the list of array
        for idx in range(n):
            # skip duplicates
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            
            # two pointer approch 
            j = idx + 1
            k = n-1

            while j < k:
              sum_value = nums[idx] + nums[j] + nums[k]

              if sum_value < 0:
                  j += 1
              elif sum_value > 0:
                  k -= 1
              else:
                  # found a triplet that is sum up to target
                  temp = [nums[idx], nums[j], nums[k]]
                  ans.append(temp)

                  j += 1
                  k -= 1

                  # skip duplicate 
                  while j < k and nums[j] == nums[j - 1]:
                      j += 1
                  while j < k and nums[k] == nums[k + 1]:
                      k -= 1
        return ans

# main method
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]

    # Create an instance of Solution class
    sol = Solution()


    ans = sol.threeSum(nums)

    # Print the result
    for triplet in ans:
        print(f"[{', '.join(map(str, triplet))}]")
    