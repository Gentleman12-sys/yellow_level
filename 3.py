from typing import List

class Solution(object):    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])           
        result = []
        for interval in intervals:
            if result == [] or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])                
        return result
    
print(Solution().merge([[1,3],[2,6],[8,10],[9,18]]))