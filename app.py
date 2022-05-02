from functools import reduce
lista_numeros = [2,3,4,5,6,7,8,9,10,11,12,13]

res_impares = filter(lambda x: x%2!=0,lista_numeros)

lis_impares = list(res_impares)
print(f"Lista impares: {lis_impares}")

suma_impares=reduce(lambda x,y:x+y,lis_impares)
print(f"Suma impares: {suma_impares}")
