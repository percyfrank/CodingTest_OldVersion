n = int(input())
n1 = n

a = list(map(int,input().split()))
    
tmp1 = 0
for i in range(len(a)):
    if n1 == 0:
        continue
    tmp1 += n1 // a[i]
    n1 -= tmp1 * a[i]
    
cnt1 = 0
cnt2 = 0
idx = a[0]
tmp2 = 0
for i in range(len(a)-1):
    if a[i] < a[i+1]:
        cnt2 = 0
        idx = a[i+1]
        cnt1 += 1
    elif a[i] > a[i+1]:
        cnt1 = 0
        idx = a[i+1]
        cnt2 += 1
    else:
        cnt1 = 0
        cnt2 = 0
        
    if cnt1 == 3:
        n += idx * tmp2
        cnt1 -= 1
        tmp2 = 0
    if cnt2 == 3:
        if n <= 0:
            continue
        tmp2 += n // idx
        cnt2 -= 1
        if n // idx == 0:
            continue
        n -= (n // idx) * idx
        
bnp = tmp1 * a[13]+n1
timing = tmp2 * a[13]+n

if bnp > timing:
    print("BNP")
elif bnp < timing:
    print("TIMING")
else:
    print("SAMESAME")