# most similar to Split Array Largest Sum.
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low <= high:
            mid = (low + high) // 2
            current = 0
            count = 1
            for weight in weights:
                if current + weight > mid:
                    count += 1
                    current = weight
                else:
                    current += weight
            if count <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low