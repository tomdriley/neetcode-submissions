class Solution:
    def isPalindrome(self, s: str) -> bool:
        canonical_repr = [c.lower() for c in s if c.isalnum()]
        return canonical_repr == canonical_repr[::-1]