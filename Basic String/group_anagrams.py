class Solution:
    def groupAnagrams(self, strs):
        groups = {}  # Hash map to store groups of anagrams
        
        # Loop through each word in the input list
        for word in strs:
            freq = [0] * 26  # Frequency array for storing letter counts (26 lowercase English letters)
            
            # Count the frequency of each character in the word
            for c in word:
                freq[ord(c) - ord('a')] += 1
            
            # Create a key based on the frequency array
            key = tuple(freq)
            
            # Group words with the same frequency pattern
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        
        # Return the grouped anagrams as a list of lists
        return list(groups.values())
            


# Main Method
if __name__ == "__main__":
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solution.groupAnagrams(strs)
    print(result)