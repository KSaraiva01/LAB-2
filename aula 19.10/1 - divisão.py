 
#1. Crie um programa que receba através de input dois números e retorne sua divisão.
def divisao(n1,n2):
    try:
        div = n1/n2
        return div
    except ZeroDivisionError:
        print("Numero dividido por 0!!!")
        raise

def main():
    n1 = 0 
    n2 = 0 
    while True:
        try:
            n1 = int(input("Digite o primeiro numero :"))
            n2 = int(input("Digite o segundo numero :"))
            resultado = divisao(n1,n2)
            print("O Resultado final é:", resultado )
            break
        except ValueError:
            print("Valor invalido!!!")
        except ZeroDivisionError:
            pass
main()