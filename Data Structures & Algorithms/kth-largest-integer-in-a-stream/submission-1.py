class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Assume that nums must be at least k-1 elements
        # To make it k, add -1001 which is smaller than the smallest number
        # to the list, which will make the rest work.
        sorted_nums = sorted(nums)
        sorted_nums.insert(0, -1001)
        self.nums = sorted_nums[-k:]

    def add(self, val: int) -> int:
        for i, num in enumerate(self.nums):
            if val < num:
                self.nums.insert(i, val)
                break
        else:
            self.nums.append(val)
        self.nums.pop(0) # Delete smallest val no longer in top k
        return self.nums[0] # New kth largest

        
