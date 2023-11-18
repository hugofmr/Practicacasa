# comenzamos con las condiciones 
# IF - ELIF(opcional) - ELSE(opcional) 

edad = 40

if (edad < 18):
    print('menor de edad')

elif (edad >= 18 and edad < 40) :
    print('Adulto Joven')

elif (edad >= 40 and edad < 70) :
    print('Adulto')

else :
    print('Persona mayor')