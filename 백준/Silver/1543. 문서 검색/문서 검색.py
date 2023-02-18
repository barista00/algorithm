search_str = input()
string = input()

cnt = 0
start = 0
end = len(string)
while True:
    if end > len(search_str):
        break
    else:
        if search_str[start:end] == string:
            cnt += 1
            start = start + len(string)
            end = end + len(string)

        elif search_str[start:end] != string:
            start = start + 1
            end = end + 1
print(cnt)