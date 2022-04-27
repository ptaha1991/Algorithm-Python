# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.


def place_distance_in_alphabet(s1, s2):
    p_s1 = ord(s1.lower()) - ord('a') + 1
    p_s2 = ord(s2.lower()) - ord('a') + 1
    if 1 <= p_s1 <= 26 and 1 <= p_s2 <= 26: # букв в английском алфавите
        between_s = abs(p_s2 - p_s1) - 1
        return f"Позиция {s1}: {p_s1}\nПозиция {s2}: {p_s2}\nМежду буквами {s1} и {s2} {between_s} букв(ы)"
    else:
        return f"Ошибка при вводе букв. Введите 2 буквы английского алфавита"


if __name__ == '__main__':
    print(place_distance_in_alphabet(
        input(),
        input()
    ))
