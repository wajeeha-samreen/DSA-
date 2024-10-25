class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Start j from i+1 to avoid duplicate pairs and redundant checks
                if nums[i] + nums[j] == target:
                    return [i, j]
