# URI Online Judge | 1001
# Extremamente Básico
#
# Adaptado por Neilor Tonin, URI Brasil
# Timelimit: 1
#
# Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B atribuindo o seu
# resultado na variável X. Imprima X conforme exemplo apresentado abaixo. Não apresente mensagem
# alguma além daquilo que está sendo especificado e não esqueça de imprimir o fim de linha após o resultado,
# caso contrário, você receberá "Presentation Error".
#
# Entrada
# A entrada contém 2 valores inteiros.
#
# Saída
# Imprima a variável X conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.
# Exemplos de Entrada     Exemplos de Saída
# 10                      X = 19
# 9
#
# -10                     X = -6
# 4
#
# 15                      X = 8
# -7

# -*- coding: utf-8 -*-

A = int(input())
B = int(input())
x = A + B
print("X = %d" %x)
