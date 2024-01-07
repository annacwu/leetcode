class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            temp = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    temp = max(temp, dp[j])
            
            dp[i] = temp + 1
        return max(dp)


        # count = 0
        # run = 1

        # for i in range(1, len(nums) -1): 
        #     if nums[i] > nums[i-1]:
        #         run += 1
        #     else:
        #         if count < run:
        #             count = run
        #         run = 1
        # return count

        