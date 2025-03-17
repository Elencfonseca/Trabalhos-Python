import random
def sorteio_aluno():
    alunos = [
        "Jose", "ana", "pedro",
        "julia", "maria", "fabiana"
    ]
    escolher = random.choice(alunos)
    print(f"o aluno escolhido foi: {escolher}")
sorteio_aluno()
# Sorteio com números
import random
def sorteio_numeros():
    numeros = [
        "10", "5", "6"
        "7", "3", "9"
    ]
    escolher = random.choice(numeros)
    print(f"o numero escolhido escolhido foi: {escolher}")
sorteio_numeros()