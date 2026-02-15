import sys
from pathlib import Path
from colorama import init, Fore

# Инициализация colorama
init(autoreset=True)

def visualize_directory(path, indent=""):
    try:
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}/")
                visualize_directory(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}[Доступ заборонено]")
    except FileNotFoundError:
        print(f"{indent}{Fore.RED}[Файл не знайдено]")

def main():

    if len(sys.argv) < 2:
        
        raw_path = "/Users/Mash2/Documents/CODE/Homework_Mash/"
        print(f"{Fore.YELLOW}Аргумент не передан. Использую путь по умолчанию: {raw_path}")
    else:
        
        raw_path = sys.argv[1]

    
    directory_path = Path(raw_path)

   
    if not directory_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{directory_path}' не існує.")
    elif not directory_path.is_dir():
        print(f"{Fore.RED}Помилка: '{directory_path}' не є директорією.")
    else:
        print(f"{Fore.YELLOW}Структура папки {directory_path}:")
        visualize_directory(directory_path)

if __name__ == "__main__":
    main()