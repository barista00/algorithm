st = input().upper()
first = 0
for i in set(st):
    if st.count(i) > first:
        output = i
        first = st.count(i)
    elif st.count(i) == first:
        output = '?'
print(output)