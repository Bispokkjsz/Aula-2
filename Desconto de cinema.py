# escreva um programa em python que pergunte tres informacoes ao usuario
# é estudante (uma str: "Sim" ou "nao")
# dia da semana (uma str: "terça" ou "outro")
# tipo de sala (uma str: "vip" ou "comum")
# 
# o programa de deve exibir: "desconto aplicado!"
# ou "valor Integral"
# regra
# o cliente ganha o desconto se for estudante ou terça feira
# E a sala for comum

estudante = str(input("Voce é um estudante? "))
dia_semana = str(input("Qual o dia da semana? "))
tipo_sala = str(input("Qual o tipo da sala? "))

if estudante == "sim" or dia_semana == "terça":
    if tipo_sala == "comum":
        print("Desconto aplicado!")
    else:
        print("valor integral!")
else:
    print("Valor integral!")