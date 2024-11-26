# Solution for LeetCode Problem 443. String Compression
# Time Complexity: O(n) where n is the size of the input array
# Space Complexity: O(1) because we're only modifying the input array
class Solution:
    def compress(self, chars: List[str]) -> int:
        chars_len = len(chars)
        i, j = 0, 0
        while i < chars_len:
            cur_count = 0
            cur_char = chars[i]
            while i < chars_len and chars[i] == cur_char:
                cur_count += 1
                i += 1

            chars[j] = cur_char
            if cur_count > 1:
                count_str = str(cur_count)
                for char in count_str:
                    j += 1
                    chars[j] = char
            j += 1
        return j
