#too slow
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x = dividend
        y = divisor

        counter = 0
        if y == 1:
            if x > 2**31 - 1:
                return 2**31 - 1
            if x < -2**31:
                return x < -2**31
            else: return x

    
        if y == -1:
            if -1*x > 2**31 - 1:
                return 2**31 - 1
            if -1*x < -2**31:
                return x < -2**31
            return -1*x
 

        if x * y > 0:
            x = abs(x)
            y = abs(y)
            while x >= y:
                x = x - y
                counter += 1
        else:
            x = abs(x)
            y = abs(y)
            while x >= y:
                x = x - y
                counter += 1
            counter = -1 * counter
        return counter