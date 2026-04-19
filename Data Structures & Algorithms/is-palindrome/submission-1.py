class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(c.lower() for c in s if c.isalnum())
        return st == st[::-1]