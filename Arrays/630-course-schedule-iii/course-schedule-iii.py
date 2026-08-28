class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        # Heap stores course durations
        heap = []
        # Total time used
        time = 0
        for duration, deadline in courses:
            # Take this course
            time += duration
            heapq.heappush(heap, -duration)
            # If we missed the deadline
            if time > deadline:
                # Remove the longest course
                longest = -heapq.heappop(heap)
                # Get its time back
                time -= longest
        return len(heap)