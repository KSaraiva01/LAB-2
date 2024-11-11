
import menu
import soma

def main():
    while True:
        opcao = menu.menu()
        if opcao == 1:
            resultado = soma.somar(1,2)
            print(resultado)
        break
main()