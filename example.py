import random

def generate_equation():
    operations = ['+', '-', '*', '//']
    operation = random.choice(operations)
    if operation == '*' :
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 10)

    elif operation == '//' :
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 10)
    
    else:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 200)
    equ = f"{num1} {operation} {num2}"
    return equ, eval(equ)

print ("Hello World")
 

