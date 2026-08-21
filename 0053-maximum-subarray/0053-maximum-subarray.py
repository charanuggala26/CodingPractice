class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        g_max=float('-inf')
        current_max=float('-inf')
        for i in range(len(nums)):
            current_max=current_max+nums[i]
            if current_max<nums[i] :
                current_max=nums[i]
            if current_max>g_max:
                g_max=current_max
        return g_max