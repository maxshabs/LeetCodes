# Solution for LeetCode Problem 125: Valid Palindrome
# Time Complexity: O(n), where n is the length of the input string `s`
#   - Both pointers traverse the string at most once.
# Space Complexity: O(1), as no additional data structures are used, and operations are done in place.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers: one starting from the beginning and one from the end
        i = 0
        j = len(s) - 1

        # Step 1: Traverse the string with the two pointers
        while i < j:
            # Skip non-alphanumeric characters from the left pointer
            while i < j and not s[i].isalnum():
                i += 1

            # Skip non-alphanumeric characters from the right pointer
            while i < j and not s[j].isalnum():
                j -= 1

            # Step 2: Compare characters at the pointers, ignoring case
            if s[i].lower() != s[j].lower():
                return False  # If mismatch, the string is not a palindrome

            # Move both pointers closer to the center
            i += 1
            j -= 1

        # Step 3: If all characters matched, the string is a valid palindrome
        return True
