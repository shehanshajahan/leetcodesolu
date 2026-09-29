class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()

        merged=[]

        for interval in intervals:
            start=interval[0]
            end=interval[1]
            if not merged or start>merged[-1][1]:
                merged.append([start,end])
            else:
                merged[-1][1]=max(merged[-1][1],end)
        return merged 