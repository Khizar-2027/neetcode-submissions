class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Prevhash = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in Prevhash:
                return [Prevhash[diff], i]
            Prevhash[n] = i
        return