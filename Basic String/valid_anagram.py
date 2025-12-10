class Solution:    
    def anagramStrings(self, s, t):
        if len(s) != len(t):
            return False
        hash_map1 = {}
        hash_map2 = {}

        for idx, ch in enumerate(s):
            if ch in hash_map1:
                hash_map1[ch] += 1
            else:
                hash_map1[ch] = 1
            if t[idx] in hash_map2:
                hash_map2[t[idx]] += 1
            else:
                hash_map2[t[idx]] = 1
        return hash_map1 == hash_map2


# Main Method
if __name__ == "__main__":
    solution = Solution()
    str1 = "INTEGER"
    str2 = "TEGERNI"
    result = solution.anagramStrings(str1, str2)
    print("True" if result else "False")