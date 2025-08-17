import find_longest_common_substring

def validation(strings_array):
    if len(strings_array) <= 2:
        mssg = "Длина массива 2 или меньше: поиск подстрок не выполняется"
    else:
        mssg = "Найдена общая подстрока: "
        # Находим самую длинную подстроку в массиве и возвращаем ее
        found_substring = find_longest_common_substring.find_longest_common_substring(strings_array)
        # Выводим найденную подстроку в консоль
        mssg += found_substring
    return mssg