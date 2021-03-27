import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.interactive(True)

#-----------------------------------------------------------
# Leitura do arquivo csv com as notas
#-----------------------------------------------------------
alunos = []
with open("alunos.csv") as csv:
    csv.readline()
    for line in csv:
        line = line.split(";")
        nome = line[0]
        e1 = float(line[1])
        e2 = float(line[2])
        alunos.append([nome, e1, e2])

print("-" * 50)
#-----------------------------------------------------------
# Número de alunos aprovados, reprovados e em exame.
#-----------------------------------------------------------
aprovados = 0
reprovados = 0
em_exame = 0

for aluno in alunos:
    # Calcula a média para cada aluno
    media = (aluno[1] + aluno[2]) / 2
    # Adiciona ao final da lista de cada aluno e valor da média
    aluno.append(media)
    
    # Se maior|igual que 7               -> Aprovado
    # Se maior|igual que 4 e menor que 7 -> Em exame
    # Senão (menor que 4)                -> Reprovado
    if media >= 7:
        aprovados += 1
    elif (4 <= media) and (media < 7):
        em_exame += 1
    else:
        reprovados += 1

print("Aprovados:  ", str(aprovados))
print("Em exame:   ", str(em_exame))
print("Reprovados: ", str(reprovados))

print("-" * 50)
#-----------------------------------------------------------
# Nome do aluno com maior e menor notal final.
#-----------------------------------------------------------

# Inicialização das listas que receberão as informações de nome e nota
# do aluno que teve a maior e menor média final
maior_media = ['', 0]
menor_media = ['', 10]

for aluno in alunos:
    # aluno[3] contém a média final do curso
    if aluno[3] > maior_media[1]:
        maior_media = [aluno[0], aluno[3]]

    if aluno[3] < menor_media[1]:
        menor_media = [aluno[0], aluno[3]]

print("Aluno com a MAIOR média: ", maior_media[0])
print("Aluno com a MENOR média: ", menor_media[0])

print("-" * 50)
#-----------------------------------------------------------
# Número de alunos ACIMA da média na 1a avaliação.
#-----------------------------------------------------------
alunos_acima_da_media = 0

for aluno in alunos:
    # Testando apenas MAIOR que 7 pois o problema pede ACIMA da média da Av 1
    # e não com nota MAIOR ou IGUAL a média
    if aluno[1] > 7:
        alunos_acima_da_media += 1

print("Número de alunos ACIMA da média na 1a avaliação: ", alunos_acima_da_media)

print("-" * 50)
#-----------------------------------------------------------
# Histograma da 2a avaliação.
#-----------------------------------------------------------

# Intervalos determinados
intervalos = ["0-0.9", "1-1.9", "2-2.9", "3-3.9", "4-4.9", "5-5.9", "6-6.9", "7-7.9","8-8.9", "9-10"]

# Lista para as contagens, onde cada posição correponde a um intervalo 
notas = [0] * len(intervalos)

for aluno in alunos:
    # aluno[2] contém as notas da Av 2
    # Entre 0 e 0.9
    if (0 <= aluno[2]) and (aluno[2] < 1):
        notas[0] += 1
    # Entre 1 e 1.9
    elif aluno[2] < 2:
        notas[1] += 1
    # Entre 2 e 2.9
    elif aluno[2] < 3:
        notas[2] += 1
    # Entre 3 e 3.9
    elif aluno[2] < 4:
        notas[3] += 1
    # Entre 4 e 4.9
    elif aluno[2] < 5:
        notas[4] += 1
    # Entre 5 e 5.9
    elif aluno[2] < 6:
        notas[5] += 1
    # Entre 6 e 6.9
    elif aluno[2] < 7:
        notas[6] += 1
    # Entre 7 e 7.9
    elif aluno[2] < 8:
        notas[7] += 1
    # Entre 8 e 8.9
    elif aluno[2] < 9:
        notas[8] += 1
    # Entre 9 e 10
    else:
        notas[9] += 1

# Plot do gráfico
plt.bar(intervalos, notas, 0.8)
plt.title('Histograma da 2a Avaliação')
plt.xlabel("Notas")
plt.ylabel("Número de Alunos")
plt.yticks(range(0, 10))
plt.grid(axis='y', linestyle='--', alpha=0.1)
plt.show()

input("ENTER para terminar")
plt.close()