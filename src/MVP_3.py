from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

import find_longest_common_substring

# Создаем экземпляр приложения FastAPI
app = FastAPI(
    title="String Array API",
    description="API для работы с массивом строк",
    version="1.0.0"
)

# Глобальный массив для хранения строк
strings_array: List[str] = []


# Модель для входящих данных
class StringsInput(BaseModel):
    strings: List[str]


# Модель для ответа
class StringsResponse(BaseModel):
    message: str


@app.post("/add-strings", response_model=StringsResponse)
async def add_strings(data: StringsInput):
    """
    Принимает JSON объект с массивом строк и добавляет их в программный массив
    """
    # Добавляем новые строки в массив
    strings_array.extend(data.strings)

    mssg = ""
    found_substring = ""

    # Получаем длину массива и проверяем его
    if len(strings_array) <= 2:
        mssg = "Длина массива 2 или меньше"
        found_substring = "поиск подстрок не выполняется"
        print(f"{mssg}: {found_substring}")
    else:
        mssg = "Найдена общая подстрока"
        # Находим самую длинную подстроку в массиве и возвращаем ее
        found_substring = find_longest_common_substring.find_longest_common_substring(strings_array)
        # Выводим найденную подстроку в консоль
        print(f"{mssg}: {found_substring}")

    return StringsResponse(
        message=f"{mssg}: {found_substring}"
    )

# пример обновления роута из main.py


@app.get("/strings", response_model=List[str])
async def get_strings():
    """
    Возвращает текущий массив строк
    """
    # Выводим массив в консоль
    print(f"Запрос массива строк: {strings_array}")
    return strings_array


@app.delete("/strings")
async def clear_strings():
    """
    Очищает массив строк
    """
    global strings_array
    strings_array.clear()
    print("Массив строк очищен")
    return {"message": "Массив строк очищен", "current_array": []}


@app.get("/")
async def root():
    """
    Корневой эндпоинт
    """
    return {
        "message": "String Array API",
        "docs": "/docs",
        "current_array_size": len(strings_array)
    }


# Для запуска сервера (если запускается напрямую)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)



