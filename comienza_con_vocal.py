"""
Inserta el encabezado aquí y escribe tu código abajo

Determinar si una palabra comienza con una vocal.
    Args:
        Palabra (str): Palabra que se evaluará

    Returns:
        str: Mensaje indicando si la palabra comienza con vocal o no.





"""

# Declaraciones
#CONSTANTE = valor

vocales_ascii = {65, 69, 73, 79, 85,   97, 101, 105, 111, 117, 193, 201, 205, 211, 218, 225, 233, 237, 243, 250, 196, 203, 207, 214, 220,
    228, 235, 239, 246, 252
 }


# Entradas
#Palabra= str(input("Escríbe tu palabra"))

Palabra= str(input("Escríbe tu palabra: "))
vocalornot= Palabra[0]
mensajesivocal= (("'")+(Palabra)+("'")+(" comienza con vocal"))
mensajesinvocal= (("'")+(Palabra)+("'")+(" no comienza con vocal"))
ordvocal= ord(vocalornot)
# Proceso
if ordvocal in vocales_ascii:
    salida=mensajesivocal
else:
    salida=mensajesinvocal

print(salida)

# Salidas

