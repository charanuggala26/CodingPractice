class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i,j=0,n-1
        while i<j:
            while nums[i]%2==0 and i<n-1:
                i+=1
            while nums[j]%2!=0 and j>0:
                j-=1
            if i<j:
                nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        return nums