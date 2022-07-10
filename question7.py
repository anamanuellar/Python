# A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).

horaBase = 9.375
salarioHoraExtra= horaBase * 1.5
horasTrabalhadas = int(input('Entre com as horas trabalhadas no mês: '))
horasExtras = horasTrabalhadas - 160
totalHorasExtras = horasExtras * salarioHoraExtra
totalSalario = horasTrabalhadas * horaBase
totalMescomExtras = (horasExtras * salarioHoraExtra) + (160 * horaBase)

if (horasTrabalhadas < 160 or horasTrabalhadas == 160):
    print("\nO salario final do vendedor: R$", totalSalario )

if (horasTrabalhadas > 160):
    print("\nO salario final do vendedor: R$", totalMescomExtras)
