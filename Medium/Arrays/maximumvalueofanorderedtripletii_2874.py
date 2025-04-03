class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_dif = 0
        max_i = 0
        result = 0
        for num in nums:
            result = max(result, max_dif * num)
            max_dif = max(max_dif, max_i - num)
            max_i = max(max_i, num)

        return result