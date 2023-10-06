k=int(input())

x=0
for i in range(1,1001):
    if i%3!=0 and i%10!=3:
       x+=1
       if x==k:
           print(i)
           break
