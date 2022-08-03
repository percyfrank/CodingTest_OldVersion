
n = input()

ten = 0
for i in range(len(n)):
    ten += int(n[i]) * (8**(len(n)-i-1))

two = []
while True:
    two.append(ten % 2)
    ten = ten // 2
    if ten == 0:
        break
    
for i in range(len(two)):
    print(two[-(i+1)],end = '')
    
        


        

 
    