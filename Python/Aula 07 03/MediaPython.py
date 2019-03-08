primeira = float(input('Digite a primeira nota: '))
segunda = float(input('Digite a segunda nota: '))
terceira = float(input('Digite a terceira nota: '))
quarta = float(input('Digite a quarta nota: '))

media = (primeira + segunda + terceira + quarta) / 4

if media >= 6:
    print('Sua média foi %s você foi aprovado!' % media)
else:
    print('Sua média foi %s você foi reprovado!' % media))


