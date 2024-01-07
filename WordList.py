class WordList(list):
    def __init__(self, my_list):
        super().__init__(my_list)
        self.my_list = my_list
        alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
                    'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю',
                    'я']
        test_set = set()
        set_mylist = set()
        for item in self.my_list:
            for element in item.lower():
                set_mylist.add(element)

        for letters in alphabet:
            if letters in set_mylist:
                test_set.add(letters)

        if test_set != set_mylist:
            raise TypeError

    def upper(self):
        for item in self.my_list:
            print(item.upper(), end=' ')
        print()

    def lower(self):
        for item in self.my_list:
            print(item.lower(), end=' ')
        print()

    def count(self, word):
        test_list = []
        for item in self.my_list:
            item = item.lower()
            test_list.append(item)
        print(test_list.count(word))

    def pop(self, index=None):
        if index is not None:
            print(self.my_list.pop(index))
        else:
            not_repeat = []
            for item in self.my_list:
                if item not in not_repeat:
                    not_repeat.append(item)

            print(' '.join(not_repeat))
