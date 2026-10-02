class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer=[]
        def back(curr,open,close): 
            if len(curr)==2*n:
                answer.append(curr)
                return 
            if open<n:
                back(curr+'(',open+1,close)
            if close<open:
                back(curr+')',open,close+1)
        
        back("",0,0)
        return answer
