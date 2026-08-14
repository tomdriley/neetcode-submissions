class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums_tuple = tuple(nums)
        length_n_subsets = {len(nums):{nums_tuple}}
        print(length_n_subsets)
        for n in reversed(range(len(nums))):
            length_n_subsets[n] = set()
            print(n)
            for subset in length_n_subsets[n+1]:
                for num in subset:
                    candidate = tuple(x for x in subset if x != num)
                    length_n_subsets[n].add(candidate)
        result = []
        for subsets in length_n_subsets.values():
            result += [list(subset) for subset in subsets]
        return result