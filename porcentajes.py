#encoding: UTF-8
# Autor: María Angélica Hernandez Parada, A01169796
# Descripcion: El programa le pregunta al usuario el nmero de hombres y el nmero de mujeres inscritos.   
# A partir de aqui escribe tu programa

hombres= int(input("Dime cuantos hombres hay en total"))
mujeres= int(input("Dime cuantas mujeres hay en total"))
total=hombres+mujeres
 
porcentaje_mujeres=(mujeres*100)/total
porcentaje_hombres=(hombres*100)/total
 
print ("Total inscritos", total)
print ("% de mujeres", porcentaje_mujeres)
print ("% de hombres", porcentaje_hombres)