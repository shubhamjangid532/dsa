def lengthOfLongestSubstring(s):
    # get the length of the s
    n = len(s)
    
    # intilaize max_count left and charset
    max_count  = 0
    left = 0
    char_set = set()
    
    for right in range(n):
        while s[right] in char_set:
            # remove the item from left until the s[right] char is present in char set
            char_set.remove(s[left])
            left += 1
        # going to add the element form the right
        char_set.add(s[right])
        max_count = max(max_count, len(char_set))
    return max_count

if __name__ == "__main__":
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s)) # Expected: 3