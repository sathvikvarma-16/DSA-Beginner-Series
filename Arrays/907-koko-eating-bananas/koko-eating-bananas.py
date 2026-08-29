class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1 # minimum possible speed
        high = max(piles) # maximum needed speed -> biggest pile
        while low <= high:
            mid = (low + high) // 2 # middle speed
# suppose low = 1, high = 11 Then : mid = 6 We're asking : Can Koko eat everything at speed 6 bananas/hour within 8 hours?
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid   # ceil(a/b) = (a+b-1)//b
            if hours <= h:
                high = mid - 1      # Try a smaller speed
            else:
                low = mid + 1       # Need a higher speed
        return low
