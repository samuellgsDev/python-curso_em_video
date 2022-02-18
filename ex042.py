# Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
#
# Redo CHALLENGE 35 of triangles,
#  adding the feature to show what type of triangle will be formed:
# – EQUILATERAL: all sides equal
# – ISOSCELES: two equal sides, one different
# – SCALENO: all different sides
#

line1 = float(input('Enter the first side: '))
line2 = float(input('Enter the second side: '))
line3 = float(input('Enter the third side: '))
if line1 < line2 + line3 and line2 < line1 + line3 and line3 < line1 + line2:
    print('Triangle can be formed!')
    if line1 == line2 == line3:
        print('EQUILATERAL')
    elif line1 == line2 or line1 == line3 or line2 == line3:
        print('ISOSCELES')
    else:
        print('SCALENO')
