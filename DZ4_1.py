
def total_salary():

     # Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
    path = 'salary_file.txt'
# Робимо виключення якщо файл не існує
    try:
        # відкриваємо файл на читання (не забуваємо про кодування)

        with open(path, 'r', encoding='utf-8') as file:

            # зчитуємо дані з файлу і розбиваємо  по комі
            data = [tuple(line.strip().split(',')) for line in file]

        # якщо нічого не знайшло 
        if not data:
            print("No data available.")
            return None, None
        
        # математичні дії
        salaries = [float(row[1]) for row in data]
        total = sum(salaries)
        average = total / len(salaries)

        # виводимо результат
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
        return total, average        

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None, None

# Виклик функції
total_salary()

# я розумії що забагато коментарів, але поки мушу так робити щоб запамятати