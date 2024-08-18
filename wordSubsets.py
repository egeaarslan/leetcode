class Solution(object):
    def wordSubsets(self, words1, words2):
        outputstrings = []
        for element in words1:
            element2 = element
            summ2 = 0
            for word in words2:
                summ = 0
                for letter in word:
                    if letter in element2:
                        print(letter, element2)
                        element2 = element2.replace(letter,"")
                        print(element2)
                        summ += 1
                    else:
                        break
                if summ == len(word):
                    summ2+=1
            if summ2 == len(words2):
                outputstrings.append(element)
        return outputstrings
        
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","oo"]

x = Solution()
print(x.wordSubsets(words1, words2))
