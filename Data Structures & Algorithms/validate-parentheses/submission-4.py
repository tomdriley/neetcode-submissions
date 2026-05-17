class Solution:
    def isValid(self, s: str) -> bool:
        seen = list()
        open_brackets = "([{"
        closed_brackets = ")]}"
        for c in s:
            if c in open_brackets:
                # Open bracket_index
                seen.append(c)
            elif c in closed_brackets:
                bracket_index = closed_brackets.find(c)
                matching_char = open_brackets[bracket_index]
                if len(seen) == 0 or seen.pop() != matching_char:
                    return False
            else:
                return False
        return len(seen) == 0

        