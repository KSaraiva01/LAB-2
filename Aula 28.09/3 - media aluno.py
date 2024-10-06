# 3. Escreva um programa que lê duas notas de vários alunos e armazena tais notas em um dicionário,
# onde a chave é o nome do aluno e o valor é uma lista contendo ambas notas. A entrada de dados deve
# terminar quando for lida uma string vazia como nome. Escreva uma função que retorna a média do
# aluno, dado seu nome.

def lista(alunos):
    while True:
        nome = input("Digite o nome do aluno:")
        if not nome: 
            break
        alunos[nome] = {'N1': int(input("Digite a primeira nota:")) ,'N2': int(input("Digite a segunda nota:"))}
    return alunos

def media(alunos):
    nome = input("Digite o nome do aluno para saber sua media")
    soma = 0 
    media = 0
    if nome in alunos: 
        soma = alunos[nome]['N1'] + alunos[nome]['N2']
        media = soma / 2
    else:
        print("Aluno inexistente!!!")
    print("A media do aluno ", nome," e de ", media)
    return media

def main():
    alunos = {}
    prencher = lista(alunos)
    
    resposta = media(alunos)
main()
