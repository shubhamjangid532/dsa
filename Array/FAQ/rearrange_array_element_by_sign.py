class Solution:
    def rearrangeArray(self, nums):
        # get the len of the array
        n = len(nums)

        # if the len is less then two no need to rearrange
        if n < 2:
            return
        # initilizae the two arrays
        pos = []
        neg = []
        
        for idx in range(n):
            if nums[idx] < 0:
                neg.append(nums[idx])
            else:
                pos.append(nums[idx])
        
        # copy the array item back to the existing array
        for idx in range(n//2):
            nums[2*idx] = pos[idx]
            nums[(2*idx)+1] = neg[idx]

        return nums


# main method
if __name__ == "__main__":
    A = [1, 2, -4, -5]
    B = [1, -1, -3, -4, 2, 3]
    C = [-4, 4, -4, 4, -4, 4]
    
    # Create an instance of Solution class
    sol = Solution()
    
    ans_a = sol.rearrangeArray(A)
    ans_b = sol.rearrangeArray(B)
    ans_c = sol.rearrangeArray(C)
    
    # Print the result
    print(" ".join(map(str, ans_a)))
    print(" ".join(map(str, ans_b)))
    print(" ".join(map(str, ans_c)))