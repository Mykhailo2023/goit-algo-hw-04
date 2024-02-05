def total_salary(path):
    # якщо файла не існує
    try:
        # відкриваємо файл на читання
        with open(path, 'r', encoding='utf-8') as file:
            # розбиваємо полінійно, роздільник кома
            data = [tuple(line.strip().split(',')) for line in file]
        # якщо файл пустий
        if not data:
            print("No data available.")
            return None, None
        
        salaries = [float(row[1]) for row in data]
        total = sum(salaries)
        average = total / len(salaries)
        
        return total, average

    except FileNotFoundError:
        print(f"File not found: {path}")
        return None, None

# Виклик функції
path = 'salary_file.txt'
total, average = total_salary(path)
print("Загальна сума заробітної плати:", total, ", Середня заробітна плата:", average)