class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    result.append(nums2[j])
                    nums2[j]=None
                    break
        return result