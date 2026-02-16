from pathlib import Path
import pprint  

def get_cats_info(path):
    cats_list = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue
                
                try:
                    cat_id, name, age = cleaned_line.split(',')
                    
                    cat_data = {
                        "id": cat_id.strip(),
                        "name": name.strip(),
                        "age": age.strip()
                    }
                    
                    cats_list.append(cat_data)
                    
                except ValueError:
                    continue

    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return []
    except Exception as e:
        print(f"Ошибка: {e}")
        return []

    return cats_list

if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    
    print("Результат работы функции:")
    pprint.pprint(cats_info)