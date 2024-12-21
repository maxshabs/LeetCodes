# Solution for LeetCode Problem 76: Minimum Window Substring
# Time Complexity: O(n), where n is the length of the input string `s`
#   - Each character in `s` is processed at most twice: once when added and once when removed from the window.
# Space Complexity: O(m), where m is the number of unique characters in `t`
#   - The dictionary `t_dict` stores character frequencies of `t`.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # The number of characters from `t` that need to be matched
        need = len(t)

        # A tuple to store the start and end indices of the minimum window
        window_indices = (0, float("inf"))

        # A dictionary to store the character counts of `t`
        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        # Sliding window pointers
        left = 0

        # Iterate through `s` with the `right` pointer
        for right in range(len(s)):
            cur_char = s[right]

            # If the current character is in `t`, update the frequency in `t_dict` and decrement `need`
            if cur_char in t_dict:
                t_dict[cur_char] -= 1
                if t_dict[cur_char] >= 0:
                    need -= 1

            # If all characters in `t` are matched
            if need == 0:
                # Shrink the window from the left to find the smallest valid window
                while True:
                    if s[left] in t_dict:
                        if t_dict[s[left]] == 0:
                            break
                        else:
                            t_dict[s[left]] += 1
                    left += 1

                # Update the minimum window if the current window is smaller
                if right - left + 1 < window_indices[1] - window_indices[0] + 1:
                    window_indices = (left, right)

                # Adjust the window for the next iteration
                t_dict[s[left]] += 1
                left += 1
                need += 1

        # Return the result
        if window_indices[1] > len(s):
            return ""
        else:
            return s[window_indices[0]: window_indices[1] + 1]
