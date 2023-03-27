import re


file = open('words.txt', 'r')
words = [item.removesuffix('\n') for item in file.readlines()
         if len(item) > 4 and item.isalpha()
         or len(item) > 5 and not item.isalpha()]
file.close()


def is_strong_password(password: str):
    pass_words = re.findall(r'\w+', password)
    for item in pass_words:
        if is_in_dictionary(item):
            return False
    return True


def is_in_dictionary(word):
    word = word.lower()
    left = 0
    right = len(words) - 1
    middle = (right + left) // 2
    dict_word = words[middle]
    while left != right:
        if dict_word.lower() < word:
            left = middle + 1
        elif dict_word.lower() > word:
            right = middle - 1
        else:
            return True
        if left > right:
            return False
        middle = (left + right) // 2
        dict_word = words[middle]
    return dict_word.lower() == word


print(is_strong_password('animal astma'))