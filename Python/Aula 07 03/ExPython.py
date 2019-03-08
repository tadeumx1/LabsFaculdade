nome = input('Seu nome: ')
sobre = input('Sobrenome: ')
idade = int(input('Idade: '))

print('Olá, {} {} {}'.format(nome, sobre, idade))


if idade < 18:
    print('Nada de Deadpool')
else:
    print('Pode assistir')
