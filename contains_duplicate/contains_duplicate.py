class Solution:
    def containsDuplicate(self, nums) -> bool:
        return True if len(nums) != len(set(nums)) else False
        
