dep_inicial = float(input("Informe o depósito inicial: "))
taxa_anual = float(input("Informe a taxa de juros ao ano: "))
valor_final = dep_inicial
taxa_mensal = (taxa_anual / 12) / 100

for i in range(24):
    calculo = valor_final * taxa_mensal
    valor_final += calculo
    print("Mês {0} = R${1:.2f} reais".format(i+1, valor_final))
    
juros_recebidos = valor_final - dep_inicial

print("Total ganho no período: R${0:.2f} reais\nRendendo {1}% ao ano".format(valor_final, taxa_anual))
print("Total em juros recebidos: R${0:.2f} reais".format(juros_recebidos))
print("branch 1")