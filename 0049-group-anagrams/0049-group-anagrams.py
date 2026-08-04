class Solution:
    def groupAnagrams(self, nums: List[str]) -> List[List[str]]:
        main=[]
        i=0
        dic={}
        for k in nums:
            dic[k]=sorted(k)
        while(i<len(nums)):
            check=[]
            j=i+1
            si=sorted(nums[i])
            while(j<len(nums)):
                if si==dic[nums[j]]:
                    check.append(nums[j])
                    nums.pop(j)
                    continue
                j+=1
            check.append(nums[i])
            main.append(check)
            nums.pop(i)
        return main