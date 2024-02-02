
from pathlib import Path
import sys
from colorama import init, Fore

def main():
    # перевіряємо довжину аргументів, передаємо пусту строку і програма зчитає поточну папку
    if len(sys.argv) < 2:
        user_input = ''
    # Якщо передали якийсь агрумент програма бере аргумент [1], тому що аргумент [0] то назва файлу
    else:
        user_input = sys.argv[1]
    path = Path(user_input)
    # якщо існує
    if path.exists():
        # перевіряємо чи папка
        if path.is_dir():
            print_directory_contents(path)
        # якщо файл
        elif path.is_file():
            print(f'{Fore.BLUE}{path} Це файл{Fore.RESET}')
    else:
        # якщо не існує
        print(f'{Fore.RED}{path.absolute()} Файл чи папка не існує{Fore.RESET}')
# функція для друку
def print_directory_contents(dir_path, indent=''):
    # проходимо по папці
    for item in dir_path.iterdir():
        # якщо папка
        if item.is_dir():
            print(indent + f'🗂️ {Fore.GREEN}{item.name}{Fore.RESET}')
            print_directory_contents(item, indent + ' ┣ ')
        else:
            # якщо файл
            print(indent + f'📑 {Fore.BLUE}{item.name}{Fore.RESET}')

if __name__ == "__main__":
    main()