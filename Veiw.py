# View (Представление) - отвечает за отображение и ввод данных
def display_menu():
    print("\nВыбери действие: 1 - Сложить, 2 - Умножить, 3 - Поделить, 4 - Вычитание")
    choice = input("Введи номер действия: ")

    return choice

def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Ошибка: введенное значение не является целым числом. Попробуйте снова.")

def show_result(result):
    print(result)

def get_book_title():
    return input("Введи название книги: ")

def get_num():
    a = get_integer_input("Введи первое число: ")
    b = get_integer_input("Введи второе число: ")
    return a,b

def get_multiplication():
    a = get_integer_input("Введи первое число: ")
    b = get_integer_input("Введи второе число: ")
    return a,b
def get_Division():
    a = get_integer_input("Введи первое число: ")
    b = get_integer_input("Введи второе число: ")
    return a, b
def get_Subtraction ():
    a = get_integer_input("Введи первое число: ")
    b = get_integer_input("Введи второе число: ")

    return a,b

def show_message(message):
    print(message)
