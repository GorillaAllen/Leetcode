def lengthOfLongestSubstring(s):
    
    longest_length = 0
    
    for j in range(0,len(s)):
        new = s[j]
        for i in range(j+1,len(s)):
            if new.find(s[i]) == -1:
                new = s[j:i+1]
            else:
                if len(new) > longest_length:
                    longest_length = len(new)
                break
            if len(new) >= longest_length:
                longest_length = len(new)
        print(new)
        
    return longest_length
    
                    
                                             
print(lengthOfLongestSubstring("tmmuredfct"))