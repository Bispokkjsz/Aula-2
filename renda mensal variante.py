# escreva um programa em python que receba as seguintes informacoes do usuario:
# renda mensal (um numero float)
# score de credito (um numero inteiro de 0 a 1000)
# possui bens como garantia? (use uma str de "sim" ou "nao")
# tem historico de inadiplencia? (uma str de "sim" ou "nao")
#
# o emprestimo sera APROVADO se o cliente cumprir uma das duas regras a seguir:
# Regra numero 1:
# ter renda mensal maior ou igual a 3.000,00 reais 
# e score de credito maior ou igua a 600 
# e NAO ter historico de indiplencia
# Regra numero 2:
# independentemente da renda ou score,
# se o cliente NAO tiver historico de indiplencia
# E possuir bens como garantia, ele tambem é APROVADO.
#
#
# Se o cliente nao se encaixar em nenhuma dessas regras, 
# o emprestimo sera REPROVADO

renda_mensal = float(input("Qual a sua renda mensal? "))
score_credito = int(input("Qual o seu score? "))
bens_materias = str(input("Tem bens materias? "))
historico_dividas = str(input("Possui historico de indiplencia? "))

if renda_mensal >= 3000 and score_credito >= 600 and historico_dividas == "nao":
    print("Aprovado!")
elif historico_dividas == "nao" and bens_materias == "sim":
    print("Aprovado!")
else:
    print("Reprovado!")