# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


def letter_number(s):
    if 1 <= s <= 26:  # букв в английском алфавите
        s = ord('a') + s - 1
        return f"Это буква {chr(s)}"
    else:
        return 'Такой буквы в английском алфавите не существует'


if __name__ == '__main__':
    print(letter_number(int(input())))
