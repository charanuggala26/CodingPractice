class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        neg=0
        if x<0:
            neg=1
        x= abs(x)
        while x!=0:
            rev=rev*10+x%10
            x=x//10
        if neg==1:
            rev=rev * -1
        if rev >= (-2**31) and rev <= 2**31-1:
            return rev
        else: return 0