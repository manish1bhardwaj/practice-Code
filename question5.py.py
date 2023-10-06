st=input()
reg=''
for ch in st:
    if ch not in reg:
        count=st.count(ch)
        print(f'{ch}:{count}')
        reg+=ch
