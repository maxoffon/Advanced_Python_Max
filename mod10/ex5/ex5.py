def find_insert_position(arr: list, a: int) -> int:
    l = 0
    r = len(arr)
    m = (l + r) // 2
    while l < r:
        if arr[m] < a:
            l = m + 1
        elif arr[m] > a:
            r = m - 1
        else:
            r = m
        m = (l + r) // 2
    return l


print(find_insert_position([], 4))