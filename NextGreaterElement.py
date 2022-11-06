class Solution(object):
    def nextGreaterElement(self,nums1,nums2):
        if not nums1 or not nums2: return []
        result=[]
        nums2_dic={v:i for i ,v in enumerate(nums2)}
        for nums in nums1:
            index=nums2_dic[nums]+1
            while index<len(nums2) and nums>=nums2[index]:
                index+=1
            if index==len(nums2):
                result.append(-1)
            else:
                result.append(nums2[index])
        return result
