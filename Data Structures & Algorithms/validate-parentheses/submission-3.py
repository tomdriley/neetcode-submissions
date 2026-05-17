class Solution:
    def isValid(self, s: str) -> bool:
        seen = list()
        brackets = "([{)]}" # First three are open, last three are closed, in same order
        for c in s:
            bracket_index = brackets.find(c)
            if bracket_index == -1:
                return False # invalid character
            elif bracket_index < 3:
                # Open bracket_index
                seen.append(c)
            elif bracket_index >= 3:
                matching_char = brackets[bracket_index - 3]
                if len(seen) == 0 or seen.pop() != matching_char:
                    return False
        return len(seen) == 0

        