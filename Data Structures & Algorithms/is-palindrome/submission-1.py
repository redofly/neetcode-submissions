import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_text = re.sub(r"[^a-zA-Z0-9]", "", s)[::-1]
        new_s = re.sub(r"[^a-zA-Z0-9]", "", s)
       
        if reversed_text.lower() == new_s.lower():
            return True
        return False
        