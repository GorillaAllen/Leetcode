s = "0123456789abcdefhi"
rows = 5
rows_list = []
ans = ""
if rows == 1:
    print (s)
else:
    # treat every line as a list. append into lists by append()
    for i in range(rows):
        rows_list.append([])
    
    cycle_frequncy_num = ( rows - 1 ) * 2
    
    for i in range(len(s)):
        #for vertical lines
        for j in range(rows):
            if i % cycle_frequncy_num == j:
                rows_list[j].append(s[i])
                rows_list[j].append(' ')
                break
        # if i % cycle_frequncy_num == 0:
        #     rows_list[0].append(s[i])
        #     rows_list[0].append(' ')
        # if i % cycle_frequncy_num == 1:
        #     rows_list[1].append(s[i])
        #     rows_list[1].append(' ')
        # if i % cycle_frequncy_num == 2:
        #     rows_list[2].append(s[i])
        #     rows_list[2].append(' ')
        # if i % cycle_frequncy_num == 3:
        #     rows_list[3].append(s[i])
        #     rows_list[3].append(' ')
        
        #for tilted lines
        for n in range(rows, cycle_frequncy_num):
            if i % cycle_frequncy_num == n:
                for k in range(rows):
                    rows_list[k].append(' ')
                rows_list[cycle_frequncy_num - n][-1] = s[i]        
                for m in range(rows):
                    rows_list[m].append(' ')
                    
            
            # if i % cycle_frequncy_num == 4:
            #     for k in range(rows):
            #         rows_list[k].append(' ')
            #     rows_list[2][-1] = s[i]        
            #     for m in range(rows):
            #         rows_list[m].append(' ')
                    
            # if i % cycle_frequncy_num == 5:
            #     for k in range(rows):
            #         rows_list[k].append(' ')
            #     rows_list[1][-1] = s[i] 
            #     for m in range(rows):
            #         rows_list[m].append(' ')
    
    # for i in range(rows):
    #     for j in range(len(rows_list[i])):
    #         if rows_list[i][j] != " " :
    #             ans = ans + rows_list[i][j]
    # print(ans)
                
    for j in range(rows):
        for i in range(len(rows_list[j])):
            print(rows_list[j][i],end = "")
        print()
    # for i in range(len(rows_list[0])):
    #     print(rows_list[0][i],end = "")
    # print()
    # for i in range(len(rows_list[1])):
    #     print(rows_list[1][i],end = "")
    # print()
    # for i in range(len(rows_list[2])):
    #     print(rows_list[2][i],end = "")
    # print()
    # for i in range(len(rows_list[3])):
    #     print(rows_list[3][i],end = "")
    # print()
    
