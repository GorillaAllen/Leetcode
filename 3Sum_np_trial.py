import numpy as np
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]    
sub_zero = []
zeros = []
over_zero = []
ans = []

for i in range(len(nums)):
    if nums[i] < 0 and sub_zero.count(nums[i]) < 2 :  sub_zero.append(nums[i])
    elif nums[i] == 0                              :  zeros.append(nums[i])
    elif over_zero.count(nums[i]) < 2              :  over_zero.append(nums[i])
    


if len(zeros)>=3:
    ans.append ([0,0,0])

#make them np array
sub_zero = np.sort(np.array(sub_zero))
sub_zero = sub_zero[::-1]
over_zero = np.sort(np.array(over_zero))

    
    
    

for i in range(len(sub_zero)-1):
    for j in range(i+1, len(sub_zero)):
        start = sub_zero[i] + sub_zero[j]
        flag = 0
        for m in range(len(over_zero)):
            if abs(start) >= over_zero[m]:
                continue
            else:
                flag = m-1
                break
        for k in range(flag, len(over_zero)):
            if sub_zero[i] + sub_zero[j] + over_zero[k] == 0:
                ans.append([ sub_zero[i], sub_zero[j], over_zero[k] ])
                break
                
for i in range(len(over_zero)-1):
    for j in range(i+1, len(over_zero)):
        start = over_zero[i] + over_zero[j]
        flag = 0
        for m in range(len(sub_zero)):
            if  start >= abs(sub_zero[m]):
                continue
            else:
                flag = m-1
                break
        for k in range(flag, len(sub_zero)):
            if over_zero[i] + over_zero[j] + sub_zero[k] == 0:
                ans.append([ over_zero[i], over_zero[j], sub_zero[k]  ] )
                break

if len(zeros) > 0:
    sub_zero = np.unique(sub_zero)
    over_zero = np.unique(over_zero)
    for i in range(len(sub_zero)):
        for k in range(len(over_zero)):
            if sub_zero[i]  + over_zero[k] == 0:
                    ans.append([sub_zero[i], 0, over_zero[k]])
                    break
            

# print(sub_zero,zeros,over_zero)
print( ans)



