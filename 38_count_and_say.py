"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""

# class Solution(object):
# 	def countAndSay(self, n):
# 		"""
# 		:type n: int
# 		:rtype: str
# 		"""
# 		s = '1'
# 		for _ in range(n-1):
# 			r = []
# 			index = 0
# 			for i in range(len(s)):
# 				if s[i]!=s[index]:
# 					r.append(str(i-index))
# 					r.append(s[index])
# 					index = i
# 			r.append(str(len(s)-index))
# 			r.append(s[index])

# 			s =  ''.join(r)
# 			print s
# 		return s

# class Solution(object):
#     def countAndSay(self, n):
#         """
#         :type n: int
#         :rtype: str
#         """
#         s = '1'
#         for i in range(n-1):
#             count = 1
#             temp = []
#             for index in range(1, len(s)):
#                 if s[index] == s[index-1]:
#                     count += 1
#                 else:
#                     temp.append(str(count))
#                     temp.append(s[index-1])
#                     count = 1
#             temp.append(str(count))
#             temp.append(s[-1])
#             s = ''.join(temp)
#         return s

class Solution(object):
	def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		s = '1'
		for _ in xrange(n-1):
			r = ''
			count = 1
			for i in xrange(1, len(s)):
				if s[i] == s[i-1]:
					count += 1
				else:
					r += str(count) + s[i-1]
					count = 1
			r += str(count) + s[-1]
			s = r
		return s

n = 10
so = Solution()
print so.countAndSay(n)
