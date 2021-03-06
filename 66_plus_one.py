"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        for i in range(l):
            if digits[l-i-1] < 9:
                digits[l-i-1] += 1
                break
            digits[l-i-1] = 0

        if digits[0] == 0:
            digits.insert(0,1)
        return digits


digits = [9, 8, 8]

so = Solution()
print so.plusOne(digits)
