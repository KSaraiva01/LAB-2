# 2. Crie um programa que receba através de um input o valor numérico de um mês e retorne seu valor escrito. 
# Lembre de tratar as exceções do seu programa. Exemplo: 1 -> Janeiro, 12 -> Dezembro

class foradamargem(BaseException):
    pass
meses = [0, "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro" , "dezembro"]

def main():
    N = None
    while True:
        try:
            N = int(input("Digite o numero de um mês :"))
            if  N < 1 or N > 12:
                raise foradamargem("Numero de mês invalido !!!")
            break
        except ValueError:
            print("Valor invalido !!!")
        except foradamargem as e:
            print(e)
    print("O seu mês e", meses[N])
main()