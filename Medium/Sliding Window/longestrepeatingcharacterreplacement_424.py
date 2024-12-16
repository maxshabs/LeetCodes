# Solution for LeetCode Problem 424: Longest Repeating Character Replacement
# Time Complexity: O(n), where n is the length of the input string `s`
#   - The sliding window traverses the string once, and each character is processed at most twice (once when added, once when removed).
# Space Complexity: O(1), since the frequency dictionary stores at most 26 characters (fixed size).

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Frequency dictionary to store the count of characters in the current window
        freq_dict = {}

        # Maximum frequency of any character in the current window
        max_freq = 0

        # The length of the longest window found
        max_window = 0

        # Left pointer for the sliding window
        left = 0

        # Length of the input string
        len_s = len(s)

        # Iterate through the string with the right pointer
        for right in range(len_s):
            # Update the frequency of the current character at the right pointer
            right_count = freq_dict[s[right]] = freq_dict.get(s[right], 0) + 1

            # Update max_freq to be the highest frequency of any character in the current window
            if max_freq < right_count:
                max_freq = right_count

            # If the current window size minus max_freq exceeds k, shrink the window from the left
            while right - left + 1 - max_freq > k:
                freq_dict[s[left]] -= 1
                left += 1

            # Update the maximum window size found so far
            if max_window < right - left + 1:
                max_window = right - left + 1

        # Return the length of the longest window found
        return max_window
