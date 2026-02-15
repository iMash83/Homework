def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use: change [name] [new_phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error: Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command format. Use: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Error: Contact not found."

def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    # Собираем все контакты в красивый список
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def show_help():
    return """
Available commands:
  hello                      - Greeting
  add [name] [phone]         - Add new contact
  change [name] [new_phone]  - Change contact number
  phone [name]               - Show phone number
  all                        - Show all contacts
  close / exit               - Exit program
"""

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print(show_help())

    while True:
        try:
            user_input = input("Enter a command: ")
            
            # Если ввели пустую строку - просто пропускаем
            if not user_input.strip():
                continue

            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            
            elif command == "hello":
                print("How can I help you?")
                
            elif command == "add":
                print(add_contact(args, contacts))
                
            elif command == "change":
                print(change_contact(args, contacts))
                
            elif command == "phone":
                print(show_phone(args, contacts))
                
            elif command == "all":
                print(show_all(contacts))
            
            elif command == "help":
                print(show_help())
                
            else:
                print("Invalid command. Type 'help' to see commands.")
                
        except ValueError:
            print("Please enter a command.")
        except (KeyboardInterrupt, EOFError):
            print("\nGood bye!")
            break

# ЭТИ ДВЕ СТРОКИ ОБЯЗАТЕЛЬНО ДОЛЖНЫ БЫТЬ В КОНЦЕ:
if __name__ == "__main__":
    main()