class Solution(object):
    def minSetSize(self, arr):
        N=len(arr)
        c=Counter(arr)
        n=0
        output=0
        for k,v in sorted(c.items(), key=lambda x: -x[1]):
            n+=v
            output +=1
            if n>=(N//2): break
        return output
