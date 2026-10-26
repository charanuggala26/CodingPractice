class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = (''.join(filter(str.isalnum, s))).lower()

        return s2 == s2[::-1]