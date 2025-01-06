# Solution for LeetCode Problem 139: Word Break
# Time Complexity: O(n * m), where:
#   - n is the length of the input string `s`.
#   - m is the total number of characters across all words in `wordDict`.
# Space Complexity: O(n), where n is the length of the input string `s`.
#   - The `arr` array uses O(n) space.

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Determines if the string `s` can be segmented into a sequence of one or more words from `wordDict`.
        
        :param s: A non-empty string to be segmented.
        :param wordDict: A list of non-empty strings representing the word dictionary.
        :return: True if `s` can be segmented, otherwise False.
        """
        s_len = len(s)
        # Create a DP array initialized to False
        arr = [False] * (s_len + 1)
        # The empty string can always be segmented
        arr[s_len] = True
        
        # Traverse the string from the end to the beginning
        for i in range(s_len - 1, -1, -1):
            # Check each word in the dictionary
            for w in wordDict:
                # If the current substring matches the word and is valid
                if (i + len(w) <= s_len) and (s[i: i + len(w)] == w):
                    arr[i] = arr[i + len(w)]
                
                # Break early if a valid segmentation is found
                if arr[i]:
                    break
        
        # Return the result for the full string
        return arr[0]
