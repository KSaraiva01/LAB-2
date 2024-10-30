# Crie uma função que recebe um ano através de um input e defina se o mesmo é bissexto ou não. Utilize as seguintes
# regras: Um ano bissexto é divisível por 4, mas não por 100, ou então se é divisível por 400. Exemplo: 1988 é bissexto pois
# é divisível por 4 e não é por 100; 2000 é bissexto porque é divisível por 400.
def verificar():
    try:
        ano = int(input("Digite um ano para saber se ele e bissexto ou não: "))
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0 :
            print("O ano ",ano, "é bissexto!!")
        else: 
            print("O ano ",ano,"Não é bissexto!!")
    except ValueError:
        print("Valor invalido!!!!")


def main():
    resultado = verificar()  

main()