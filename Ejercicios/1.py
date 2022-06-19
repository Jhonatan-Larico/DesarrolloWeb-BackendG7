# ejemplo
# Para evitar que en cada impresion se ejecute una nueva linea, se puede agregar el parametro end y este indicara como queremos que actue al finalizar la linea
#for numero in range(5):
#    print(numero, end="")


# EJERCICIO 1
# Escriba el codigo que le pida al usuario ingresar la altura y el ancho de un rectangulo y
# que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****
heigh = int(input("Ingrese la altura: "))
width = int(input('Ingrese el ancho: '))

for i in range (heigh):
    for j in range (width):
        print('*',end="")
    print("")

# EJERCICIO 2
# Escribir el codigo que el usuario le ingrese el grosor de un octagono y que lo dibuje
# Ejemplo:
# Grosor: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****
thickness = int(input('Ingrese el grosor: '))

heigh = thickness + 2*(thickness-1)
row = thickness
space= thickness-1 #3

for i in range(1,heigh+1): #0 - 5 +2*(5-1) = 13
    if(i < thickness):
        print(" "*space,end="")
        for j in range(row):
            print("*",end="")
        row+=2
        space-=1
    if(i >=thickness and i<= (thickness+ thickness-1 )):
        for j in range(row):
            print("*",end="")
        space=0        
    if(i >(thickness+ thickness-1 )):
        row-=2
        space+=1
        print(" "*space,end="")
        for j in range(row):
            print("*",end="")        
    print()

# EJERCICIO 3
# De acuerdo a la altura que nosotros ingresemos, nos tiene que dibujar el triangulo
# invertido
# Ejemplo
# Altura: 4
# ****
# ***
# **
# *
heigh = int(input("Ingrese la altura: "))
row = heigh

for i in range(1,heigh+1):
    for j in range(1,row+1):
        print("*",end="")
    row-=1    
    print()

# EJERCICIO 4
# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 12
number = int(input("Ingrese un número: "))
result = number
series =[]
series.append(number)

while result != 1:
    if(result%2==0):
        result = result // 2
        series.append(result)
    else:
        result = result*3 + 1
        series.append(result)

print(series)

# EJERCICIO 5
# si el texto de ingreso es:
texto = "hola alumnos buenas noches ya se viene el break"
# entonces el texto resultado debera ser:
#resultado_final = ["Hola", "Alumnos", "Buenas", "Noches", "Ya", "Se"]
# Hacer el codigo para ello

text = texto.split(" ")

for i in range(len(text)):
    text[i]= text[i].capitalize()

print(text)

# EJERCICIO 6
# ingresar numeros hasta que ese numero sea adivinado
numero_adivinar = 2
# 5 => 'el numero es mayor que ese'
# 13 => 'el numero es menor que ese'
# 10 => 'felicidades adivinaste el numero'
n=0

while n!= numero_adivinar:
    n = int((input("Ingrese un número: ")))
    if(n < numero_adivinar):
        print("El número es mayor que ese")
    if(n > numero_adivinar ):
        print("El número es menor que ese") 
    if(n == numero_adivinar):
        print("Felicidades adivinastes el numero")

# EJERCICIO 7
# dado los siguientes numeros:
numeros = [1, 2, 5, 9, 12, 15, 17, 19, 21, 39, 45]
# indicar cuantos de ellos son multiplos de 3 y de 5 , ademas si hay un multiplo de 3 y de 5 no contabilizarlos
# multiplos de 3: 3 , multiplos de 5: 1

mult_3=0
mult_5=0

for n in numeros:
    if n % 3 == 0 and n % 5 == 0:
        continue
    if n % 3 == 0:
        mult_3 += 1
        print("Mult 3",n)
    if n % 5 == 0:
        mult_5 += 1
        print("Mult 5",n)


print("Multiplos de 3: ",mult_3)
print("Multiplos de 5: ",mult_5)
