"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

"""

class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		new_length = 1
		current = nums[0]
		for i in range(len(nums)):
			if current != nums[i]:
				new_length += 1
				current = nums[i]
		return new_length


s = [1,1,2,2,3,3,3,4]
so = Solution()
print so.removeDuplicates(s)