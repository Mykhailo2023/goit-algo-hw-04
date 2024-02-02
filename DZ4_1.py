from colorama import Fore, Back, Style


def read_salary_data(file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Розділяємо рядок за комою та створюємо кортеж
                values = tuple(line.strip().split(','))
                data.append(values)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return data

def calculate_statistics(data):
    if not data:
        return None, None
    
    salaries = [float(row[1]) for row in data]  
    average_salary = sum(salaries) / len(salaries)    
    total = sum(salaries)
    
    return average_salary, total

# Викликаємо функцію для читання даних та розрахунку статистики
file_path = 'salary_file.txt'
salary_data = read_salary_data(file_path)

# Перевірка чи є дані та виведення їх
if salary_data:
    for row in salary_data:
        continue
    
    # Розрахунок та виведення статистики
    average_salary, total = calculate_statistics(salary_data)
    if average_salary is not None and total is not None:
    #     Кольори зробив, бо просто цікаво
       print(f" {Fore.BLUE}Загальна сума заробітної плати: {Fore.RED} {total}, {Fore.CYAN} Середня заробітна плата:{Fore.GREEN} {average_salary} {Fore.RESET}")       

    else:
        print("Unable to calculate statistics.")
else:
    print("No data available.")