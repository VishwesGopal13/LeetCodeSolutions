class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        low=min(stations)
        high=sum(stations)+k

        stations = [0]*r + stations + [0]*r
        ressult = low

        def check(mid):
            available = k 
            index = r
            window = sum(stations[:2*r])
            added = defaultdict(int)

            while index < len(stations) - r:
                window += stations[index + r]
                if window < mid:
                    diff = mid - window
                    if diff > available:
                        return False
                    window += diff
                    added[index + r] = diff
                    available -= diff
                
                window -= (stations[index - r] + added[index - r])
                index += 1

            return True

        while low<=high:
            m=(low+high)//2
            if check(m):
                result = m
                low = m+1
            else:
                high = m-1
        return result