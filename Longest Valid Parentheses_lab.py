import numpy as np
def p_test(test):
    flag = 0
    if sum(test) != 0:
        # print("not balanced")
        return False
        
    else:
        for num in test:
            flag = flag + num
            if flag < 0:
                # print("below zero")
                return False
    return True


np_test_list = np.array([], dtype = "int8")
s = "())))((()))()()("

for i in range(len(s)):
    if s[i] == '(':
        np_test_list = np.append(np_test_list, 1)
    else: np_test_list = np.append(np_test_list, -1)


print(np_test_list)

for j in range(len(np_test_list)):
    for k in range(0,j+1):
        if p_test(np_test_list[k:len(np_test_list)-j+k]) == True:
            return (np_test_list[k:len(np_test_list)-j+k])
        
# print(p_test(np_test_list[0:len(np_test_list)]-0+0))

# print(p_test(np_test_list[0:len(np_test_list)-1+0]))
# print(p_test(np_test_list[1:len(np_test_list)-1+1]))

# print(p_test(np_test_list[0:len(np_test_list)-2+0]))
# print(p_test(np_test_list[1:len(np_test_list)-2+1]))
# print(p_test(np_test_list[2:len(np_test_list)-2+2]))

# print(p_test(np_test_list[0:len(np_test_list)-3+0]))
# print(p_test(np_test_list[1:len(np_test_list)-3+1]))
# print(p_test(np_test_list[2:len(np_test_list)-3+2]))
# print(p_test(np_test_list[3:len(np_test_list)-3+3]))