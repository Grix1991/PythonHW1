# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

x = input("Введите трехзначное число: ")
x = int(x)
 
d1 = x % 10
x = x // 10
d2 = x % 10
x = x // 10
 
print("Сумма цифр числа:", x + d1 + d2)