class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        buff = set()

        for i in range(0, len(nums)):
            if nums[i] in buff:
                return True
            else:
                buff.add(nums[i])

        return False
                