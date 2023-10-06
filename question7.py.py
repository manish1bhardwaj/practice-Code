n  = int(input())
mp = list(map(int,input().split()))
out_list=[]
for i in mp:
    out_list.append(i % 2)
print(*out_list)       