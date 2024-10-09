class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = numRows
        rows_list = []
        ans = ""
        if rows == 1:
            return s
        else:
            for i in range(rows):
                rows_list.append([])
            
            cycle_frequncy_num = ( rows - 1 ) * 2
            
            for i in range(len(s)):
                for j in range(rows):
                    if i % cycle_frequncy_num == j:
                        rows_list[j].append(s[i])
                        break
                for n in range(rows, cycle_frequncy_num):
                    if i % cycle_frequncy_num == n:
                        for k in range(rows):
                            rows_list[k].append(' ')
                        rows_list[cycle_frequncy_num - n][-1] = s[i]        
            
            for i in range(rows):
                for j in range(len(rows_list[i])):
                    if rows_list[i][j] != " " :
                        ans = ans + rows_list[i][j]
            return ans
                        
            
