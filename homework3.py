import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def visualize_directory(path, indent=""):
    try:
        
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
    else:
        
        path_str = "." 
        print(f"{Fore.YELLOW}Шлях не вказано. Використовую поточну директорію для демонстрації:")

    directory_path = Path(path_str)

    if not directory_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{path_str}' не існує.")
    elif not directory_path.is_dir():
        print(f"{Fore.RED}Помилка: '{path_str}' це файл, а потрібна директорія.")
    else:
        
        root_name = directory_path.resolve().name if path_str == "." else directory_path.name
        print(f"{Fore.BLUE}{root_name}/")
        visualize_directory(directory_path)

if __name__ == "__main__":
    main()