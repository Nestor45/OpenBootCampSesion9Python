from tkinter import Y


def lista_paises():
    lista = []
    perdi_pais = input("Insertar pais (Y/n):  ")
    while (perdi_pais == 'y' or perdi_pais == 'Y'):
        insertar_pais = input("Introduce el pais (Y/n):  ")
        if(insertar_pais == 'n'):
            break
        else:
            lista.append(insertar_pais)
    lista_ordenada = sorted(set(lista))
    for pais in range(len(lista_ordenada)):
        if pais < len(lista_ordenada)-1:
            print(lista_ordenada[pais], end=", ")
        else:
            print(lista_ordenada[pais])
lista_paises()
