# Дано число N (N > 0). Найти сумму N² + (N + 1)² + (N + 2)² + ... + (2N)²

N = int(input("Введите число N"))

while type(N) != int:
    try: N = int(N)
    except:
        print('Ошибка: Некоректно введены данные!')
        N = int(input("Введите целое число"))

while N <=0:
    print('Ошибка: Число меньше или равно 0!')
    num = input('Введите число больше 0: ')

sum = 0
current = N

while current <= 2 * N:
    sum += current ** 2
    current += 1

print("Сумма равна: ", sum)