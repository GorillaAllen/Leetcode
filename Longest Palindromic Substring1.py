def longestPalindrome(s):
    longest = s[0]
    if len(s)==0 or len(s) ==1:
        return s
    if len(s)==2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]
        
    for i in range(1,len(s)):
        rev_s = s[0:i][::-1]
        sub_s = s[i:len(s)]
        if len(rev_s)>len(sub_s):
            compare_length = len(sub_s)
        else:
            compare_length = len(rev_s)


        if rev_s[0] == sub_s[0]:
            flag = True
            temp_s1 = ""
            for j in range(1, compare_length):
                if rev_s[j] != sub_s[j]:
                    flag = False
                    temp_s1 = rev_s[0:j][::-1] + sub_s[0:j]
                    if len(temp_s1) > len(longest):
                        longest = temp_s1
                    break
            temp_s1 = rev_s[0:compare_length][::-1] + sub_s[0:compare_length]
            if flag and len(temp_s1) > len(longest):
               longest = temp_s1

        if len(sub_s) > 1:
            if rev_s[0] == sub_s[1]:
                flag = True
                temp_s2 = ""
                mid_char = sub_s[0]
                sub_s = sub_s[1:len(sub_s)]
                if len(rev_s)>len(sub_s):
                    compare_length = len(sub_s)
                else:
                    compare_length = len(rev_s)
                for j in range(1, compare_length):
                    if rev_s[j] != sub_s[j]:
                        flag = False
                        temp_s2 = rev_s[0:j][::-1] + mid_char + sub_s[0:j]
                        if len(temp_s2) > len(longest):
                            longest = temp_s2
                        break
                temp_s2 = rev_s[0:compare_length][::-1] + mid_char + sub_s[0:compare_length]
                if flag and len(temp_s2) > len(longest):
                    longest = temp_s2
    return longest
            
print(longestPalindrome("cbbd"))
        
        