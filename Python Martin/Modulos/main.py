# 1. Ejemplo importacion modulo nativo de Python --> Matematicas

# import math

# 2. renombrar los imports que traemos

import math as m

# 3 Importar algo especifico 
from math import factorial #as miCalculo 

# 4.  Importacion de funciones por separado de un modulo

from funciones.saludos import saludo_basico, saludo_formal


#help('modules') 
# from funciones import *

saludo_basico('Hugo')
saludo_formal('Hugo')

print(f' El factorial de 3 es; {math.factorial(3)}')