def longestPalindrome(s):
    longest = ""
    if len(s)==0 or len(s) ==1:
        return s
    if len(s)==2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]
    if len(s) > 2 and len(s) % 2 == 1:
        for i in range(1,len(s)-1):
            mid_char = s[i]
            rev_s = s[0:i][::-1]
            sub_s = s[i+1:len(s)]
            # print(rev_s[::-1] + mid_char + sub_s)
            # return(s, mid_char, rev_s, sub_s)
            for j in range()
            if rev_s == sub_s and len(rev_s[::-1] + mid_char + sub_s) > len(longest):
                longest = rev_s[::-1] + mid_char + sub_s
    # else:
    #     for i in range(1,len(s))
    # return longest
            
            
            
print(longestPalindrome("abcbg"))
        
        