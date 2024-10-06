# lista = chave = nome, valor = quantidade, fazer menu - adicionar produto, remover produto,
# alterar intem(informa item, verificar iten, se existir pedir uma nova qunatidade,
# porem se informar quantidade 0 = remover produto), listar itens 

def menu(lista):
    while True:
        print("--Lista de compras--\n1 - Adicionar produto\n2 - Remover Produto\n3 - Alterar item\n4 - Listar itens\n5 - Sair")
        opc = int(input("Digite uma opção :"))
        if opc == 1:
            nome = input("Digite o nome do produto:")
            lista[nome] = int(input("Digite a Quantidade do produto : "))
        elif opc == 2:
            remover = input("Qual item deseja retirar ? ")
            if remover in lista:
                del lista[remover] 
            else:
                print("Item não encontrado!!!")
        elif opc == 3:
            alterar = input("Qual item deseja alterar a quantidade ? ")
            quantidade = int(input("Digite a quantida : "))
            if quantidade == 0:
                del lista[alterar]
            elif alterar in lista:
                lista[alterar] = quantidade
            else:
                print("Item não encontrado!!!")

        elif opc == 4:
            for nome in lista:
                print(nome,":", lista[nome])
        elif opc == 5:
            break
        else:
            print("Opção invalida!!!!")
    return lista



def main():
    lista = {}
    resultado = menu(lista)


main()