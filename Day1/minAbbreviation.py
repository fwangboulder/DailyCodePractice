ass Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """

        dictionary = [i for i in dictionary if len(i) == len(target)]
        if not dictionary:
            return str(len(target))

        # calculate the value to represent same locations
        maps = []
        for i in dictionary:
            mask = 0
            for j in xrange(len(target)):
                if target[j] == i[j]:
                    mask |= (1 << j)
            maps.append(mask)

        res = target
        for i in xrange(1 << len(target)):
            for j in maps:
                # This means same abbr
                if i & j == i:
                    break

            # this is just to construct the abbr
            else:
                pre = 0
                tmpstr = ""
                for j in xrange(len(target)):
                    if i & (1 << j):
                        if pre < j:
                            tmpstr += str(j - pre)
                        tmpstr += target[j]
                        pre = j + 1
                if pre < len(target):
                    tmpstr += str(len(target) - pre)
                if len(tmpstr) < len(res):
                    res = tmpstr
        return res
# Go back and redo this problems again soon to better understand the idea.
