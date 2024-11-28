class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        averages = []
        cur_avg = 0
        for i in range(k):
            cur_avg += nums[i] / k
        averages.append(cur_avg)
        loop_len = len(nums) - (k - 1)
        for i in range(1, loop_len):
            cur_avg -= nums[i - 1] / k
            cur_avg += nums[k + i - 1] / k
            averages.append(cur_avg)
        return max(averages)
