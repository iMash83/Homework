def total_salary(path):
    total_sum = 0
    count = 0
    
    with open(path) as file:
        for line in file:
            
            print(f"Прочитана строка: {line.strip()}")

            
            name, salary = line.split(',')
            total_sum += float(salary)
            count += 1

    if count == 0:
        return 0, 0

    average_salary = total_sum / count
    return total_sum, average_salary


total, average = total_salary("/Users/Mash2/Documents/CODE/Homework_Mash/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")