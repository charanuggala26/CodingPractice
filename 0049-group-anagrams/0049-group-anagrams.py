class Solution:
    def groupAnagrams(self, nums: List[str]) -> List[List[str]]:
        dic={}
        for i in range(len(nums)):
            ns=str(sorted(nums[i]))
            if ns in dic:
                dic[ns].append(nums[i])
            else:
                dic[ns]=[nums[i]]
        main=[]
        for i in dic:
            main.append(dic[i])

        return main