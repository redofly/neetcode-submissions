class Solution:
    def countSeniors(self, details: List[str]) -> int:
        old = 0
        for word in details:
            if int(word[11:13]) > 60:
                old += 1
        return old
       

                
       
        