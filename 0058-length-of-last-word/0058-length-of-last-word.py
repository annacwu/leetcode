class Solution(object):
    def lengthOfLastWord(self, s):
        """
        Given a string s consisting of words and spaces, return the length of the   last word in the string.

        A word is a maximal substring consisting of non-space characters only.
        """
        sentence = []
        word = ''
        for character in s: 
            if character == " ":
                if word != '':
                    sentence.append(word)
                word = ''
            else: 
                word += character
        if word != '':     
            sentence.append(word)
        
        print(sentence)

        return len(sentence[-1])
        