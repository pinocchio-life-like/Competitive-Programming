class Solution(object):
    def rearrangeArray(self, nums):
        nums.sort()
        n=len(nums)
        l=0
        r=n-1
        ans=[]
       
        while len(ans)!=n:
            ans.append(nums[l])
            l+=1
            if l<=r:
                ans.append(nums[r])
                r-=1
        return ans
