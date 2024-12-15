# Solution for LeetCode Problem 3: Longest Substring Without Repeating Characters
# Time Complexity: O(n), where n is the length of the input string `s`
#   - Each character is processed at most twice: once when added to the set and once when removed.
# Space Complexity: O(n), due to the space needed to store characters in the set.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # A set to store unique characters in the current substring
        cur_dict = set()

        # Variable to store the length of the longest substring found
        longest_sub = 0

        # j is the left pointer of the sliding window
        j = 0

        # Iterate through the string with the right pointer i
        for i in range(len(s)):
            # If s[i] is already in the set, remove characters from the left until it's unique
            while s[i] in cur_dict:
                cur_dict.remove(s[j])
                j += 1

            # Add the current character to the set
            cur_dict.add(s[i])

            # Update the length of the longest substring
            longest_sub = max(longest_sub, i - j + 1)

        # Return the length of the longest substring found
        return longest_sub
