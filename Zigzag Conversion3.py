class Solution:
    def convert(self, s: str, numRows: int) -> str: 
        if numRows == 1:
            return s
        rows = numRows
        cycle_frequncy_num = ( rows - 1 ) * 2
        ans = ""
        #notice the pattern:
        # 0       8       h   the index that devides by cycle_frequncy_num will be at 1st line
        # 1     7 9     f i   the index that devides by cycle_frequncy_num+1, "1", "i", "9", here will be at 2nd line. "7" & "f" are coming along
        # 2   6   a   e       vice versa
        # 3 5     b d         vice versa
        # 4       c           the index that devides by row-1 will be at 1st line
        for i in range(len(s)):
            if i % cycle_frequncy_num == 0:
                ans = ans + s[i]
        
        for j in range(1, rows-1):
            for i in range(len(s)):
                if i % cycle_frequncy_num == j:
                    ans = ans + s[i]
                    if i + cycle_frequncy_num - (j*2) < len(s):
                        ans = ans + s[i + cycle_frequncy_num - (j*2)]
                    
        for i in range(len(s)):
            if i % cycle_frequncy_num == rows-1:
                ans = ans + s[i]
        return ans


    
