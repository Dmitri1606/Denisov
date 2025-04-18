import flet as ft


def main(page: ft.Page):
    page.title = "Окно с кнопкой"
    a = 0

    # Поле для вывода результата
    result_text = ft.Text(str(a), size=30)

    # Функция обработки нажатия кнопок
    def calculate(e):
        nonlocal a

        operation = e.control.text  # Узнаем, какую кнопку нажали

        # Вычисляем результат
        if operation == "+":
            a = a + 1
        elif operation == "-":
            a = 0

        result_text.value = str(a)
        page.update()  # Обновляем интерфейс

    # Кнопки операций
    buttons = [
        ft.ElevatedButton(op, on_click=calculate) for op in ["+", "-"]
    ]

    # Добавляем все элементы в окно
    page.add(result_text, *buttons)  # Распаковываем список кнопок


ft.app(target=main)