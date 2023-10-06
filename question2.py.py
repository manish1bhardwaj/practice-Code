##to count all chr repetation in string
st=input()
reg=''
for x in st:
    count=0
    if x not in reg:
       for a in st:
           if a == x:
              count+=1
        
       print(x,':',count)
       reg+=x
