from pathlib import Path

def total_salary(path):
    total_sum = 0
    count = 0
    
    try:
        with open(path, 'r') as file:
            for line in file:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue  
                
                try:
                    name, salary = cleaned_line.split(',')
                    total_sum += float(salary)
                    count += 1
                except ValueError:
                    print(f"Ошибка парсинга строки: {cleaned_line}")
                    continue

    except FileNotFoundError:
        print(f"Файл по пути '{path}' не найден.")
        return 0, 0
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return 0, 0

    average_salary = total_sum / count
    return total_sum, average_salary

if __name__ == "__main__":
    path_to_file = "salary_file.txt" 
    
    total, average = total_salary(path_to_file)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")