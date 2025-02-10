class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        df = [0] * n
        powers = [0] * n
        start = 0
        for i, v in enumerate(stations):
            if i < r:
                start += v
            else:
                df[i - r] += v
            if i + r + 1 < n:
                df[i + r + 1] -= v
        
        for i in range(n):
            start += df[i]
            powers[i] = start

        start = min(powers)
        end = start + k + 1

        while start < end:
            mid = (start + end) // 2

            cond = True

            df = [0] * n
            d = 0
            need = 0
            for i in range(n):
                d -= df[i]
                if powers[i] + d < mid:
                    x = mid - powers[i] - d
                    need += x
                    d += x
                    e = i + 2 * r + 1
                    if e < n:
                        df[e] += x
                    if need > k:
                        break
            if need > k:
                end = mid
            else:
                start = mid + 1

        return start - 1