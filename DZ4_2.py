def get_cats_info(path):
    cats_list = []
    try:
        
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                # Розділяємо рядок на ідентифікатор, ім'я та вік кота
                cat_info = line.strip().split(',')
                
                # Формуємо словник для кота
                cat_dict = {
                    "id": cat_info[0],
                    "name": cat_info[1],
                    "age": int(cat_info[2])
                }
                
                # Додаємо словник до списку
                cats_list.append(cat_dict)

        return cats_list

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return None

# Приклад використання
path = 'cats_file.txt'
cats_info = get_cats_info(path)
print(cats_info)
