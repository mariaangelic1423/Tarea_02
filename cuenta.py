#encoding: UTF-8
# Autor: Mara Anglica Hernandez Parada, A01169796
# Descripcion: El programa le pregunta al usuario el total de la comida  
# A partir de aqui escribe tu programa

subtotal=int(input("Dime el subtotal de tu comida"))
propina=subtotal*0.15
IVA=subtotal*0.16
total=subtotal+propina+IVA

print ("El subtotal es de $", subtotal)
print ("la propina $", propina)
print ("el IVA $", IVA)
print ("junto de un Total de $", total) 