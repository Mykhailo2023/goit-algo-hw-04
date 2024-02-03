
def get_cats_info(file_path):
    cats_dict = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Розділяємо рядок за комою та отримуємо id, ім'я кота та рік
                cat_info = line.strip().split(',')
                if len(cat_info) == 3:
                    id, name, year = cat_info
                    cats_dict[id] = {'name': name, 'year': year} # тут можна виставляти поля 
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return cats_dict

# Приклад виклику функції для створення словника
file_path = 'cats_file.txt'
cats_dict = get_cats_info(file_path)
print(cats_dict)