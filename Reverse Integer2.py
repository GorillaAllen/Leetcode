class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            x = -x
            flag = True
        
        x = str(x)[::-1]
        x = int(x)
        if flag:
            x = -x
        if x > 2**31-1 or x < -2**31:
            return 0
        return x