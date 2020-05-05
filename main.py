
def is_digit(string):
    if string.isdigit() or string == "0":
       return int(string)
    else:
        try:
            string = string.replace(',','.')
            float(string)
            return float(string)
        except ValueError:
            return "alfa"

def vvod():
    a = input("Введите первое число \n")
    a = is_digit(a)
    if a == "alfa":
        print("Введено неправильное значение")
        vvod()
    znak_oper = input("Введите '+' для сложения, '-' для вычитания \n")
    if znak_oper != "+" and znak_oper != "-":
        print("Введено неправильное значение")
        vvod()
    b = input("Введите второе число \n")
    b = is_digit(b)
    if b == "alfa":
        print("Введено неправильное значение")
        vvod()
    return a,b,znak_oper

def sum(a,b):
    return a + b

def sub(a,b):
    return a - b

while True:

    a,b,znak_oper = vvod()

    if znak_oper == "+":
        print(f"Результат вычисления {a} + {b} = ", sum(a,b))
    elif znak_oper == "-":
        print(f"Результат вычисления {a} - {b} = ", sub(a,b))
    else:
        print("Ошибка")






