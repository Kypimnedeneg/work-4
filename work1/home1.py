n = int(input("Введите число: "))
if n <= 999 and n >= 100:
    a = n % 10 
    b = n // 10 % 10 
    c = n // 10 // 10 % 10 
    print (f"Сумма: {a + b + c}")
else:
    print("Число не трёхзначное")