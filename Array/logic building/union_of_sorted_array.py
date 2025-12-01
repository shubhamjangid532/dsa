class Solution:
    def unionArray(self, nums1, nums2):
        ans = []

        # get the lenght of both the given arrays
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)

        # pointer variable initilizations
        i = 0
        j = 0

        # check for the array element present in both the array
        while i < len_nums1 and j < len_nums2:
            if nums1[i] < nums2[j]:
                item_to_insert = nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                item_to_insert = nums2[j]
                j += 1
            else:
                item_to_insert = nums1[i]
                j += 1
                i += 1
            if not len(ans) or ans[-1] != item_to_insert:
                ans.append(item_to_insert)
        
        # insert the remaining elements from nums1
        while i < len_nums1:
            if not len(ans) or ans[-1] != nums1[i]:
                ans.append(nums1[i])
            i += 1
        
        # insert the remaining elements from nums2
        while j < len_nums2:
            if not len(ans) or ans[-1] != nums2[j]:
                ans.append(nums2[j])
            j += 1

        return ans
    
# main method for testing
if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nums2 = [2, 3, 4, 4, 5, 11, 12]

    # Create an instance of the Solution class
    finder = Solution()

    # Get union of nums1 and nums2 using class method
    union = finder.unionArray(nums1, nums2)

    print("Union of nums1 and nums2 is:")
    print(union)