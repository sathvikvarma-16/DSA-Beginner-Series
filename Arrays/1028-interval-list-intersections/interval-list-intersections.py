class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])  # Later start
            end = min(firstList[i][1], secondList[j][1])  # Earlier end
            if start <= end:  # Overlap exists
                ans.append([start, end])
            if firstList[i][1] < secondList[j][1]:  # First interval ends first
                i += 1
            else:  # Second interval ends first
                j += 1
        return ans