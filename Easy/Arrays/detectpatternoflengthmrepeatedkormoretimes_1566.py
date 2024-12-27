# Solution for LeetCode Problem 1566: Detect Pattern of Length M Repeated K or More Times
# Time Complexity: O(n * m * k), where n is the length of the input array `arr`, m is the pattern length, and k is the number of repetitions.
# - The outer loop iterates through the array of size `n`.
# - The nested loops iterate over `m` and `k` for each starting index.
# Space Complexity: O(1), as no additional data structures are used.

from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        """
        Determines if there exists a pattern of length `m` in the array `arr` that is repeated
        `k` or more times consecutively.

        :param arr: List of integers representing the input array.
        :param m: Length of the pattern to detect.
        :param k: Number of consecutive repetitions required for the pattern.
        :return: True if such a pattern exists, otherwise False.
        """
        # Iterate through the array starting from each index `i`
        for i in range(len(arr)):
            cur_count = 0  # Counter to track if the pattern is repeated `k` times
            j = 0  # Pointer for the current position in the pattern
            
            # Iterate over the pattern length `m`
            while j < m:
                cur_char = arr[i + j]  # Current character in the pattern
                l = 0  # Counter for the repetitions of the pattern
                
                # Check for `k` repetitions of the pattern
                while l < k:
                    # If the index goes out of bounds or the character does not match, break
                    if i + j + m * l >= len(arr) or arr[i + j + m * l] != cur_char:
                        break
                    l += 1
                
                # If the pattern did not repeat `k` times, exit the loop
                if l < k:
                    break
                j += 1
            
            # If we successfully matched `m` characters repeated `k` times, return True
            if j == m:
                return True
        
        # If no such pattern is found, return False
        return False
