print("0 в качестве знака операции"
      "\nзавершит работу программы\n")

def calc(x,a,b):
    if x == '+':
        return a + b
    elif x == '-':
        return a - b
    elif x == '*':
        return a * b
    elif x == '/':
        if b != 0:
            return a / b

while True:
    x = input("Знак (+, -, *, /): ")
    if x == '0':
        break
    if x in ('+', '-', '*', '/'):
        a = float(input("a = "))
        b = float(input("b = "))
        if x == '+':
            print("%.2f" % calc(x, a, b))
        elif x == '-':
            print("%.2f" % calc(x, a, b))
        elif x == '*':
            print("%.2f" % calc(x, a, b))
        elif x == '/':
            if x != 0:
                print("%.2f" % calc(x, a, b))
            else:
                print("Деление на ноль!")
        else:
            print("Неверный знак операции!")