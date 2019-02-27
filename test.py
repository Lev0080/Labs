a=int(input())
b=int(input())
c=int(input())
k=int(input())
try:
 print (abs((a**2/b**2+c**2*a**2)/(a+b+c*(k-a/b**3))+c+(k/b-k/a)*c))
except ZeroDivisionError:
 print ("Деление на ноль")
