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
            a, b = get_multiplication()

            show_result(multiplication(a,b))




        elif choice == "3":
            a,b= get_Division()
            if b==0:
             print("На ноль делить нельзя")
             main()
            else:
             show_result(Division(a, b))
        elif choice=='4':
            a,b = get_Subtraction()

            show_result(Subtraction(a, b))

        elif choice == "0":
            show_message("Пока!")
            break



main()
