# 1. Escreva um programa em Python que verifique se uma chave existe ou não em um dicionário. Se a
# chave existir no dicionário, imprima Verdadeiro. Caso contrário, imprima Falso.

def verificar(dicionario):
    chave = input("Diigite a chave que quer verificar:")
    if chave in dicionario:
        print(True)
    else: 
        print(False)

def main():
    dicionario = { 'nome' : 'kaua' , 'idade' : '19'}
    resultado = verificar(dicionario)

main()
