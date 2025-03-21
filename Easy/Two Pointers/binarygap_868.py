# Solution for LeetCode Problem 868: Binary Gap
# Time Complexity: O(log N), since converting the number to binary takes log N time (number of bits).
# Space Complexity: O(log N), to store the binary string of the number.

class Solution:
    def binaryGap(self, n: int) -> int:
        """
        Finds the maximum distance between two consecutive 1's in the binary representation of an integer.

        Parameters:
        n (int): The input integer.

        Returns:
        int: The maximum distance between two consecutive 1's in the binary representation of n.
             If there is no such pair, return 0.
        """
        bin_n = str(bin(n))[2:]  # Convert number to binary string and strip the '0b' prefix
        left = -1  # Pointer to store the index of the previous '1'
        max_len = 0  # Variable to track the maximum gap found
        
        # Iterate over the binary string to find gaps between '1's
        for right in range(len(bin_n)):
            if bin_n[right] == '1':
                if left != -1:
                    max_len = max(max_len, right - left)  # Update max gap
                left = right  # Move left pointer to current '1'
        
        return max_len  # Return the maximum gap found
