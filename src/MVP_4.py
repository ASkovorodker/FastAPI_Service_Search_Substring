from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

import validation

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

    # Проверка длины массива и поиск подстроки. Функция валидации вызывает функцию поиска подстроки
    mssg = validation.validation(strings_array)
    print(f"{mssg}")

    return StringsResponse(
        message=f"{mssg}"
    )


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



