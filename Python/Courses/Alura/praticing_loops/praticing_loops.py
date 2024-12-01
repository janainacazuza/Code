#Exercise 1 : 

clients = ['João', 'Maria', 'Carlos', 'Ana', 'Beatriz']

for client in clients:
    print(client)

#Exercise 2 :
i = 0
message = "Bem-vindo ao Buscante!"
while i < 5:
    print(message)
    i += 1

# Exercise 3 :
valores = [10, 20, 30, 40, 50]

soma = 0
for valor in valores:
    soma += valor

print(f"A soma total dos valores é: {soma}")

# Exercise 4 :

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
for projeto in projetos: 
    if projeto == None:
        print("Projeto ausente")
    else:
        print(f"Projeto: {projeto}")

# Exercise 5 :
livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
for livro in livros:
    if livro == "O Hobbit":
        print(f"Livro encontrado: {livro}" )
        break

# Exercise 6 :
estoque = 5
