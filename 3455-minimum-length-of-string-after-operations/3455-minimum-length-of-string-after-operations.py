class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        removable_len = 0
        freq = [0] * 26

        for char in s:
            freq[ord(char) - ord('a')] += 1

        for frequency in freq:
            if frequency % 2 != 0:
                removable_len += frequency - 1
            elif frequency != 0:
                removable_len += frequency - 2

        return n - removable_len