def task(array):
    """
    Первое задание через итерирование, а не функцию find
    """
    for ind in range(len(array)):
        if array[ind] == '0':
            return ind
    return "Not found"

print(task("111111111110000000000000000"))