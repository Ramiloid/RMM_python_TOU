# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def calculate(a, b, x):
    # Use a breakpoint in the code line below to debug your script.
    try:
        if (x >= 5):
            y = (5*pow(x,2))/(6*pow(a+b,2))
        else:
            y = pow(x,3)*(a+b)

        print("y=" + str(y))
    except ValueError:
        print("Неверные значения попробуйте еще раз")





if __name__ == '__main__':
    while True:
        try:
            a = int(input("Введите А "))
            b = int(input("Введите B "))
            x = int(input("Введите X "))
            calculate(a, b, x)
            break
        except Exception:
            print("Неверные значения, попробуйте еще раз")






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
