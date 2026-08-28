class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort events by starting day
        events.sort()
        # Min-heap stores ending days
        heap = []
        # i = which event we are checking
        i = 0 
        # Start from day 1
        day = 1
        # Number of events attended
        ans = 0
        # Continue while events or available events exist
        while i < len(events) or heap:
            # Add all events that have started by today
            while i < len(events) and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1
            # Remove events that already expired
            while heap and heap[0] < day:
                heapq.heappop(heap)
            # If an event is available
            if heap:
                # Attend the event ending earliest
                heapq.heappop(heap)
                # One event attended
                ans += 1
                # Move to the next day
                day += 1
            else:
                # No event available today
                # Jump directly to the next event's start day
                if i < len(events):
                    day = events[i][0]
        return ans
