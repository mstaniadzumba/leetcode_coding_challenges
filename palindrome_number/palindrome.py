class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[:] == str(x)[-1::-1]:
            return True
        return False


pal = Solution()
print(pal.isPalindrome(121))
str = '121'
print(str[-1::-1])

