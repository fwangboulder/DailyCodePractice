class Solution(object):

    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        easy,string
        """
        i = 0
        j = 0
        while i < len(abbr):
            if j >= len(word):
                return False
            elif abbr[i].isalpha():
                if word[j] != abbr[i]:
                    return False
                i += 1
                j += 1
            elif abbr[i].isdigit():
                if abbr[i] == '0':
                    return False
                num = ''
                while i < len(abbr) and abbr[i].isdigit():
                    num += abbr[i]
                    i += 1
                j += int(num)
        return j == len(word)
a = Solution()
s = "internationalization"
abbr = "i12iz4n"
print a.validWordAbbreviation(s, abbr)
