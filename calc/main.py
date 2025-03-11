import os
import time 
from calc import add, sub,mul,div

def select(num1,num2,option):
    if option == 1:
        print("Result : ",add(num1,num2))
    elif option ==2 :
        print("Result : ",sub(num1,num2))
    elif option ==3:
        print("Result : ",mul(num1,num2))
    elif option ==4:
        print("Result : ", div(num1,num2))
    else:
        print("Erro : incorrect option")

print("Calculator")
num1 = int(input("Enter the no1 : "))
num2 = int(input("Enter the no2 : "))

print("1. add\n2. sub\n3. multi\n4. div")
option = int(input("Enter the option : "))

select(num1,num2,option)
time.sleep(5)
os.system("cls")