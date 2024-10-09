class Solution:
    def isPalindrome(self, x: int) -> bool:   
        imported_int = x
        if x <0 :
            return (False)
        
        output = 0
        while x >= 1:
            output = output + x % 10
            output = output * 10
            x = x // 10
        output = output // 10
        # print( output )
        
        if output == imported_int:
            return True
        else: return False
    
