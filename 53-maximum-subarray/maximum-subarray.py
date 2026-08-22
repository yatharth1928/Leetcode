class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums=0
        maxi=nums[0]
        for num in nums:
            sums=sums+num
            maxi=max(maxi,sums)

            if sums<0:
                sums=0
        return maxi