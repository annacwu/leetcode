class Solution(object):
    def countHomogenous(self, s):
        count = 0
        run = 1

        for i in range(1,len(s)): 

            if s[i] == s[i -1]:
                run += 1
            else: 
                count += (run * (run + 1)) // 2
                run = 1
            # x = 1
            # while x < len(s) - i and s[i] == s[i + x]:
            #     count +=1
            #     x += 1

        count += (run * (run + 1)) // 2
        
        return count % (10**9 + 7)