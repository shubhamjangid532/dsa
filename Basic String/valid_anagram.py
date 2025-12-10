class Solution:    
    def anagramStrings(self, s, t):
        if len(s) != len(t):
            return False
        hash_map1 = {}
        hash_map2 = {}

        for idx, ch in enumerate(s):
            hash_map1[ch] = hash_map1.get(ch, 0) + 1 
            hash_map2[t[idx]] = hash_map2.get(t[idx], 0) + 1
            
        return hash_map1 == hash_map2


# Main Method
if __name__ == "__main__":
    solution = Solution()
    str1 = "INTEGER"
    str2 = "TEGERNI"
    result = solution.anagramStrings(str1, str2)
    print("True" if result else "False")