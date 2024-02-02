
import os
from colorama import Fore, Back

contacts = {}
first_run = True

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return Fore.RED + "Неправильна кількість аргументів. Потрібно ввести ім'я та номер телефону." + Fore.RESET
    else:
        name, phone = args
        if phone.isdigit():
            if phone in contacts.values():
                return Fore.RED + "Цей номер вже присутній у контактах." + Fore.RESET
            else:
                contacts[name] = phone
                return Fore.GREEN + "Контакт додано." + Fore.RESET
        else:
            return Fore.LIGHTRED_EX + "Номер не є цифрами." + Fore.RESET
        
def write_to_file(file_name, data):
    # файл при збереженні перезаписується бо поки не можу зробити перевірку чи є вже дані у файлі
    with open(file_name, 'w+') as file: 
        for name, phone in data.items():
            file.write(f'{name}: {phone}\n')
    return Fore.LIGHTYELLOW_EX + 'Дані успішно записано у файл.' + Fore.RESET


# функція створення файлу якщо його не існує contacts.txt

def check_and_create_file():
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, 'contacts.txt')

    try:
        # Перевірка, чи існує файл
        if not os.path.isfile(file_path):
            # Створення файлу, якщо він не існує
            with open(file_path, 'w') as file:
                pass
                # print(f"Файл {file_path} створено.")
    except Exception as e:
        print(f"{Fore.RED}Помилка при перевірці та створенні файлу:{Fore.RESET} {e}")



def read_file_to_contacts(filename):
    global contacts 
    # Запуснаємо функцію провірки існування файлу
    check_and_create_file()
    
    # якщо у файлі немає даних
    if os.path.getsize(filename) == 0:

        print(f"{Fore.LIGHTBLUE_EX} Файл поки що порожній порожній.{Fore.RESET}")
        return contacts
    
        # відкриваємо файл і якщо є дані підгружаємо дані у словник 
    with open(filename, 'r') as file:
        for line in file:
            if ':' in line:
                name, phone = line.strip().split(':')
                contacts[name] = phone.strip()  # Забираємо можливі пробіли з номера телефону
            else:
                # виводить попередження якщо не коректні вхідні дані
                print(f"Некоректний формат рядка у файлі (без `:`): {line.strip()}")
    return contacts

# функція зміни імені у словнику
def change_username(name, new_name):
    global contacts 

    if name in contacts:
        print(f"Знайдено контакт: {Fore.GREEN} {name}{Fore.RESET}, поточний номер телефону: {Fore.YELLOW} {contacts[name]}{Fore.RESET}")
        confirmation = input("Ви впевнені, що хочете змінити ім'я? (y/n): ").lower()

        if confirmation == 'y':
            contacts[new_name] = contacts.pop(name)
            print(f"{Fore.GREEN}Ім'я змінено на {new_name}.{Fore.RESET}")
        else:
            print(f"{Fore.RED}Зміни скасовано.{Fore.RESET}")
    else:
        print(f"{Fore.MAGENTA}Контакт з ім'ям {name} не знайдено.{Fore.RESET}")

# функція видалення файлу з даними
        
def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"Файл {file_name} успішно видалено.")
    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено.")
    except Exception as e:
        print(f"Помилка при видаленні файлу {file_name}: {e}")


# Функція видалення контакту
def delete_contact(name):

    global contacts  

    if name in contacts:
        confirmation = input(f"{Back.LIGHTRED_EX}Ви впевнені, що хочете видалити контакт?{Back.RESET} {Fore.GREEN}{name}{Fore.RESET}{Back.LIGHTRED_EX}{Back.RESET}\n(y/n): ").lower()

        if confirmation == 'y':
            del contacts[name]
            print(f"{Fore.LIGHTRED_EX}Контакт{Fore.RESET} {Fore.GREEN}{name}{Fore.RESET} {Fore.LIGHTRED_EX}видалено.{Fore.RESET}")
        else:
            print(f"{Fore.LIGHTYELLOW_EX}Видалення {Fore.GREEN}{name} {Fore.LIGHTYELLOW_EX}скасовано.{Fore.RESET}")
    else:
        print(f"{Fore.LIGHTBLUE_EX}Контакт з ім'ям {Fore.GREEN}{name} {Fore.LIGHTBLUE_EX}не знайдено.{Fore.RESET}")


def help_command():
    
    # print(f"{Fore.LIGHTGREEN_EX}Welcome to the assistant bot!{Back.RESET}")
    print(f"{Fore.GREEN}Hello{Fore.RESET} - Привітання з ботом")
    print(f"{Fore.MAGENTA}read{Fore.RESET} - читання з файлу")    
    print(f'{Fore.CYAN}add{Fore.RESET} - додати контакт ({Fore.GREEN}add {Fore.BLUE}name{Fore.RESET})')
    print(f'{Fore.LIGHTBLUE_EX}name {Fore.RESET} - змінити імя контакту ({Fore.GREEN}enter{Fore.RESET})')
    print(f'{Fore.YELLOW}save {Fore.RESET} - зберегти контакти в файл')
    print(f"{Fore.YELLOW}Якщо не зберегти то ми будемо працювати тільки з тими даними що в пам'яті")    
    print(f"{Fore.RED}del{Fore.RESET} - видалити контакт ({Fore.GREEN}del {Fore.BLUE}name{Fore.RESET})")
    print(f"{Fore.LIGHTRED_EX}del_file{Fore.RESET} - видалити файл з всіма записами ({Fore.GREEN}del_file{Fore.RESET})")
    print(f"{Fore.LIGHTMAGENTA_EX}exit{Fore.RESET} - вихід з бота")
    print(f'{Fore.GREEN}Help {Fore.RESET} for help')



def main():
    global contacts
    count = 1
    # друкуємо один раз для допомоги
    while count > 0:
        print(f"Type {Fore.GREEN}Help{Fore.RESET} for more information.")
        count -= 1

    while True:      

        user_input = input(f"{Back.LIGHTBLACK_EX}Введіть команду: {Back.RESET}")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(f"{Back.LIGHTMAGENTA_EX}Good bye!{Back.RESET}")
            break

        elif command in ["hello", "привіт"]:
            print(f"{Fore.GREEN}Як я можу вам допомогти?{Fore.RESET}")

        elif command in ["add", "додати"]:
            print(add_contact(args, contacts))
            # print(contacts)

        elif command == "save":
            result = write_to_file('contacts.txt', contacts)
            print(result)  # Виведе 'Дані успішно записано у файл.'
        
        elif command == "read":
            result = read_file_to_contacts('contacts.txt')
            print(result)

        elif command == "name":
            result = change_username(input(f"{Fore.LIGHTRED_EX}Введіть поточне ім'я: {Fore.RESET}"), input(f"{Fore.LIGHTGREEN_EX}Введіть нове ім'я: {Fore.RESET}"))

        elif command == "del":
            parts = user_input.split(maxsplit=1)
            if len(parts) == 2:
                result = delete_contact(parts[1])
            else:
                print(f"Неправильний формат команди {Fore.RED}del.{Fore.RESET} Введіть {Fore.GREEN}'del ім'я'{Fore.RESET}")
        
        elif command == "del_file":
            delete_file('contacts.txt')

        elif command == "help":
            help_command()

        else:
            print(f"{Fore.LIGHTRED_EX}Невірна команда.{Fore.RESET}")

if __name__ == "__main__":
    main()


