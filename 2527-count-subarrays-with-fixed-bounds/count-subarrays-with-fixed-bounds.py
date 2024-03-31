class Solution:
    def countSubarrays(self, nums, mink, maxK):
        result = 0
        last_out_of_range = last_mink = last_maxK = -1

        for i, num in enumerate(nums):
            if num < mink or num > maxK:
                last_out_of_range = i
            if num == mink:
                last_mink = i
            if num == maxK:
                last_maxK = i

            if last_mink > last_out_of_range and last_maxK > last_out_of_range:
                result += min(last_mink, last_maxK) - last_out_of_range

        return result