class Solution:
    def twoSum(self,nums: list, target: int) -> list:
        for i, num in enumerate(nums):
            for j, number in enumerate(nums):
                if i == j:
                    continue
                if num + number == target:
                    return [i,j]

lst1 = [3,3]

sol = Solution()
print(sol.twoSum(lst1, 6))
