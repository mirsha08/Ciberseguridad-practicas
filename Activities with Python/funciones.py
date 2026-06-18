# Función para control de usuarios autorizados
# objetivo: estructurar los datos de usuarios para trabajar con ellos de distintas maneras. 

# Paso1, convetir en una lista de usuarios autorizados. para poder trabajar con la lista para añadir o eliminar usuarios
# username_list es una lista de usuarios autorizados
# Paso2, crear un bucle en la función que itere a través de los eltos de la lista y muestre cada elemento.

# Definir una función llamada 'list_to_string()'

def list_to_string():
  # almacen la lista de nombre de usuarios autorizados en la variable username_list
  username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]
  # bucle for que itere a través de la los elementos de username_list y muestre cada elemento
  for i in username_list:
    print(i)
# LLamada a la función
list_to_string()

### CONCATENACIÓN ###
# Usar la concatenación para combinar los nombres de usuario de username_list y almacenar el resultado en sum_variable
# Paso3. en cada paso del bucle se agrega cada elto a sum_variable y muestra en pantalla el valor de sum_variable al final

def list_to_string():
  # almacen la lista de nombre de usuarios autorizados en la variable username_list
  username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]
  sum_variable =""
  # bucle for que itere a través de la los elementos de username_list y muestre cada elemento
  for i in username_list:
    sum_variable = sum_variable + i + ", "
    print("añadido", i, "Resultado: ", sum_variable)
# LLamada a la función
list_to_string()
