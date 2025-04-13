# IMPORTS NECESARIOS
from functools import reduce

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.
def contar_frecuencias(cadena):
    frecuencias = {}
    for letra in cadena:
        if letra.isalpha():  # Verifica si es una letra
            letra = letra.lower()  # Convierte todo a minúscula para contar sin distinción de mayúsculas/minúsculas
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias


# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
def duplicar_por_valor(numeros):
    duplicados = list(map(lambda x : 2*x, numeros))
    return duplicados


# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
# devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
def detectar_palabra_objetivo(palabras, objetivo):
    return list(filter(lambda palabra: objetivo in palabra, palabras))


# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
def calcular_diferencia(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))


# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
# defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
# una tupla que contenga la media y el estado.
def calcular_media_y_estado(numeros, nota_aprobado=5):
    if len(numeros) == 0:
        return (0, "suspenso")
    
    media = sum(numeros) / len(numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)


# 6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)


# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
def covertir_tuplas_a_strings(tuplas):
    return list(map(lambda tupla: str(tupla), tuplas))


# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.
def division(numerador, denominador):
    try:
        resultado = numerador/denominador
    except TypeError:
        print("No se pueden dividir valores no numéricos")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    else:
        print("La division fue exitosa. El resultado es:", resultado)


# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
# excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
def mascotas_permitidas(mascotas):
    mascotas_prohibidas = ["mapache", "tigre", "serpiente pitón", "cocodrilo", "oso"]
    return list(filter(lambda mascota: mascota.lower() not in mascotas_prohibidas, mascotas))


# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada y maneja el error adecuadamente.
def calcular_promedio(numeros):
    try: 
        promedio = sum(numeros) / len(numeros)
    except ZeroDivisionError:
        print("La lista está vacía, no se puede calcular el promedio.")
    else:
        print("El promedio es:", promedio)


# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.
def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
    except ValueError:
        print("Error: Se ha introducido un valor no numerico")
    else:
        if edad<0 or edad>120:
            print("No se admiten valores que no esten entre 0 y 120")
        else:
            print("Valor aceptado. Tu edad es de", edad, "años")


# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))


# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
# mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()
def generar_tuplas_mayus_minus(caracteres):
    caracteres = caracteres.lower()  # Convierte todo a minúscula para evitar duplicados
    caracteres_unicos = set(caracteres)  # Elimina duplicados
    return list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))


# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
# función filter()
def filtrar_por_letra(palabras, letra):
    letra = letra.lower()  # Convierte la letra a minúscula para comparación
    palabras = list(map(lambda palabra: palabra.lower(), palabras))  # Convierte todas las palabras a minúscula
    return list(filter(lambda palabra: palabra.startswith(letra), palabras))


# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
def sumar_tres(numeros):
    return list(map(lambda x: x + 3, numeros))


# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter()
def palabras_mas_largas(cadena, n):
    palabras = cadena.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))


# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()
def encadenar_digitos(digitos):
    return int(reduce(lambda x, y: str(x) + str(y), digitos))
    

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
# 90. Usa la función filter().
def filtrar_estudiantes(estudiantes):
    return list(filter(lambda estudiante: estudiante['calificacion'] >= 90, estudiantes))

# Ejemplo de uso:
print(filtrar_estudiantes([{'nombre': 'Juan', 'edad': 20, 'calificacion': 95},
                        {'nombre': 'Ana', 'edad': 22, 'calificacion': 85},
                        {'nombre': 'Luis', 'edad': 21, 'calificacion': 90},
                        {'nombre': 'Maria', 'edad': 23, 'calificacion': 88}]))


# 19. Escribe una función que tome una lista de números y devuelva una lista con los números pares. Usa la función filter()
def filtrar_pares(numeros):
    return list(filter(lambda x: x % 2 == 0, numeros))


# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
# filter()
def filtrar_enteros(lista):
    return list(filter(lambda x: isinstance(x, int), lista))


# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda.
def calcular_cubo(numero):
    cubo = lambda x: x ** 3
    return cubo(numero)


# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() .
def producto_total(lista):
    return reduce(lambda x, y: x * y, lista)


# 23. Concatena una lista de palabras. Usa la función reduce()
def concatenar_palabras(palabras): 
    palabras = list(map(str, palabras)) # Convertir todo a strings:
    return reduce(lambda x, y: x + y, palabras)


# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce()
def diferencia_total(lista):
    return reduce(lambda x, y: x - y, lista)


# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
def contar_caracteres(cadena):
    return len(cadena)


# 26. Crea una función que calcule el resto de la división entre dos números dados.
def calcular_resto(x, y):
    resto = lambda a, b: a % b
    return resto(x, y)


# 27. Crea una función que calcule el promedio de una lista de números.
def calcular_promedio_lista(lista):
    return sum(lista) / len(lista) if len(lista) > 0 else 0


# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None


# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.
def enmascarar_variable(variable):
    variable_str = str(variable)
    if len(variable_str) <= 4:
        return variable_str
    else:
        return '#' * (len(variable_str) - 4) + variable_str[-4:]
    

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.
def son_anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)


# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.
def buscar_nombre_en_lista():
    nombres = input("Introduce una lista de nombres separados por comas: ").split(",")
    nombres = [nombre.strip().lower() for nombre in nombres] # convertir a minúsculas y eliminar espacios en blanco
    nombre_a_buscar = input("Introduce el nombre a buscar: ")
    nombre_a_buscar = nombre_a_buscar.strip().lower()  # convertir a minúscula y eliminar espacios en blanco
    
    if nombre_a_buscar in nombres:
        print(f"El nombre '{nombre_a_buscar}' fue encontrado en la lista.")
    else:
        raise ValueError(f"El nombre '{nombre_a_buscar}' no se encuentra en la lista.")
    

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.
def buscar_empleado(nombre_completo, empleados):
    for empleado in empleados:
        if empleado['nombre'] == nombre_completo:
            return empleado['puesto']
    return f"{nombre_completo} no trabaja aquí."

# Ejemplo de uso:
print(buscar_empleado("Juan Perez", [{'nombre': 'Juan Perez', 'puesto': 'Gerente'},
                        {'nombre': 'Ana Gomez', 'puesto': 'Desarrolladora'},
                        {'nombre': 'Luis Martinez', 'puesto': 'Diseñador'}]))


# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
def sumar_listas(lista1, lista2):
    return list(map(lambda x, y: x + y, lista1, lista2))


# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
# manipular la estructura del árbol.
class Arbol:
    def __init__(self, tronco, ramas):
        self.tronco = tronco
        self.ramas = ramas

    def crecer_tronco(self):
        self.tronco = self.tronco + 1

    def nueva_rama(self):
        self.ramas.append(1)
    
    def crecer_ramas(self):
        self.ramas = list(map(lambda x: x+1, self.ramas))

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
           self.ramas.pop(posicion)

    def info(self):
        print("Longitud del tronco:", self.tronco)
        print("Número de ramas:", len(self.ramas))
        print("Longitudes de las ramas:")
        for i, rama in enumerate(self.ramas):
            print(f"  Rama {i + 1}: Longitud {rama}")

# CASO DE USO:

# 1. Crear un arbol con tronco le longitud 0 y sin ramas:
arbol = Arbol(0,[])

# 2. Hacer crecer el tronco del árbol una unidad:
arbol.crecer_tronco()

# 3. Añadir una nueva rama al árbol (es de longitud 1).
arbol.nueva_rama()

# 4. Hacer crecer todas las ramas del árbol una unidad.
arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas al árbol.
for i in range(2):
    arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2.
arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol.
arbol.info()



# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes para retirar.")

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

    def transferir_dinero(self, usuario_remitente, cantidad):
        try:
            if usuario_remitente.saldo < cantidad:
                print("AVISO: Saldo insuficiente en la cuenta del usuario remitente")
            else:
                usuario_remitente.retirar_dinero(cantidad)
                self.agregar_dinero(cantidad)
                print("Transferencia realizada con exito.")
                print("Saldo actualizado del usuario remitente:", usuario_remitente.saldo)
                print("Saldo actualizado del usuario destinatario", self.saldo)
        
        except AttributeError:
            print("ERROR: No se ha podido identificar al usuario remitente")

# CASO DE USO:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True) 

# 2. Agregar 20 unidades de saldo de "Bob".
bob.agregar_dinero(20)

# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
alicia.transferir_dinero(bob, 80)

# 4. Retirar 50 unidades de saldo a "Alicia".
alicia.retirar_dinero(50)


# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
# reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
# de la función procesar_texto .
# 1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
# que devolver un diccionario.
def contar_palabras(texto):
    palabras = texto.lower().split()
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

# 2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
# que devolver el texto con el remplazo de palabras.
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    palabras = texto.split()
    palabras = [palabra_nueva if palabra.lower() == palabra_original.lower() else palabra for palabra in palabras]
    return ' '.join(palabras)

# 3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
# eliminada.
def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    palabras = list(filter(lambda x: x.lower() != palabra.lower(), palabras)) 
    return ' '.join(palabras)  # Une las palabras restantes en un solo string

# 4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
# número de argumentos variable según la opción indicada.
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Se requieren exactamente dos argumentos para reemplazar.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Se requiere exactamente un argumento para eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Debe ser 'contar', 'reemplazar' o 'eliminar'.")

    
# EJEMPLO DE USOS:
texto = "Hola mundo, hola a todos. Hola a todos los que están en el mundo."
print(procesar_texto(texto, "contar"))  # Contar palabras
print(procesar_texto(texto, "reemplazar", "Hola", "Adios"))  # Reemplazar palabras
print(procesar_texto(texto, "eliminar", "Hola"))  # Eliminar palabra
print(procesar_texto(procesar_texto(texto, "eliminar", "Hola"), "contar"))  # Contar palabras después de eliminar


# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
def momento_del_dia():
    try:
        hora_usuario = int(input("Introduce la hora actual (0-23): "))
        if hora_usuario < 0 or hora_usuario > 23:
            print("La hora debe estar entre 0 y 23.")
        elif 6 <= hora_usuario < 12:
            print("Es de día (mañana).")
        elif 12 <= hora_usuario < 20:
            print("Es por la tarde.")
        else:
            print("Es de noche.")
    except ValueError:
        print("Error: El valor introducido no es numérico.")


# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# Las reglas de calificación son:
# - 0 - 69 insuficiente
# - 70 - 79 bien
# - 80 - 89 muy bien
# - 90 - 100 excelente
def calificacion_texto(calificacion):
    try:
        if 0 <= calificacion < 70:
            print("Insuficiente")
        elif 70 <= calificacion < 80:
            print("Bien")
        elif 80 <= calificacion < 90:
            print("Muy bien")
        elif 90 <= calificacion <= 100:
            print("Excelente")
        else:
            print("Calificación fuera de rango")
    except TypeError:
        print("Error: El valor introducido no es numérico.")


# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
# "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).
def calcular_area(**kwargs):
    '''
    Calcula el área de una figura geométrica.
    Parámetros esperados:
        - figura: una cadena que puede ser 'rectangulo', 'triangulo' o 'circulo'.
        - datos: una tupla con los valores necesarios:
            - rectangulo: (base, altura)
            - triangulo: (base, altura)
            - circulo: (radio,)
    Devuelve el área correspondiente o None si la figura no es válida.
    '''
    figura = kwargs.get('figura')
    datos = kwargs.get('datos')

    if figura == 'rectangulo':
        base, altura = datos
        area = base * altura

    elif figura == 'triangulo':
        base, altura = datos
        area = (base * altura) / 2

    elif figura == 'circulo':
        (radio,) = datos  
        pi = 3.1416
        area = pi * radio ** 2

    else:
        print("ERROR: No se ha reconocido la figura", figura)
        return None

    return area


# 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
# siguiente:
# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
# a cero). Por ejemplo, descuento de 15€.
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
# programa de Python.
def calcular_precio_final():
    try:
        precio_original = float(input("Introduce el precio original del artículo: "))
        tiene_cupon = input("¿Tienes un cupón de descuento? (si/no): ").strip().lower()

        if tiene_cupon == "si":
            valor_cupon = float(input("Introduce el valor del cupón de descuento: "))
            if valor_cupon > 0:
                if valor_cupon > precio_original:
                    print("El valor del cupon es mayor que el precio. El artículo le saldra gratis.")
                    precio_final = 0
                else:
                    precio_final = precio_original - valor_cupon
            else:
                print("El valor del cupón debe ser mayor que cero.")
                precio_final = precio_original

        elif tiene_cupon == "no":
            precio_final = precio_original

        else:
            print("Respuesta no válida. Se aplicará el precio original.")
            precio_final = precio_original

        print(f"El precio final de la compra es: {precio_final:.2f}€")
    except ValueError:
        print("Error: El valor introducido no es numérico.")