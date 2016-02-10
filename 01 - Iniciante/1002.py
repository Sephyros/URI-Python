# URI Online Judge | 1002
# Área do Círculo
#
# Adaptado por Neilor Tonin, URI Brasil
# Timelimit: 1
#
# A fórmula para calcular a área de um círculo é: area = π . raio2. Considerando que para este problema que π = 3.14159:
#
# - Efetue o cálculo da área, elevando o valor de Raio ao quadrado e multiplicando por π.
#
# Entrada
# A entrada contém um valor de ponto flutuante (dupla precisão) no caso a variável raio.
#
# Saída
# Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto
# decimal. Utilize variáveis de dupla precisão (double). Como todos os problemas, não esqueça de imprimir o fim de linha
# após o resultado, caso contrário, você receberá "Presentation Error".
# Exemplos de Entrada 	Exemplos de Saída
# 2.00                    A=12.5664
#
# 100.64                  A=31819.3103
#
# 150.00                  A=70685.7750

pi = 3.14159
raio = float(input())
area = pi * pow(raio, 2)
print("A=%.4f" % area)
