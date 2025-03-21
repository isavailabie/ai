a = input().replace(' ', '')
a = a.replace('x', '')
cnt = 0
for i in range(8): 
    for j in range(i, 8):  
        if a[i] > a[j]: 
            cnt += 1  

if cnt & 1:  
    print("0")
else:
    print("1")  
