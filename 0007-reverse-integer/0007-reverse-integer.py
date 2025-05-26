class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        n = str(abs(x))
        rx = int(n[::-1])
        r = sign * rx

        if r < -2**31 or r > 2**31 - 1:
            return 0

        return r
