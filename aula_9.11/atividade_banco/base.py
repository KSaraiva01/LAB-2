import menubanco
import Sacar
import Depositar
import mostrar
import extrato



def main():
    saldo = 0.0
    while True:
        opc = menubanco.menu()
        if opc == 1:
            Rsaldo = Sacar.sacar(saldo)
            saldo = Rsaldo
        elif opc == 2:
            Rdeposito = Depositar.depositar(saldo)
            saldo = Rdeposito
        elif opc ==3:
            mostrar.mostrar(saldo)
        elif opc ==4:
            extrato.tomate(saldo)
        elif opc == 5:
            print("Obrigado por usar nosso banco :) ")
            break

main()
