class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_s = set(nums)
        if len(nums_s) != len(nums):
            return True
        return False