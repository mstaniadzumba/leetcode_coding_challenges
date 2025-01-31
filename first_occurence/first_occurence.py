class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1
        

l = 'sapbutsap'
n = 'sad'
h = Solution()
print(h.strStr(l,n))