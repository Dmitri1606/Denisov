# View (Представление) - отвечает за отображение и ввод данных
def display_menu():
    print("\nВыбери действие: 1 - Умножить, 2 - Сложить, 3 - Поделить")
    choice = input("Введи номер действия: ")

    return choice

def show_result(result):
    print(result)

def get_book_title():
    return input("Введи название книги: ")

def get_num():
    a = int(input("Введи первое число: "))
    b = int(input("Введи второе число: "))
    return a,b

def get_multiplication():
    a = int(input("Введи первое число: "))
    b = int(input("Введи второе число: "))
    return a,b

def show_message(message):
    print(message)