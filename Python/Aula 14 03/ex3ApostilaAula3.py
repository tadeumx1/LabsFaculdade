
# EXEMPLO

numero = int(input('Digite um numero de 3 digitos: '))

a = numero // 1 % 10
b = numero // 10 % 10
c = numero // 100 % 10
d = numero // 1000 % 10
e = numero //10000 % 10

print(a, b, c)


# SOMENTE EXEMPLO: 123

x = int(input('Valor: '))


print(x % 10, end='') # No exemplo, aqui saiu o 3 !
x = x // 10 # Tirou o digito mais a direita o 3

print(x % 10, end='') # No exemplo, aqui saiu o 2 !
x = x // 10 # Tirou o digito mais a direita o 2

print(x % 10, end='') # No exemplo, aqui saiu o 1 !
x = x // 10 # Tirou o digito mais a direita o 1