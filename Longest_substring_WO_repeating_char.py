def lengthOfLongestSubstring(s):
        l_subs_l = 0
        no_repeat = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                for k in range(0, len(sub)):
                    if sub.count(sub[k]) > 1:
                        no_repeat = False
                        break
                if no_repeat:
                    if len(sub) > l_subs_l:
                        l_subs_l = len(sub)
                no_repeat = True
        return l_subs_l
                
                    
                                             
print(lengthOfLongestSubstring("bbbbccas"))