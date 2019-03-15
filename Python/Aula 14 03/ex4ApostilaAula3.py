xprimeiroponto = float(input())
xsegundoponto = float(input())
yprimeiroponto = float(input())
ysegundoponto = float(input())

d = (((xsegundoponto - xprimeiroponto) ** 2) + ((ysegundoponto - yprimeiroponto) ** 2)) ** (1/2)

print('%.2f' % d)