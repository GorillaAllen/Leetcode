def longestCommonPrefix(strs) -> str:
    minL = len(strs[0])
    output = ''
    for i in range(1, len(strs)):
        if len(strs[i]) < minL:
            minL = len(strs[i])
    
    # print(minL)
    
    for i in range(minL):
        charA = strs[0][i]
        for j in range(len(strs)):
            if charA != strs[j][i]:
                return output
        output += strs[0][i]
    return output
            
    
print(longestCommonPrefix(["flower","flow","flight"]))