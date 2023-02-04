while True:
    string = input()
    if string == '0':
        break
    else:
        if string == string[::-1]:
            print('yes')
        else:
            print('no')