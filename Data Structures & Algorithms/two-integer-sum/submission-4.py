class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            remaining_list = nums[i+1:]
            pair_num = target - num
            if pair_num in remaining_list:
                return list([i, i + 1 + remaining_list.index(target - num)])

