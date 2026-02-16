import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def visualize_directory(path, indent=""):
    try:
        if not path.exists():
            print(f"{indent}{Fore.RED}[Шлях не знайдено]")
            return

        items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name))

        for item in items:
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}/")
                visualize_directory(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")

    except PermissionError:
        print(f"{indent}{Fore.RED}[Доступ заборонено]")
    except Exception as e:
        print(f"{indent}{Fore.RED}[Помилка: {e}]")

def main():
    
    if len(sys.argv) > 1:
        path_str = sys.argv[1]
        print(f"{Fore.YELLOW}Аналіз директорії за вказаним шляхом: {path_str}")
    else:
        path_str = "."
        print(f"{Fore.YELLOW}Шлях не вказано. Використовую поточну директорію.")

    directory_path = Path(path_str)

    if not directory_path.exists() or not directory_path.is_dir():
        print(f"{Fore.RED}Помилка: '{path_str}' не є директорією або не існує.")
    else:
        visualize_directory(directory_path)

if __name__ == "__main__":
    main()