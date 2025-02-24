import typing

class Solution:
    def missingNumber(self, nums: list) -> int:
        nums.sort()
        for i in range(min(nums),len(nums)+1):
            if i not in nums:
                return i
sol = Solution()
print(sol.missingNumber([1,2,4]))