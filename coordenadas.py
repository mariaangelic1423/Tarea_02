#encoding: UTF-8
# Autor: Mara Anglica Hernandez Parada, A01169796
# Descripcion: El programa le pregunta al usuario el valor de x y y. 
import math
# A partir de aqui escribe tu programa

x= int(input("Dame el valor de x"))
y= int(input("Dame el valor de y"))

r=((x*x)+(y*y))**0.5
grados1=math.atan(y/x)
grados2=math.degrees(grados1)
print ("r=",r)
print (grados2)