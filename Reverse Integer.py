class Solution:
    def reverse(self, x: int) -> int:
        flag_negative = False
        if x < 0:
            flag_negative = True
            x = -x
        # print(x)
        output = 0
        while x >= 1:
            output = output + x % 10
            output = output * 10
            x = x // 10
        output = output // 10
        if flag_negative == True:
            output = output * -1
        if output > 2**31-1 or output < -2**31:
            return 0
        return output