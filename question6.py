# Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor

salarioBase = int(input('Entre com o salário base do vendedor: '))
valorComissao = int(input('Entre com o valor da comissão por carro vendido: '))
totalCarros = int(input('Entre com o total de carros vendidos: '))
totalVendas = int(input('Entre com o total de vendas: '))

total_comissao = totalCarros * valorComissao
total_comissao = total_comissao + ( totalVendas * 5/100 )
total_salario = total_comissao + salarioBase
 
print("\nO salario final do vendedor: R$", total_salario)