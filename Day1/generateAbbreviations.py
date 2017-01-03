ass Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]

        ['w',],[1]

        """

        ans = [[]]
        for c in word:
            new_ans = []
            for l in ans:

                new_ans.append(l + [c])

                if len(l) > 0 and l[-1].isdigit():
                    l[-1] = str(int(l[-1]) + 1)
                    new_ans.append(l)
                else:
                    new_ans.append(l + ['1'])
            ans = new_ans

        return [''.join(x) for x in ans]
a = Solution()
print a.generateAbbreviations('word')
