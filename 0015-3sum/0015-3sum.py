class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        for i in range(n-2):
            if nums[i]==nums[i-1] and i>0:
                continue
            j,k=i+1,n-1
            while j<k:
                s=nums[i]+nums[k]+nums[j]
                if s==0:
                    ans.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:j+=1
                    while j<k and nums[k]==nums[k-1]:k-=1
                    j+=1
                    k-=1
                elif s<0:
                    j+=1
                else:k-=1
        return ans