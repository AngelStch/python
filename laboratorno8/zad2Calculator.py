import cal

print("Добре дошли в калкулатора!")
print("Изберете операция:")
print("1. Събиране")
print("2. Изваждане")
print("3. Умножение")
print("4. Деление")
choice = input("Въведете номер на операция: ")
try:
    num1 = int(input("Въведете първото число: "))
    num2 = int(input("Въведете второто число: "))
    if choice == '1':
        print(f"Резултатът от събирането е: {cal.addd(num1, num2)}")
    elif choice == '2':
        print(f"Резултатът от изваждането е: {cal.subtract(num1, num2)}")
    elif choice == '3':
        print(f"Резултатът от умножението е: {cal.multiply(num1, num2)}")
    elif choice == '4':
        if num2 == 0:
            print("Не може да се дели на нула!")
        else:
            print(f"Резултатът от делението е: {cal.divide(num1, num2)}")
    else:
        print("Невалиден избор!")
except ValueError:
    print("Моля, въведете валидни цели числа.")


