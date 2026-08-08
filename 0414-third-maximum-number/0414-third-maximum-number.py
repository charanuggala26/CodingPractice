class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        count=1
        if len(nums)<3:
            return nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]!=nums[i+1]:
                count+=1
            if count==3 :
                return nums[i]
            if i==0:
                return nums[-1]