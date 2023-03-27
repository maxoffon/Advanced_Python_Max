import re


num_dict = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}


def my_t9(string: str) -> list[str]:
    with open('words.txt', 'r') as file:
        words = ' '.join([item.replace('\n', '').lower() for item in file.readlines()])
        pattern = r'\b'
        for item in list(string):
            pattern += f'[{num_dict[int(item)]}]'
        return list(set(re.findall(pattern, words)))


if __name__ == '__main__':
    print(my_t9('22736368'))
