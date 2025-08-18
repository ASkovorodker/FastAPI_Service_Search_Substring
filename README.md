# FastAPI Longest Common Substring Service

Веб-сервис на базе FastAPI для поиска наибольшей общей подстроки в массиве строк.

## Описание

Сервис принимает JSON файл с массивом строк, находит наибольшую общую подстроку среди всех строк и возвращает результат в виде строки. Дополнительно создается выходной файл `output.json` с найденной подстрокой.

## Возможности

- ✅ Прием массива строк через REST API
- ✅ Поиск наибольшей общей подстроки оптимизированным алгоритмом
- ✅ Валидация входных данных
- ✅ Автоматическая генерация документации API
- ✅ Создание JSON файла с результатом
- ✅ Управление массивом строк (просмотр, очистка)

## API Endpoints

| Метод | URL | Описание |
|-------|-----|----------|
| `POST` | `/add-strings` | Добавить строки и найти общую подстроку |
| `GET` | `/strings` | Получить текущий массив строк |
| `DELETE` | `/strings` | Очистить массив строк |
| `GET` | `/` | Корневой эндпоинт с информацией о сервисе |
| `GET` | `/docs` | Интерактивная документация Swagger |
| `GET` | `/redoc` | Альтернативная документация ReDoc |

## Требования

- Python 3.8+
- pip (менеджер пакетов Python)

## Установка и запуск

### 1. Клонирование/создание проекта

```bash
# Создайте директорию проекта
mkdir fastapi-substring-project
cd fastapi-substring-project
```

### 2. Создание виртуального окружения

```bash
# Создание виртуального окружения
python -m venv venv

# Активация виртуального окружения
# Для Windows:
venv\Scripts\activate

# Для macOS/Linux:
source venv/bin/activate
```

### 3. Создание файла зависимостей 
- Файл зависимостей requirements.txt создаем в корне проекта
- Содержание файла
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
python-multipart==0.0.6
```

### 4. Установка зависимостей

```bash
# Установка всех необходимых пакетов
pip install -r requirements.txt
```

### 5. Запуск сервиса

```bash
# Способ 1: Запуск через Python
python main.py

# Способ 2: Запуск через uvicorn с автоперезагрузкой
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### 6. Проверка работы сервиса
После запуска сервер будет доступен по адресу:
- **API**: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Использование

### Запросы через curl в консоли

#### Подача массива в json формате
```bash
curl -X POST "http://127.0.0.1:8000/add-strings" \
     -H "Content-Type: application/json" \
     -d '{"strings": ["привет", "мир", "python"]}'
```
#### Подача json файла с массивом
В параметрах флага -d пишем нужный нам json файл, например  @substr_on.json
```bash
curl -X POST "http://127.0.0.1:8000/add-strings" \
     -H "Content-Type: application/json" \
     -d @substr_on.json
```
### Для очистки массива строк
```bash
curl -X DELETE "http://127.0.0.1:8000/strings"
```
### Для получения текущего массива строк
```bash
curl -X GET "http://127.0.0.1:8000/strings"
```
### Файлы для тестирования
Файлы для тестирования лежат в директории src
- substr_on.json - набор строк включающий общую подстроку
- substr_off.json - набор строк без общей подстроки
- two_substr.json - набор из двух строк для проверки валидации

## Контейнеризация
Используем именованный том для доступа к выходному файлу json с результатами работы программы

### Создание и запуск контейнера

#### 1. Создание именованного тома
```bash
docker volume create fastapi-output-data
```

#### 2. Сборка Docker образа
```bash
docker build -t fastapi-substring-app .
```

#### 3. Запуск контейнера с именованным томом
```bash
docker run -d -p 8000:8000 \
  --name fastapi-container \
  -v fastapi-output-data:/app/output \
  fastapi-substring-app
```

#### 4. Тестирование API -  корневой эндпоинт
```bash
curl -X GET "http://localhost:8000/"
```

#### 5. Отправка json файла с массивом строк
Берем команду curl из Инструкций по развертыванию приложения

#### 6. Просмотр созданного выходного файла
```bash
docker run --rm -v fastapi-output-data:/data busybox cat /data/output.json
```

#### 7. Копирования файла из тома на хост
```bash
docker run --rm -v fastapi-output-data:/data -v "$(pwd)":/backup busybox cp /data/output.json /backup/result.json
```

### Команды удаления и очистки

#### 1. Остановка контейнера
```bash
docker stop fastapi-container
```

#### 2. Удаление контейнера
```bash
docker rm fastapi-container
```

#### 3. Удаление тома
```bash
docker volume rm fastapi-output-data
```

#### 4. Удаление образа
```bash
docker rmi fastapi-substring-app
```

## Структура проекта

```
fastapi-substring-project/
├── venv/                          # Виртуальное окружение
├── main.py                        # Основной файл приложения FastAPI
├── validation.py                  # Модуль валидации входных данных
├── create_json_file.py           # Модуль создания JSON файла
├── find_longest_common_substring.py  # Алгоритм поиска подстроки
├── requirements.txt              # Зависимости проекта
├── README.md                     # Документация
├── curl_commands.txt             # Примеры запросов curl
├── output.json                   # Выходной файл (создается автоматически)
├── Dockerfile                    # Docker конфигурация
├── docker-compose.yml           # Docker Compose конфигурация
└── .dockerignore                # Файлы для исключения из Docker контекста
```

## Алгоритм работы

1. **Валидация**: Проверка, что в массиве больше 2 строк
2. **Оптимизация**: Выбор самой короткой строки как базовой
3. **Поиск**: Проверка подстрок от длинных к коротким
4. **Результат**: Возврат первой найденной максимальной общей подстроки
5. **Сохранение**: Создание файла `output.json` с результатом

## Примеры работы

### Успешный поиск

**Вход:**
```json
{
  "strings": ["programming", "programmer", "program"]
}
```

**Выход:**
```json
{
  "message": "Подстрока найдена.\nJSON файл создан."
}
```

**Файл output.json:**
```json
  "program"
```

### Недостаточно строк

**Вход:**
```json
{
  "strings": ["hello", "world"]
}
```

**Выход:**
```json
{
  "message": "Длина массива 2 или меньше: поиск подстрок не выполняется"
}
```

## Интерактивная документация

После запуска сервиса доступна автоматически сгенерированная документация:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Зависимости

- **FastAPI** - современный веб-фреймворк для создания API
- **Uvicorn** - ASGI сервер для запуска приложения
- **Pydantic** - валидация данных и настройки
- **python-multipart** - поддержка multipart/form-data


### Тестирование

Для тестирования алгоритма поиска подстроки можно запустить:

```bash
python find_longest_common_substring.py
```

## Лицензия

Этот проект создан в образовательных целях.

## Автор

Проект создан с использованием FastAPI и Python.
