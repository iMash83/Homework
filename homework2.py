def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    line = line.strip()
                    if not line:
                        continue
                    cat_id, name, age = line.split(',')
                    cats_list.append({
                        "id": cat_id,
                        "name": name,
                        "age": age
                    })
                except ValueError:
                    continue
        return cats_list
    except FileNotFoundError:
        return []

info = get_cats_info("/Users/Mash2/Documents/CODE/Homework_Mash/cats_file.txt")

for cat in info:
    print(cat)