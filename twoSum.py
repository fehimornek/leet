class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # O(N) complexity using hash tables
    def twoSum_optimized(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_set:
                return [hash_set[target - nums[i]], i]
            hash_set[nums[i]] = i