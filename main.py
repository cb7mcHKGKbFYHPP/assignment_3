def isNumber(s): 
    negative = False
    if(s[0] =='-'): 
        negative = True
          
    if negative == True: 
        s = s[1:] 
    try: 
        n = int(s) 
        return True
    except ValueError: 
        return False
          
def inputt():
    print("Введіть лабіринт, позначаючи стінки x, а прохід пробілом. Коли закінчите введення, введіть ok.")
    labirint = [] #масив лабіринту
    row = [] #кожен рядок, який вводиться користувачем
    while True:
        user_input = str(input())
        if user_input == "ok":
            break
        for symbol in user_input:
            if symbol != "x" and symbol != " ":
              print("Недопустимый символ ", symbol) 
              inputt()
            else: continue
        for element in user_input:
            row.append(element)
        labirint.append(row)
        row = []
    return labirint


def out(labirint):
    print(labirint)
    for row in labirint:
        for element in row:
           print(element, end = "")
        print("")
    return


'''
ПРОГРАМА ПРАЦЮЄ НЕКОРЕКТНО! Ось алгоритм, який я намагався реалізувати.

АЛГОРИТМ
1. Створити матрицю-результат.
2. Почати пошук шляху з клітини n=0. Нумерувати клітинки n + 1.
3. Якщо тупик і всі шляхи пройдені, то нічого не робити; якщо точка досягнута, то запам'ятати цей варіант.
4. Відкат назад до альтернативи.
4.1. Відкочувати назад по клітинці і дивитися на сусідні клітинки.
4.2. На перехресті йти туди, де клітинка порожня.
5. Повторити пошук шляху.
6. Якщо натрапив на пройдену раніше клітку:
Число клітини менше поточної: значить, цей шлях не оптимальний. Відкат назад.
Число клітини більше поточної: перезаписати клітку і йти далі.
7. Повторювати, доки не будуть заповнені усі клітини коло фінальної точки.
8. Найкоротший шлях визначається n - 1 від найменшоо значення суміжних клітинок з фінальною клітинкою.
'''

def goto(next_x, next_y):
    global x
    global y
    global labirint
    x = next_x
    y = next_y
    print(x, " ", y)
    return

def check_cell(x, y):
    global n
    global labirint
    this = str(labirint[x][y])
    if isNumber(this):
        if int(this)>n:
           return False # go_back()
        elif int(this)<=n:
            labirint[x][y]=n
            n += 1
            return True
    else:
        labirint[x][y]=n   #що не так?
        n += 1
        return True


def find_a_way():
    global x
    global y
    global labirint
    #labirint[x][y] = "0"
    #Якщо оголосити тут змінну n, алгоритм в рекурсії її не побачить. Цікаво, чому.
    while True:
       if labirint[x-1][y] == 'x':    #крок вліво
          pass
       else:
           goto(x-1, y)
           #на цей момент значення x y вже нові!
           bbool = check_cell(x, y)
           if bbool == False:
               return
       if labirint[x+1][y] == 'x':    #крок вправо
          pass
       else:
           goto(x+1, y)
           #на цей момент значення x y вже нові!
           bbool = check_cell(x, y)
           if bbool == False:
               return
       if labirint[x][y+1] == 'x':    #крок донизу
          pass
       else:
           goto(x, y+1)
           #на цей момент значення x y вже нові!
           bbool = check_cell(x, y)
           if bbool == False:
               return
       if [x][y-1] == 'x':    #крок догори
          pass
       else:
           goto(x, y-1)
           #на цей момент значення x y вже нові!
           bbool = check_cell(x, y)
           if bbool == False:
               return


n = int(0)
labirint = inputt()
out(labirint)
x = int(input("Введите х: "))
y = int(input("Введите у: "))
find_a_way()
out(labirint)
