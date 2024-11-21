import menu 
import iniciar
import verscore
import jogadorscore

def main():
    while True:
        opc = menu.menu()
        if opc == 1:
            inicio = iniciar.jogar()
        elif opc ==2:
            ver = verscore.score()
        elif opc ==3:
            jover = jogadorscore.score()
        elif opc ==4:
            print('Obrigado por jogar!!')
            break

main()