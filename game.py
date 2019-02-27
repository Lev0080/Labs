import random

print ("Введите границы промежтука для угадывания числа")
print ("Введите левую границу")
x= int(input())
print("Введите правую границу")
y= int(input())
n= random.randint(x,y)
m= int(input())
while m!=n:
        if(m>n):
          print("Заданное число меньше")
        else:
                print("Заданное число больше")
        m=int(input())
print("Победа")
