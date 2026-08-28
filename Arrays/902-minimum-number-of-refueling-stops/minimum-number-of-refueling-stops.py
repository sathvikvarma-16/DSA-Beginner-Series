class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []
        fuel = startFuel
        position = 0
        stops = 0
        i = 0
        while fuel < target:
            # Add stations we can currently reach
            while i < len(stations) and stations[i][0] <= fuel:
                heapq.heappush(heap, -stations[i][1])  # i can reach this station, so remember its fuel.
                i += 1
            # No reachable station left
            if not heap:
                return -1
            # Take the station with maximum fuel
            fuel += -heapq.heappop(heap) # I need fuel, so take the biggest fuel from the stations I have already passe
            stops += 1
        return stops

"""
Start with fuel
      ↓
See which stations you can reach
      ↓
Store their fuel in heap
      ↓
Need more fuel?
      ↓
Take the BIGGEST fuel
      ↓
Increase reachable distance
      ↓
Repeat
"""