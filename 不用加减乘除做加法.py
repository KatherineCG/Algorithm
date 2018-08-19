class Solution:
    def Add(self, num1, num2):
        if num2 == 0:
            return num1
        while num2 != 0:
            sum = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = sum
            num2 = carry
        return sum
test = Solution()
print test.Add(2,0)