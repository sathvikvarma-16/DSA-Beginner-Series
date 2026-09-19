class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find closest point on rectangle
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        # Distance from circle center to closest point
        dx = xCenter - closestX
        dy = yCenter - closestY

        # Check if point is inside/on circle
        return dx * dx + dy * dy <= radius * radius