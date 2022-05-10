mi_variable = 12
print(mi_variable)

mi_variable2 = 'dario'
print(mi_variable2)

mi_complejo = 5 + 7j
print(mi_complejo)


mi_numero = input('Ingrese un valor')
print('el valor ingresado fue', mi_numero)
## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

nombre = "Bryan"
print(nombre)
 
# Imprimir el tipo de dato de la constante 8.5
type(8.5)

# Imprimir el tipo de dato de la variable creada en el punto 1
type(nombre)

# Crear una variable que contenga tu nombre
segundonombre = "Alexander"

# Crear una variable que contenga un número complejo
n_complejo = -7 + 8j

# Mostrar el tipo de dato de la variable crada en el punto 5
print(n_complejo)

# Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
pi = 3.1416

# Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
b = "TRUE"
c = True
# la primera variable contine una dato tipo string por lo que solo puede ser impreso o sumado y el segundo es un dato  
# boleano que su valor es encedido o 1 

# Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print("El tipo de dato de la primera variable es", type(b) , "El tipo de dato de la segunda variable es" , type(c) )

# Asignar a una variable, la suma de un número entero y otro decimal
var1 = 5 + 10.2

# Realizar una operación de suma de números complejos
y= 5+8j
z= 8+1j
print(y+z)

# Realizar una operación de suma de un número real y otro complejo
n1= -9
print(n1+y)

# Realizar una operación de multiplicación
print(9*9)

# Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)

# Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
print(27/4)

# De la división anterior solamente mostrar la parte entera
print(int(27/4))
# o print(27//4)

# De la división de 27 entre 4 mostrar solamente el resto
print(27%4)

# Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(6*4+3)

# Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
varx = "Nuevo "
vary = "Chimbote "
print(varx + vary )

# Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print ("2" == 2)

# Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
a = "2"
b = 2
str(2)
print(a == b)

# ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
a = float('3,8')

# Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
va_3 = 3
va_3 -=4
print(va_3)

# Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
# la formula para hallar ese resultado es la siguiente a <<b , a*(2**b)
# añado otro operacion semejante x>>y=x//(2**y)[Floor division]
print(1<<2)

# Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
2 + "2"
float(2) + float ("2")
int(2) + int("2")
str(2) + str("2")

# Realizar una operación válida entre valores de tipo entero y string

vare = 20
snota = "en mi curso de matematica obtuve "
print (snota,vare)

vary = 'este texto se repite '
varz = 3
print(vary * varz + str(varz) + ' veces')

cat = 0
have = " gatos"

print("Tengo " + str(cat) + have)