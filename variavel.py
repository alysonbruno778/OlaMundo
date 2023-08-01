# input é uma função que permite perguntar algo ao usuário
# nome = input("Qual é o seu nome?")

'''
bloco
de 
comentário
permite que várias linhas se tornem um comentário
'''

# print("Olà,", nome,".Tudo bem com você?")

# print(type(nome))

a = 10
b = 5.8
c = "Rio de Janeiro"
d = True

print("a ", a)
print("b ", b)
print("c ", c)
print("d ", d)

print("tipo da var a", type(a))  # tipo inteiro (Números inteiros)
print("tipo da var b", type(b))  # tipo float (Números reais)
print("tipo da var c", type(c))  # tipo string (Alfanumérico)
print("tipo da var d", type(d))  # tipo boolean (True ou False)

a = 20
print("a ", a)
b = "São Paulo"
print("b ", b)

print("tipo da var a", type(a))
print("tipo da var b", type(b))

a = input("informe um número: ")
b = input("informe outro número: ")

print("a: ", a, "- b: ", b)

print("tipo da var a", type(a))
print("tipo da var b", type(b))
c = a + b
print("c: ", c)  # concatenou as strings de a e b
print("tipo da var c", type(c))
d = int(a)
print("d: ", d)
print("tipo da var d", type(d))

a = float(input("informe um número: "))
b = float(input("informe outro número: "))

print("a: ", a, "- b: ", b)

c = a + b
print("c: ", c)
print("tipo da var c", type(c))
