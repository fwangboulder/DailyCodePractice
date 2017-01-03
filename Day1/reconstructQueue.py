class Solution(object):

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
        """
        # sort the list descending by the height and ascending by # of people k
        people.sort(key=lambda x: (-x[0], x[1]))
        for i in range(1, len(people)):

            start = people[i][1]
            # insert the people to the conresponding location k.
            if start != i:
                tmp = people[i]
                while start != i and i != 0:
                    people[i] = people[i - 1]
                    i -= 1
                people[start] = tmp

        return people
# test the progrom
# people=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# self.reconstructQueue(people)
