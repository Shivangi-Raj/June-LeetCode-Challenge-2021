#https://leetcode.com/problems/minimum-number-of-refueling-stops/

import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel>=target:
            return 0
        stations.append([target, 0])
        pq_passed_stations = []
        tank = startFuel
        ret = 0

        for mile, gas in stations:
            while pq_passed_stations and tank < mile:
                tank += -heapq.heappop(pq_passed_stations)
                ret += 1

            if tank < mile:
                return -1

            heapq.heappush(pq_passed_stations, -gas)

        return ret
