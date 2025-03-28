
# Model (Модель) - отвечает за данные и логику работы с ними
books = ["Война и мир", "Гарри Поттер", "Мастер и Маргарита"]

def summ(a,b):
    result = a+b
    return result
def multiplication(a,b):
    sen= a*b
    return sen
def remove_book(index):
    if 0 <= index < len(books):
        books.pop(index)

def get_books():
    return books