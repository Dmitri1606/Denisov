from Model import *
from Veiw import *

# Controller (Контроллер) - управляет логикой и связывает модель с представлением
def main():
    while True:
        choice = display_menu()

        if choice == "1":
            a, b = get_num()

            show_result(summ(a, b))

        elif choice == "2":
                a,b = get_multiplication()

                show_result(multiplication(a,b))

        elif choice == "3":
            book_list = get_books()
            show_books(book_list)
            index_input = get_book_index()
            try:
                index = int(index_input)
                if remove_book(index):
                    show_message("Книга удалена")
                elif len(books)<index:
                    show_message("Такого индекса нет")
            except ValueError:
                show_message("Введи корректный номер")
        elif choice == "0":
            show_message("Пока!")
            break
        else:
            show_message("Неверный выбор, попробуй снова")


main()

# # Запуск программы
# if __name__ == "__main__":
#     main()