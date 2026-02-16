from datetime import datetime

date_input = input("Введите дату (например, 22.02.2026 или 22/02/2026): ")

# 1. Заменяем все возможные разделители на один стандартный (например, точку)
clean_date = date_input.replace("/", ".").replace("-", ".")

try:
    # 2. Теперь парсим строку, зная, что там точно точки
    event_date = datetime.strptime(clean_date, "%d.%m.%Y")
    print(f"Успех! Дата распознана: {event_date}")
    
except ValueError:
    print("Ошибка: Кажется, вы ввели дату в неверном порядке или использовали странные символы.")