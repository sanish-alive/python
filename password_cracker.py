while True:
    try_no=1
    user_pass= str(input('Enter password: '))
    with open('password_list.txt', 'r', encoding='utf-8') as file:
        
        file = file.read().splitlines()

        
        for line in file:
            if line == user_pass:
                print('\n|--------------------|')
                print('|'+'no of try:',try_no)
                print('|password: '+line)
                print('|--------------------|\n')
                break
            else:
                try_no+=1
    if try_no == 1000000:
        print('Not found')



