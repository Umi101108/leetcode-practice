"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
"""

class Solution(object):
	def isPowerOfThree(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		while n>1  :
			if n%3 != 0:
				return False
			n = n/3
		return n == 1

n = 270
so = Solution()
print so.isPowerOfThree(n)

