class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # The key insight I think is that:
        # n XOR n = 0
        # n XOR 0 = n
        # so if we just XOR everything together,
        # all the pairs cancel and we are left 
        # with a single digit

        total = 0

        for num in nums:
            total ^= num

        return total