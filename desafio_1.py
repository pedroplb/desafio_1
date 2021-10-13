#2 random
import random

#1 ler os nomes
with open("C:\\Users\\pedro\\Documents\\Treinamento_python\\projeto_1\\venv\\pessoas_sorteio.txt", "r", encoding="latin1") as arq:

    nomes=[]

    #guarda o nome em uma lista
    for nome in arq:
        nomes.append(nome)

sorteado = 0
sorteado = random.randint(0,9999)

premiados = {"primeiro":"nome","segundo":"nome","terceiro":"nome"}
premiados["primeiro"] =nomes[sorteado]
nomes.remove(nomes[sorteado])

sorteado = random.randint(0,9998)

premiados["segundo"] =nomes[sorteado]
nomes.remove(nomes[sorteado])

sorteado = random.randint(0,9997)

premiados["terceiro"] =nomes[sorteado]
nomes.remove(nomes[sorteado])

for posicao in premiados:
    print(f"O {posicao} foi : {premiados[posicao]}")

with open("C:\\Users\\pedro\\Documents\\Treinamento_python\\projeto_1\\venv\pessoas_resultado.txt", "w+") as arqSai:
    for posicao in premiados:
        arqSai.write(f"{posicao} - {premiados[posicao]}")
