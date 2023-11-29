class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if len(needle) > len(haystack):
        #     return -1

        # index = -1
        # matches = False
        # for i in range(len(haystack)): 
        #     j = 0
        #     if haystack[i] == needle[j]:
        #         matches = True
        #         index = i
        #         while matches and j < len(needle):
        #             if haystack[i+j] != needle[j]:
        #                 index = -1
        #                 matches = False
        #             j += 1
        #         if matches != False: 
        #             break
        
        # return index

        return haystack.find(needle)
        