def task(array):
    """
    Возвращает индекс первого 0, иначе возвращает "Not found"
    """
    pos = array.find("0")
    return pos if pos >= 0 else "Not found"

print(task("111111111110000000000000000"))