
possible_operations = ['+', '-', '*', '/']


def addition(var_1, var_2) -> int:
    return var_1 + var_2


def subtraction(var_1, var_2):
    return var_1 - var_2


def multiplication(var_1, var_2):
    return var_1 * var_2


def division(var_1, var_2):
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        return None


def input_data():
    global_flag = True
    while global_flag:
        expression = input("Введите выражение в польской нотации (+ 2 2): ").split(' ')
        if len(expression) > 3:
            print("Вы ввели недопустимое количество элементов")
            continue
        operation = expression[0]
        assert operation in possible_operations, f"Введена некорректная арифметическая операция! Доступные операции: {possible_operations}"

        assert expression[1].isdigit(), "Первое значение в формуле должно быть положительным числом!"
        assert expression[2].isdigit(), "Второе значение в формуле должно быть положительным числом!"
        
        var_1 = int(expression[1])
        var_2 = int(expression[2])

        return operation, var_1, var_2


def main():
    print("Вычисление по польской нотации")
    print("Для положительных чисел")
    print(f"Доступные операции: {possible_operations}")
    print("-" * 40)
    operation, var_1, var_2 = input_data()
    if operation == '+':
        print(f"{operation} {var_1} {var_2} = {addition(var_1, var_2)}")

    if operation == '-':
        print(f"{operation} {var_1} {var_2} = {subtraction(var_1, var_2)}")

    if operation == '*':
        print(f"{operation} {var_1} {var_2} = {multiplication(var_1, var_2)}")

    if operation == '/':
        if division(var_1, var_2) is None:
            print("Деление на ноль!")
        else:
            print(f"{operation} {var_1} {var_2} = {division(var_1, var_2)}")


if __name__ == '__main__':
    main()
