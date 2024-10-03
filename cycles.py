фрукты = ["яблоко", "банан", "вишня"]
for фрукт in фрукты:
    print(фрукт)

collection = [1,2,3,4,5,6,7,8,9,10]

n = 10

for i in collection:

      l = n*i

      print(l)

слово = "Python"
for буква in слово:
    print(буква)

n = 1
while n < 6:
    print('Цикл выполнился', n, 'раз(а)')
    n = n+1

a = 6

while a > 0:

    a -= 1

    print(a)

x = 6

while x > 0:

    x -= 1

    if x == 3:

        continue

    print(x)

print('Конец цикла')
