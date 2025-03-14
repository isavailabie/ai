def countin(a1):
    a1.remove('x') 
    count = 0
    for i in range(len(a1)):
        for j in range(i + 1, len(a1)):
            if a1[i] > a1[j]:
                count += 1
    return count


a1 = input().split()
rx = 3-(a1.index('x')//3)
inv_count = countin(a1)
if (inv_count + rx) % 2 == 0:
    print(1)
else:
    print(0)
