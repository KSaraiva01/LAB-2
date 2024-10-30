# O professor deseja dividir uma turma com N alunos em dois grupos: um com M alunos e outro com (N-M) alunos. Faça
# o programa que lê o valor de N e M e informa o número de combinações possíveis.
# N - Total de alunos
# M - Tamanho de um dos grupos - Deve ser menor que o tamanho total
# Fórmula: N!/(M! * (N-M)!)
# Para calcular o fatorial (!) utilize a biblioteca math com comando math.factorial(value)
import math

def calcular():
    try:
        N = int(input("Digite o numero de alunos:"))
        M = int(input("Digite o numero de grupos:"))
        while M > N:
            M = int(input("numero de grupos invalido, Digite o numero de grupos:"))
            if M >N:
                print("Numero de grupos maior que o de alunos !!!") 
            else:
                break
        combinacoes = math.factorial(N) / (math.factorial(M) * math.factorial(N - M))
        print("o Numeoro de alunos são de ",N ," O numero de grupos são de ",M," Grupos, e a quantidade de combinações possiveis são de ", combinacoes)

    except ValueError as e:
        return "Erro:", e 

def main():
    Resultado = calcular()
main()
