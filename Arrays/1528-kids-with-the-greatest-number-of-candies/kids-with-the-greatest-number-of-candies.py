class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        for i in range(len(candies)):
            maximum=candies[i]+extraCandies
            if maximum>=max(candies):
                ans.append(True)
            else:
                ans.append(False)
        return ans