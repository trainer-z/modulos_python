##Validar el nombre
def validar_nombre(nombre):
    if len(nombre) > 0:
        return True
    else:
        return False

#edades menores a 10
#edades mayores a 117
def validar_edad(edad):
    if edad>=15 and edad<=117:
        return True
    else:
        return False