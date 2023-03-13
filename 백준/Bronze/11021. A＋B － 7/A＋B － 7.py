import sys

n=int(input())
arr1=[]
arr2=[]

for i in range(n):
  a,b=map(int,sys.stdin.readline().split())
  arr1.append(a)
  arr2.append(b)
for i in range(n):
  print("Case #%d: %d"%((i+1),arr1[i]+arr2[i]))