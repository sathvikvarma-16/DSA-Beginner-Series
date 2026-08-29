class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Answer array, initially all 0
        answer = [0] * len(temperatures)
        # Stack stores INDEXES of days not temperatures
        stack = []
        for i in range(len(temperatures)):
            # If today's temperature is warmer,
            # today's day is the answer for previous colder days
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Get the previous day
                prev = stack.pop()
                # Number of days we waited
                answer[prev] = i - prev
            # Current day is now waiting for a warmer day
            stack.append(i)
        return answer