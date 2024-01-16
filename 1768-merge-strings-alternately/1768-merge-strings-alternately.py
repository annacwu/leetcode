class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        string = ""
        length = min(len(word1),len(word2))
        for i in range(length):
            string += word1[i]
            string += word2[i]
        if len(word1) > len(word2):
            string += word1[length:]
        elif len(word1) < len(word2): 
            string += word2[length:]

        return string

