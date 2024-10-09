nums = [-1,0,1,2,-1,-4]
sub_zero = []
zeros = set()
over_zero = []
ans = []

for i in range(len(nums)):
    if nums[i] < 0:
        sub_zero.append(nums[i])
    elif nums[i] == 0:
        zeros.add(nums[i])
    else: over_zero.append(nums[i])
    
if len(sub_zero) == 0 and len(over_zero) == 0:
    if len(zeros)>=3:
        print( [0,0,0] )
    else: print( [] )
    

for i in range(len(sub_zero)-1):
    for j in range(i+1, len(sub_zero)):
        for k in range(len(over_zero)):
            if sub_zero[i] + sub_zero[j] + over_zero[k] == 0:
                ans.append([sub_zero[i], sub_zero[j], over_zero[k]])
                
for i in range(len(over_zero)-1):
    for j in range(i+1, len(over_zero)):
        for k in range(len(sub_zero)):
            if over_zero[i] + over_zero[j] + sub_zero[k] == 0:
                ans.append([over_zero[i], over_zero[j], sub_zero[k]])

if len(zeros) > 0:
    sub_zero = list(set(sub_zero))
    over_zero = list(set(over_zero))
    for i in range(len(sub_zero)):
        for k in range(len(over_zero)):
            if sub_zero[i]  + over_zero[k] == 0:
                    ans.append([sub_zero[i], 0, over_zero[k]])
            

print(sub_zero,zeros,over_zero)
print(ans)
        

