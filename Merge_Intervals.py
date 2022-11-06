class Solution(object):
    def merge(self,intervals):
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]
        print(intervals[0])
        for interval in intervals[1:]:
            if interval[0] <= result[-1][1]:
                print(result[-1][1])
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result
       

            
         