class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_streak = 0
        streak = 0
        for index, v in enumerate(nums):
                if v != 1:
                    streak = 0
                if v == 1:
                 streak += 1
                 max_streak = max(max_streak, streak)
                
                 
            
            
        
               
        return max_streak

        