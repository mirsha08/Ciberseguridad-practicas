# Actvidades correspondientes a creación de nuevos ID de empleado
# IDs correspondiente al departamento de ventas
# criterios: todos los IDs deben ser números únicos, divisibles por 5 y comprendido entre 5000 y 5150 (incluidos)
# creación mediante while

# Asigna a la variable de bucle `i` un valor inicial de 5000

i = 5000
id_ventas =[]

# Bucle while que genera ID de empleados únicos para el departamento de ventas iterando a través de los números
# y muestra cada ID creado

while i<=5150:
    id_ventas.append(i)
    i += 5

print("Lista de usarios creados", id_list)

# Incorporar un mensaje que muestre "Solo quedan 10 ID de empleado válidos." como una alerta útil una vez que la variable de bucle alcance 5100.
# Bucle while que genera ID de empleados únicos para el departamento de ventas iterando a través de los números
# y muestra cada ID creado
# Este bucle muestra “Solo quedan 10 ID de empleado válidos” una vez que `i` alcanza 5100

while i<=5150:
    print(i)
    if i ==5100:
      print("ALERT!, solo quedan 10 ID de empleados válidos."
      # break # si queremos detener aquí y asignar manual
    i += 5
