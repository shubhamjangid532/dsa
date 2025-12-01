class Solution:
    def intersectionArray(self, nums1, nums2):
        # List to store the intersection elements
        ans = []  

         # Pointers for nums1 and nums2
        i, j = 0, 0 

        # Traverse both arrays using two pointers approach
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums2[j] < nums1[i]:
                j += 1
          # nums1[i] == nums2[j]
            else:  
                ans.append(nums1[i])
                i += 1
                j += 1

        return ans
        
        
# main method
if __name__ == "__main__":
  nums1 = [1, 2, 3, 3, 4, 5, 6, 7]
  nums2 = [3, 3, 4, 4, 5, 8]

  # Create an instance of the Solution class
  finder = Solution()

  # Get intersection of nums1 and nums2 using class method
  ans = finder.intersectionArray(nums1, nums2)

  print("Intersection of nums1 and nums2 is:")
  print(ans)