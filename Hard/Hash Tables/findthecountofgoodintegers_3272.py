# Solution for LeetCode Problem 3272: Count Palindromic Integers Divisible by K
# Time Complexity: O(10^(n//2) * n), since we iterate over all palindromic templates of length n
# Space Complexity: O(1e4) for factorials and digit frequency tracking

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # Precompute factorials up to n for permutation calculation
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        def count_permutations(freq, total_len):
            # Calculate total permutations of digits given their frequency
            res = fact[total_len]
            for i in range(10):
                f = freq[i]
                if f > 1:
                    res //= fact[f]
            return res

        def count_leading_zero(freq, total_len):
            # Count how many permutations have a leading zero
            if freq[0] == 0:
                return 0
            freq[0] -= 1
            res = fact[total_len - 1]
            for i in range(10):
                f = freq[i]
                if f > 1:
                    res //= fact[f]
            freq[0] += 1  # Restore the count after use
            return res

        def digits_to_number(digits):
            # Convert a list of digits to the actual integer
            num = 0
            for d in digits:
                num = num * 10 + d
            return num

        seen = {}     # Tracks already seen digit frequency combinations
        total = 0     # Final answer

        half_len = n // 2
        is_odd = n % 2

        # Determine the valid range for half-digits to generate palindromes
        start = 10 ** (half_len - 1) if half_len > 0 else 0
        end = 10 ** half_len

        # Iterate over all possible first halves of palindromes
        for half in range(start, end):
            half_digits = []
            h = half
            for _ in range(half_len):
                half_digits.append(h % 10)
                h //= 10
            half_digits.reverse()

            if is_odd:
                # If n is odd, try each digit in the middle
                for mid in range(10):
                    full_digits = half_digits + [mid] + half_digits[::-1]
                    num = digits_to_number(full_digits)

                    # Check if the number is divisible by k
                    if num % k != 0:
                        continue

                    # Create a digit frequency key
                    sorted_key = [0] * 10
                    for d in full_digits:
                        sorted_key[d] += 1
                    key_str = ''.join(chr(f + 48) for f in sorted_key)

                    # Skip duplicate digit arrangements
                    if key_str in seen:
                        continue
                    seen[key_str] = True

                    # Count permutations and subtract invalid ones (with leading 0)
                    total_perm = count_permutations(sorted_key, n)
                    leading_zero_perm = count_leading_zero(sorted_key, n)
                    total += total_perm - leading_zero_perm
            else:
                # For even length palindromes
                full_digits = half_digits + half_digits[::-1]
                num = digits_to_number(full_digits)

                if num % k != 0:
                    continue

                sorted_key = [0] * 10
                for d in full_digits:
                    sorted_key[d] += 1
                key_str = ''.join(chr(f + 48) for f in sorted_key)

                if key_str in seen:
                    continue
                seen[key_str] = True

                total_perm = count_permutations(sorted_key, n)
                leading_zero_perm = count_leading_zero(sorted_key, n)
                total += total_perm - leading_zero_perm

        return total
