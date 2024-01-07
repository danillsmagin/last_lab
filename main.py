from WordList import WordList

if __name__ == '__main__':
    while True:
        get_data = input('U wanna get data from txt file?(y-yes/n-not/e-exit)\n')
        if get_data == 'y':
            with open('words_list', 'r') as file:
                str_file = file.read()
                list_file = str_file.split(' ')
                print(list_file)
                word_list_file = WordList(list_file)

                while True:
                    print('1.Upper register all word')
                    print('2.Lower register all word')
                    print('3.The number of words entered in the list')
                    print('4.Method pop(without argument or with argument)')
                    print('5.Method sort')
                    print('6.Exit')
                    choose_number = int(input('Choose number 1-5: '))

                    if choose_number == 1:
                        word_list_file.upper()
                    elif choose_number == 2:
                        word_list_file.lower()
                    elif choose_number == 3:
                        amount_word = input('Enter word u wanna count: ')
                        word_list_file.count(amount_word)
                    elif choose_number == 4:
                        word_list_file.pop()
                    elif choose_number == 5:
                        word_list_file.sort()
                        print(word_list_file)
                    elif choose_number == 6:
                        break

        elif get_data == 'n':
            word_list = WordList(['привет', 'але', 'але', 'как', 'дела', 'але', 'как'])
            while True:
                print('1.Upper register all word')
                print('2.Lower register all word')
                print('3.The number of words entered in the list')
                print('4.Method pop(without argument or with argument)')
                print('5.Method sort')
                print('6.Exit')
                choose_number = int(input('Choose number 1-5: '))

                if choose_number == 1:
                    word_list.upper()
                elif choose_number == 2:
                    word_list.lower()
                elif choose_number == 3:
                    amount_word = input('Enter word u wanna count: ')
                    word_list.count(amount_word)
                elif choose_number == 4:
                    word_list.pop()
                elif choose_number == 5:
                    word_list.sort()
                    print(word_list)
                elif choose_number == 6:
                    break

        elif get_data == 'e':
            break
