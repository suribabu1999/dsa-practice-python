class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word = []
        first = 0
        second = 0

        while first < len(word1) and second < len(word2):
            word.append(word1[first])
            word.append(word2[second])
            first +=1
            second +=1
        if first < len(word1):
            word.append(word1[first:])
        if second < len(word2):
            word.append(word2[second:])
        return "".join(word)