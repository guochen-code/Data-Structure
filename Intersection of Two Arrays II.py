'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[]
        dict_1={}
        dict_2={}
        for i in nums1:
            if i not in dict_1.keys():
                dict_1[i]=1
            else:
                dict_1[i]+=1
        for i in nums2:
            if i not in dict_2.keys():
                dict_2[i]=1
            else:
                dict_2[i]+=1
        for i in dict_1.keys():
            if i in dict_2.keys():
                count=min(dict_1[i],dict_2[i])
                lst=lst+[i]*count
        return lst
