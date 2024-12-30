# Solution for LeetCode Problem 131: Palindrome Partitioning
# Time Complexity: O(2^n * n), where n is the length of the input string.
# Space Complexity: O(n) for recursion stack.

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Finds all possible palindrome partitions of the input string.

        :param s: Input string to be partitioned.
        :return: List of lists where each inner list represents a palindrome partition.
        """
        result = []  # Stores all valid palindrome partitions
        current = []  # Tracks the current partition being built
        s_len = len(s)  # Length of the input string
        
        def recursive(start: int):
            """
            Recursive backtracking helper function to explore all partitions.

            :param start: Current starting index for partitioning the string.
            """
            # Base case: If start reaches the end of the string, add the current partition
            if start == len(s):
                result.append(current.copy())  # Append the current partition
                return
            
            # Try all possible substrings starting from `start`
            for i in range(start, s_len):
                # Check if the substring is a palindrome
                if self.isValidPali(s[start:i + 1]):
                    current.append(s[start:i + 1])  # Add the substring to the partition
                    recursive(i + 1)  # Recurse for the remaining string
                    current.pop()  # Backtrack to explore other partitions

        # Start recursive exploration from index 0
        recursive(0)
        return result

    def isValidPali(self, s: str) -> bool:
        """
        Checks if a string is a palindrome.

        :param s: Input string to check.
        :return: True if the string is a palindrome, otherwise False.
        """
        i, j = 0, len(s) - 1  # Initialize two pointers
        while i < j:  # Check characters from both ends
            if s[i] != s[j]:  # If mismatch found, not a palindrome
                return False
            i += 1  # Move left pointer to the right
            j -= 1  # Move right pointer to the left
        return True  # All characters matched, it's a palindrome
