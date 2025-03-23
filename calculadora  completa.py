def adicionar(x, y):
    return x + y
def subrair (x, y):
    return x - y
def multiplicar (x, y):
    return x * y
def dividir (x, y):
    if y == 0:
        return 'erro divisão por zero'
    return x / y
def potencia (x, y):
    return x ** y
print('selecione a operação')
print('1. adição')
print('2. subtração')
print('3. multiplicação')
print('4. divisão')
escolha = input('digite a operação desejada (1/2/3/4):')
num1 = int(input('dugite o primeiro número'))
num2 = int(input('digite o segundo número'))
if escolha == '1':
    print(num1, '+', num2, '=',adicionar(num1, num2))
elif escolha == '2':
    print(num1, '-', num2, '=',subrair(num1, num2))
elif escolha == '3':
    print(num1, '*', num2, '=',multiplicar(num1, num2))
elif escolha == '4':
    print(num1, '/', num2, '=',dividir(num1, num2))
else:
    print('operação invalida')
