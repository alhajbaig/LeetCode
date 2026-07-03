class Solution(object):
    def intersection(self, nums1, nums2):
        s1=set()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]== nums2[j]:
                    s1.add(nums1[i]) 
        l1=list(s1)
        return l1

# the above code is what i initially thought 


# class Solution(object):
#     def intersection(self, nums1, nums2):
#         return list(set(nums1) & set(nums2))