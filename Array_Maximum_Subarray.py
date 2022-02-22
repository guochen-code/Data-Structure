''' Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cum=0
        max_sum=nums[0]
        for i in nums:
            cum+=i
            if i>cum:
                cum=i
            max_sum=max(max_sum,cum)
        return max_sum
