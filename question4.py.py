##find the frequency(no. of repetation of any char in any sentence)
st1=input()
st2=input()
count=0
for i in st1:
    if i == st2:
        count += 1
print(count)
