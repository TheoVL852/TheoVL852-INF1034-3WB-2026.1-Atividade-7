

num1 = (input('--> '))
op = input('--> ')
num2 = (input('--> '))
resultado = 0

if num1.isdigit() == True:
    num1=int(num1)
if num2.isdigit() == True:
    num2=int(num2)

if op == 'x':
    resultado = num1*num2
    print(f'= {resultado}')
elif op == '/':
    resultado = num1/num2
    print(f'= {resultado:.2f}')
elif op == '+': 
    resultado = num1+num2
    print(f'= {resultado}')
elif op == '/':
    resultado = num1-num2
    print(f'= {resultado}')
else:
    print('Insira um operador válido')


