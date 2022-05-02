# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и
# заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар
# "код-символ" в каждой строке

def table_ascii_characters(start, stop):
    i = 1
    while start <= stop:
        print(f'{start} {chr(start)}'.ljust(7), end=' ')
        if i % 10 == 0:
            print()
        start += 1
        i += 1


if __name__ == '__main__':
    table_ascii_characters(32, 127)
    #table_ascii_characters(int(input()),int(input()))
