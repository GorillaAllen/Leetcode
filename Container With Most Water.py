height = [1,8,6,2,5,4,8,3,7]
hei = height.copy()
maximun = 0

for i in range(len(hei)-1):
    for j in range(i,len(hei)):
        if min(hei[i], hei[j]) * (j-i) > maximun:
            maximun = min(hei[i], hei[j]) * (j-i)
    

print(maximun)

