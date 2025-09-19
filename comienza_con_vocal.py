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
Palabra= str(input("Escríbe tu palabra: "))
vocalornot= Palabra[0]
mensajesivocal= (("'")+(Palabra)+("'")+(" comienza con vocal"))
mensajesinvocal= (("'")+(Palabra)+("'")+(" no comienza con vocal"))


# Entradas
#Palabra= str(input("Escríbe tu palabra"))


# Proceso
if(vocalornot == 'a' or
    vocalornot == 'e' or
    vocalornot == 'i' or
    vocalornot == 'o' or
    vocalornot == 'u'):
    salida=mensajesivocal
else:
    salida=mensajesinvocal

print(salida)

# Salidas

