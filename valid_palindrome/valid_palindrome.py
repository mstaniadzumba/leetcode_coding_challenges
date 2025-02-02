class Solution:
    def isPalindrome(self, s: str) -> bool:
        for char in s:
            if not char.isalnum():
                s = s.replace(char, '')
        s = ''.join(s).lower()
        print(s)
       
        if s[0:] == s[-1::-1]:
            return True
        return False

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))