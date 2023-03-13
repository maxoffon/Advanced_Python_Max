import sys


def decrypt(code):
    list_code = list(code)
    result = []
    dot_flag = False
    for i in range(len(list_code)):
        if list_code[i] != '.':
            result.append(list_code[i])
        else:
            if not dot_flag:
                dot_flag = True
            else:
                if len(result) > 0:
                    result.pop()
                dot_flag = False
    return ''.join(result)


print(decrypt(sys.stdin.readline()))

