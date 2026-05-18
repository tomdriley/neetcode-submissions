class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        pivot = low + (high - low) // 2

        while(nums[pivot] != target):
            if nums[pivot] > target:
                if high != pivot:
                    high = pivot
                else:
                    return -1
            if nums[pivot] < target:
                if low != pivot:
                    low = pivot
                else:
                    return -1
            pivot = low + (high - low) // 2

            if low > high:
                return -1
        
        return pivot