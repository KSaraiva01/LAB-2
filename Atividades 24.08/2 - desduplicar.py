# Crie um método que receba uma lista com elementos duplicados. 
# Ela deve gerar uma lista com os elementos que estava duplicados e uma lista com os elementos unificados.

def desduplicar(lista,desduplicado, duplicados):
    for i in range(len(lista)):
        if lista[i] not in desduplicado:
            desduplicado.append(lista[i])
        else:
            duplicados.append(lista[i])
    return desduplicado, duplicados


        
    return nova_lista

def main():
    lista = [1,1,2,2,3,3,4,4,5,6,7,7,8,9,9,9,10]
    desduplicados = []
    duplicados = []
    inverter = desduplicar(lista, desduplicados, duplicados)
    print("Lista original:", lista)
    print("lista dos item que estavam duplicados:", duplicados)
    print("lista dos item sem repetição:", desduplicados)

main()