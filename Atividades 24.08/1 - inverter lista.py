#1. Invertendo uma Lista em Python sem Usar Métodos Internos
#Você deve criar uma função chamada inverter_lista que aceita uma lista como entrada e retorna
#uma nova lista que é a inversão da lista original. Não é permitido o uso de métodos internos
#1de reversão de listas, como reverse() ou slicing negativo. Você deve criar a lógica de inversão manualmente.


def inverter_lista(lista,nova_lista):
    indice = len(lista) -1
    while indice >= 0:
        nova_lista.append(lista[indice])
        indice -=1
    return nova_lista


def main():
    lista = [1,2,3,4,5,6,7,8,9,10]
    nova_lista = []
    inverter = inverter_lista(lista, nova_lista)
    print(lista)
    print(nova_lista)

main()