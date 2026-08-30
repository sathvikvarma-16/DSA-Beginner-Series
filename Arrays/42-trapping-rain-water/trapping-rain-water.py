class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = []
        maxleft = 0
        for i in range(len(height)):
            maxl.append(maxleft)
            maxleft = max(maxleft,height[i])
        maxr = []
        maxright = 0
        for i in range(len(height)-1,-1,-1):
            maxr.append(maxright)
            maxright = max(maxright,height[i])
        maxr.reverse()
        total = 0
        for i in range(len(height)):
            value = min(maxl[i],maxr[i])-height[i]
            if value > 0:
                total+=value
        return total
            