class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True
    

"""
Yes. The correct logic for all cases is: return True

If there is at least one odd number, we can make the whole array odd. => For every even number 
x: x - odd = odd
If there are no odd numbers, all numbers are already even..
"""
