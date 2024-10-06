# 2. Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em
# um dicionário, onde a chave é a vogal considerada.
def verificar(vogais, frase):
    for letra in frase:
        if letra in vogais:
            vogais[letra] += 1
               
    return vogais

def printar(vogais):
    print("A quantidade de vogais que apareceram no texto e:")
    for i in vogais:
        print(i,"-", vogais[i]) 

def main():
    vogais = {
        'a' : 0,
        'e' : 0,
        'i' : 0,
        'o' : 0,
        'u' : 0,
    }
    frase = input("Digite uma Frase: ").lower()
    resultado = verificar(vogais,frase)
    mostrar = printar(vogais)
main()