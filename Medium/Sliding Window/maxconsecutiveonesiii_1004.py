class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_size = cur_size = i = 0
        nums_len = len(nums)
        while i < nums_len:
            if nums[i] == 0 and k > 0:
                k -= 1
                cur_size += 1
            elif nums[i] == 1:
                cur_size += 1
            elif nums[i] == 0 and k == 0 and cur_size > 0:
                if nums[i - cur_size] == 0:
                    k += 1
                    cur_size -= 1
                else:
                    cur_size -= 1
                continue
            max_size = max(max_size, cur_size)
            i += 1
        return max_size