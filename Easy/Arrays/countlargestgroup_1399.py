# Solution for LeetCode Problem 1399: Count Largest Group
# Time Complexity: O(n * d), where n is the input number and d is the number of digits in each number (max 5 for n ≤ 10^4)
# Space Complexity: O(1), using a fixed-size array of length 37 (maximum digit sum is 36)

class Solution:
    def countLargestGroup(self, n: int) -> int:
        count_arr = [0] * 37  # Array to count how many numbers fall into each digit sum group (index = digit sum)
        max_count = 0         # Track the largest size among all groups

        for num in range(1, n + 1):
            digit_sum = 0
            temp = num
            # Compute the digit sum of the current number
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10

            # Update the count of the group corresponding to this digit sum
            count_arr[digit_sum] += 1
            # Update the current maximum group size if necessary
            max_count = max(max_count, count_arr[digit_sum])

        # Count how many groups have the maximum size
        return sum(1 for freq in count_arr if freq == max_count)
