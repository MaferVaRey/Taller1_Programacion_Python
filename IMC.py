# Se pedirán los datos de entrada: peso, estatura y edad.
estatura = float(input('digite su estatura en metros: '))
peso = float(input('digite se peso en kilogramos: '))
edad = int(input('digite du edad: '))

# Se elvaluará el IMC teniendo encuenta su fórmula (peso sobre estatura al cuadrado.
IMC = peso / (estatura**2)

# El programa evaluará si está en una situación de riesgo de salud o no
# en una cadena de if else
# (no pude usar match case porque no pude descargar python 3.10 en mi computador)
if IMC < 22.0 and edad < 45:
    print('La condición de riesgo es baja. IMC: ', IMC, 'Edad ', edad)
elif IMC < 22.0 and edad >= 45:
    print('La condición de riesgo es media. IMC: ', IMC, 'Edad ', edad)
elif IMC >= 22.0 and edad < 45:
    print('La condición de riesgo es media. IMC: ', IMC, 'Edad ', edad)
elif IMC >= 22.0 and edad >= 45:
    print('La condición de riesgo es alta. IMC: ', IMC, 'Edad ', edad)
