# URI Online Judge | 1010
# Cálculo Simples
#
# Adaptado por Neilor Tonin, URI Brasil
# Timelimit: 1
#
# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de
# uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
#
# Entrada
# O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um
# valor com 2 casas decimais.
#
# Saída
# A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos
# e um espaço após o $. O valor deverá ser apresentado com 2 casas após o ponto.
# Exemplos de Entrada 	Exemplos de Saída
#
# 12 1 5.30               VALOR A PAGAR: R$ 15.50
# 16 2 5.10
#
# 13 2 15.30              VALOR A PAGAR: R$ 51.40
# 161 4 5.20
#
# 1 1 15.10               VALOR A PAGAR: R$ 30.20
# 2 1 15.10

VALUES1 = input().split()
VALUES2 = input().split()
P1_CODE = int(VALUES1[0])
P1_QUANTITY = int(VALUES1[1])
P1_VALUE = float(VALUES1[2])
P2_CODE = int(VALUES2[0])
P2_QUANTITY = int(VALUES2[1])
P2_VALUE = float(VALUES2[2])
VALUE_TO_PAY = (P1_QUANTITY * P1_VALUE) + (P2_QUANTITY * P2_VALUE)
print("VALOR A PAGAR: R$ %.2f" % VALUE_TO_PAY)
