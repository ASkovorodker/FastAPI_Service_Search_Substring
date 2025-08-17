import find_longest_common_substring
import create_json_file

def validation(strings_array):
    if len(strings_array) <= 2:
        mssg = "Длина массива 2 или меньше: поиск подстрок не выполняется"
    else:
        # Находим самую длинную подстроку в массиве и записываем ее в файл
        found_substring = find_longest_common_substring.find_longest_common_substring(strings_array)
        mssg = create_json_file.create_json_file(found_substring)
    return mssg