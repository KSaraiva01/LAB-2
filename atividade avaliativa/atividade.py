# Adicionar um produto: Solicite o nome do produto, quantidade em estoque e preço unitário. 
# Armazene essas informações em um dicionário dentro do dicionário estoque.

# Buscar um produto: Solicite o nome do produto e exiba as informações disponíveis, incluindo quantidade em estoque e preço unitário.

# Visualizar todos os produtos: Mostre uma lista de todos os produtos disponíveis, juntamente com suas quantidades e preços.

# Vender um produto: Solicite o nome do produto vendido e a quantidade vendida. Atualize a quantidade em estoque e calcule o valor total da venda.

# Relatório de Vendas: Mostre um relatório que liste todas as vendas realizadas, incluindo o nome do produto,
# a quantidade vendida e o valor total da venda.


def menu(armazem, relatorio):
    while True:
        print("1 - Adicionar produto\n2 - Buscar produto\n3 - visualizar todos os produtos\n4 - Vender produto\n5 - Relatório de venda\n6 - Sair")
        opc = int(input("Digite uma opção : "))
        if opc == 1:
            nome = input("Digite o nome do produto :")
            armazem[nome] = {'Quantidade' : int(input("DIGITE A QUANTIDADE DO PRODUTO : ")), 'Valor' : float(input("DIGITE O VALOR DO PRODUTO :"))}
        elif opc == 2:
            buscar = input("Qual produto deseja buscar : ")
            if buscar in armazem:
                print(armazem[buscar]) 
            else:
                print("Produto não encontrado em estoque !!")
        elif opc == 3:
            print(armazem)
        elif opc == 4:
            vender = input("Qual produto quer vender ? : ")
            Quanti = int(input("Digite Quantos produtos deseja? : "))
            if vender not in armazem:
                print("Produto sem estoque!")
            elif Quanti > armazem[vender]['Quantidade']:
                print("Quantidade indisponível no estoque.")
            else:
                armazem[vender]['Quantidade'] -= Quanti
                relatorio.append("Item", vender," Vendido,", Quanti, "Quantidades vendidas ")
            if armazem[vender]['Quantidade'] <= 0:
                del armazem[vender]
        elif opc == 5:
           print(relatorio)
        elif opc == 6 or opc == False :
            break
        else:
            print("opção invalida!!!")
    return armazem, relatorio

def main():
    armazem = {}
    relatorio = []
    manupular_menu = menu(armazem, relatorio) 

main()