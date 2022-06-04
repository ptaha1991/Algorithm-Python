# 2.	Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from collections import Counter


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(head, codes=None, code=''):
    if codes is None:
        codes = dict()
    if head is None:
        return None
    if isinstance(head.value, str):
        codes[head.value] = code
        return codes
    get_code(head.left, codes, code+'0')
    get_code(head.right, codes, code+'1')
    return codes


def get_tree(temp):
    count_str = Counter(temp)
    if len(count_str) <= 1:
        node = Node(None)
        if len(count_str) == 1:
            node.left = Node(count_str.most_common()[0][0])
            node.right = None
        count_str = {node: 1}

    while len(count_str) != 1:
        node = Node(None)
        spam = count_str.most_common()[:-3:-1]
        if type(spam[0][0]) is Node:
            node.left = spam[0][0]
        else:
            node.left = Node(spam[0][0])
        if type(spam[1][0]) is Node:
            node.right = spam[1][0]
        else:
            node.right = Node(spam[1][0])
        count_str -= Counter(dict(spam))
        count_str[node] = spam[0][1] + spam[1][1]

    return list(count_str)[0]


if __name__ == '__main__':
    string = 'beep boop beer!'
    node = get_tree(string)
    encoding = get_code(node)
    print(encoding)
    for i in encoding:
        print(f'{i} : {encoding[i]}')
    encoded = "".join(encoding[i] for i in string)
    print(encoded)


