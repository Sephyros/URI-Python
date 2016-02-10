# URI Online Judge | 1004
# Produto Simples
#
# Adaptado por Neilor Tonin, URI Brasil
# Timelimit: 1
#
# Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à
# variável PROD. A seguir mostre a variável PROD com mensagem correspondente.
#
# Entrada
# O arquivo de entrada contém 2 valores inteiros.
#
# Saída
# Imprima a variável PROD conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade. Não esqueça
# de imprimir o fim de linha após o produto, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
# Exemplos de Entrada 	Exemplos de Saída
#
# 3                       PROD = 27
# 9
#
# -30                     PROD = -300
# 10
#
# 0                       PROD = 0
# 9
#
# Resolvido por Leonardo Vinicius Maciel (aka Sephyros)

V1 = int(input())
V2 = int(input())
PROD = V1 * V2
print("PROD = %d" % PROD)
