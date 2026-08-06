class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_list = sorted(heights)
        count = 0
        for i, h in enumerate(heights):
            if h != new_list[i]:
                count += 1
            else:
                pass
        return count        