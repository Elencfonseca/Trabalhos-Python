nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
matriculado = input("você esta matriculado? (s/n): ")

if matriculado.upper() == "s":
    matriculado = True

print(f"Nome: {nome}")
print(f"idade: {idade} anos")
print(f"Matriculado: {'sim' if matriculado else 'não'}")


