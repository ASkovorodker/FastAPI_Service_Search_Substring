def find_longest_common_substring(strings):
    """
    Оптимизированная версия наивного алгоритма.
    Останавливается при первом найденном результате.
    """
    if not strings or len(strings) == 0:
        return ""

    if len(strings) == 1:
        return strings[0]

    # Берем самую короткую строку как базу
    base_string = min(strings, key=len)
    if len(base_string) == 0:
        return ""

    longest_common = ""

    # Проверяем от самых длинных подстрок к коротким
    for length in range(len(base_string), 0, -1):
        for start in range(len(base_string) - length + 1):
            substring = base_string[start:start + length]

            # Проверяем наличие подстроки во всех строках
            if all(substring in s for s in strings):
                return substring  # Возвращаем первую (самую длинную) найденную

    return ""

# Демонстрация работы алгоритма
if __name__ == "__main__":
    # Тестовые примеры
    test_cases = [
        {
            "name": "Обычный случай",
            "strings": ["abcdefg", "xyzabcuvw", "123abc789"],
            "expected": "abc"
        },
        {
            "name": "Длинная общая подстрока",
            "strings": ["programming", "programmer", "program"],
            "expected": "program"
        },
        {
            "name": "Нет общей подстроки",
            "strings": ["abc", "def", "ghi"],
            "expected": ""
        },
        {
            "name": "Одинаковые строки",
            "strings": ["hello", "hello", "hello"],
            "expected": "hello"
        },
        {
            "name": "Одна пустая строка",
            "strings": ["abc", "", "def"],
            "expected": ""
        }
    ]

    for test in test_cases:
        print("=" * 60)
        print(f"ТЕСТ: {test['name']}")
        print(f"Входные строки: {test['strings']}")
        print("=" * 60)

        result = find_longest_common_substring(test['strings'])

        print(f"\nРЕЗУЛЬТАТ: '{result}'")
        print(f"ОЖИДАЛОСЬ: '{test['expected']}'")
        print(f"ТЕСТ {'ПРОЙДЕН' if result == test['expected'] else 'ПРОВАЛЕН'}")
        print("\n" + "=" * 60 + "\n")