class Solution:
    def searchInsert(self, nums:list, target: int):
        if target in nums:
            return nums.index(target)
        elif target not in nums:
            for i in nums:
                if i == nums[-1] and len(nums) != 1:
                    nums.insert(nums.index(i)+1, target)
                    return nums.index(target)
                elif i < target:
                    prev_num_index = nums.index(i)
                    nums.insert(prev_num_index, target)
                    return nums.index(target)
                elif i > target:
                    nums.insert(0, target)
                    print(nums)
                    return nums.index(target)

