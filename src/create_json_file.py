import json

def create_json_file(found_substring):
        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(found_substring, f, ensure_ascii=False, indent=2)

        return "Подстрока найдена.\nJSON файл создан."