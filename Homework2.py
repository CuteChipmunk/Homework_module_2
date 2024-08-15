first = int(input("Введите первое число"))
second = int(input("Введите второе число"))
third= int(input("Введите третье число"))
if first == second and second == third :
    print(3)
elif first == second and first != third or second == third and second != first or third == first and third != second :
    print(2)
elif first != second and second != third :
    print(0)