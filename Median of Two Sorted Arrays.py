def findMedianSortedArrays(nums1, nums2):
    B = []
    S = []
    start_point = 0
    if len(nums1) >= len(nums2):
       B = nums1
       S = nums2
    else:
        B = nums2
        S = nums1
    for i in range(0,len(S)):
        for j in range(start_point,len(B)):
            if S[i] <= B[j]:
                B.insert(j,S[i])
                start_point = j
                break
            elif j == len(B)-1:
                B.append(S[i])
                start_point = len(B) - 1
    print(B)
    if len(B) % 2 ==0:
        return ((B[len(B)//2 - 1] + B[len(B)//2]) / 2.0)
    else:    
        return float(B[len(B)//2])

s = [1,2,3,4,5,6]
b = [3,4]
print(findMedianSortedArrays(s,b))