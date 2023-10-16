records = {}

def user_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params. Use help."
        except KeyError:
            return "Unknown name. Try another or use help."
    return inner

def hello():
    return "How can I help you?" 

@user_error
def add_record(*args):
    if len(args) > 2:
        raise ValueError("Ambiguous input. Please provide only a name and a phone number")
    name = args[0]
    phone_number = args[1]
    records[name] = phone_number
    return f"Add record {name = }, {phone_number = }"

@user_error
def change_record(*args):
    name = args[0]
    new_value = args[1]
    rec = records[name]
    if rec:
        records[name] = new_value
        return f"Change record {name = }, {new_value = }"

@user_error    
def phone(name):
    return records[name]
    
def unknown(*args):
    return "Unknown command. Try again."
        
COMMANDS = {add_record: "add",
            change_record: "change",
            phone: "phone"}

def parser(text: str):
    for func, kw in COMMANDS.items():
        if text.startswith(kw):
            return func, text[len(kw):].strip().split()
    return unknown, []

def main():
    while True:
        user_input = input(">>>")
        if user_input == "hello":
            print(hello())
        elif user_input == "show all":
            print(records)
        elif user_input in ("good bye", "close", "exit"):
            print("Good bye!")
            break 
        else: 
            func, data = parser(user_input)
            print(func(*data))
                
if __name__ == '__main__':
    main()