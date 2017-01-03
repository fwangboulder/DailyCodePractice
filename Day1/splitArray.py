class Solution(object):

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        mid=17

        """

        def valid(mid):
            cnt = 0
            current = 0
            for n in nums:
                current += n
                if current > mid:
                    cnt += 1
                    if cnt >= m:
                        # print 'False=',mid
                        return False
                    current = n
            return True

        l = max(nums)
        h = sum(nums)

        while l < h:
            mid = l + (h - l) / 2
            # print l,h,mid
            if valid(mid):
                # print 'True=',mid
                h = mid
            else:
                l = mid + 1
        return l

nums = [7, 2, 5, 10, 8]
m = 2
a = Solution()
print 'result=', a.splitArray(nums, m)

'''
class Solution(object):
    def splitArray(self,nums,m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
	"""
	dp=[[sys.maxint]*m for _ in range(len(nums)+1)]
	#dp[i][0] sum of accumulate # in nums
	#dp[i][1] minimum sum of the larget sum
	add=0
	dp[0][0]=0
	for i in range(1,len(nums)+1):
		add+=nums[i-1]
		dp[i][0]=add
	for j in range(m):
	    dp[0][j]=0
	for i in range(1,len(nums)+1):
	    for i_ in range(i):
	        for j in range(1,m):
		    dp[i][j]=min(dp[i][j],max(dp[i_][j-1],dp[i][0]-dp[i_][0]))
	return dp[len(nums)][m-1]
'''
