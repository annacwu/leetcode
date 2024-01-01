class Solution(object):
    def findContentChildren(self, g, s):

        g.sort()
        s.sort()
        gInd = 0
        sInd = 0
        count = 0
        while gInd < len(g) and sInd < len(s):
            i = g[gInd]
            if s[sInd] >= i:
                gInd += 1
                sInd += 1
                count += 1
            else: 
                sInd += 1

        return count


        # failed 12/21 testcase
        # dp = {}
        # count = 0
        # for i in s:
        #     if i in dp:
        #         dp[i] += 1
        #     else: 
        #         dp[i] = 1

        # for i in g: 
        #     if i in dp:
        #         if dp[i] > 0:
        #             dp[i] -= 1
        #             count += 1
            
        # return count
        