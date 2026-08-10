class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f,s,t=float('-inf'),float('-inf'),float('-inf')
        for i in range(len(nums)):
            if nums[i]>f and s<nums[i] and t<nums[i]:
                t,s,f=s,f,nums[i]
            elif nums[i]>s and nums[i]>t and nums[i]<f:
                t,s=s,nums[i]
            elif t<nums[i] and nums[i]<s and nums[i]<f: 
                t=nums[i]
        if len(nums)<3 or t==float('-inf'):
            return f
        return t