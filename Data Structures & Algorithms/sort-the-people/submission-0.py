class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sort = {}
        for index, value in enumerate(names):
            sort[heights[index]] = value
        new = sorted(sort.keys(), reverse=True)
        return [sort[value] for value in sorted(sort.keys(), reverse=True)]
        
         
    