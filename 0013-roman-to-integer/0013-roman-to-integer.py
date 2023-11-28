class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        final = 0
        vals = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)):
            if i > 0 and vals[s[i]] > vals[s[i - 1]]:
                final += vals[s[i]] - 2*vals[s[i-1]]
            else: 
                final += vals[s[i]]


        # for i in range(0, len(s)): 
        #     if s[i] == "M":
        #         if s[i-1] == 'C':
        #             final -= 200
        #         final += 1000
        #     if s[i] == "D":
        #         if s[i-1] == 'C':
        #             final -= 200
        #         final += 500
        #     if s[i] == "C":
        #         if s[i-1] == 'X':
        #             final -= 20
        #         final += 100
        #     if s[i] == "L":
        #         if s[i-1] == 'X':
        #             final -= 20
        #         final += 50
        #     if s[i] == "X":
        #         if s[i-1] == 'I':
        #             final -= 2
        #         final += 10
        #     if s[i] == "V":
        #         if s[i-1] == 'I':
        #             final -= 2
        #         final += 5
        #     if s[i] == "I":
        #         final += 1

        return final

        
        