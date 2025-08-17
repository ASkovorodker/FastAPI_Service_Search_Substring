import json
import os

def create_json_file(found_substring):
        # with open("output.json", "w", encoding="utf-8") as f:
        #     json.dump(found_substring, f, ensure_ascii=False, indent=2)
        #
        # return "Подстрока найдена.\nJSON файл создан."

        # Проверяем, существует ли директория output
        output_dir = "output" if os.path.exists("output") else "."
        output_path = os.path.join(output_dir, "output.json")

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(found_substring, f, ensure_ascii=False, indent=2)

        return "Подстрока найдена.\nJSON файл создан."