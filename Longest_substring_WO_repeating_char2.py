s = "tmmzuxt"
first_repeating_char = ""
index_list_of_repeating = []
loop_count = 0
while True:
    for i in range(0,len(s)):
        if s.count(s[i]) > 1:
            first_repeating_char = s[i]
            break
    for i in range(0,len(s)):
        if s[i] == first_repeating_char:
            index_list_of_repeating.append(i)
            if len(index_list_of_repeating) == 2:
                break
    if len(index_list_of_repeating) == 0:
        print("no repeated char")
        break
    if  index_list_of_repeating[0] >= len(s) - 1 - index_list_of_repeating[1]:
        s = s[0:index_list_of_repeating[1]]
    else:
        s = s[index_list_of_repeating[0]+1: len(s)]
    first_repeating_char = ""
    index_list_of_repeating = []
    print(len(s))

        
        
        
    # l_subs_l = 0
    # no_repeat = True
    # for i in range(len(s)):
    #     for j in range(i, len(s)):
    #         sub = s[i:j+1]
    #         print(sub)
    #         for k in range(0, len(sub)):
    #             if sub.count(sub[k]) > 1:
    #                 no_repeat = False
    #                 break
    #         if no_repeat:
    #             if len(sub) > l_subs_l:
    #                 l_subs_l = len(sub)
    #         no_repeat = True
    #         print (l_subs_l)
    # return l_subs_l
                
                    
                                             
