def facto(num):
    if num < 0:
        return f'Não é possivel realizar o fatorial de {num} pois é um número negativo!'
    elif num == 0 or num == 1:
        return 1
    else:
        return num * facto(num-1)
def num_par(n):
    return n if n % 2 == 0 else None


from functools import reduce
fac = reduce(lambda x,y: x*y, range(1, 7))
print(fac)