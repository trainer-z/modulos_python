#Programa para inscripcion de cursos, validar edades de los participantes, hacer calculos de costos 
#Y si la persona va a tener descuentos

#El primero es la carpeta, el segundo el archivo
from validaciones.validaciones import validar_nombre, validar_edad
from matematicas.calculos import calcular_costo

print("===Matricula del curso===")

nombre=input("Ingresa tu nombre: ")
edad=int(input("Ingresa tu edad: "))
#horas=int(input("Cuantas horas dura el curso: "))

##Validar el nombre de la persona, que este correcto
if not validar_nombre(nombre):
    print("Error: el nombre NO puede estar vacio")
elif not validar_edad(edad):
    print("No puedes matricularte, o eres muy joven o ya eres una momia")
else:
    valor_hora=int(input("Introduce el valor por hora del curso: "))
    horas=int(input("Introduce la cantidad de horas del curso: "))
    costo=calcular_costo(horas,valor_hora)
    print(f"Bienvenido sujeto {nombre}")
    print(f"Costo del curso: {costo}")

#Intenten validar las horas del curso, no hayan horas negativas
#Creen una funcion para hacer un descuento del 10% si la persona es mayor a 65 años