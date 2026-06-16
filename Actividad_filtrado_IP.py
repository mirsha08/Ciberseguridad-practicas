# Actvidades correspondientes a revisión de seguridad de IP
# Se desarrolla en bucle for donde se coteja que cada una de las conexiones se realiza desde una ip permitda
# En caso de error se debe dar parte de esa ip y guardarla en una variable para futuros chekeos



# Asigna `allow_list` a una lista de direcciones IP a las que se les permite iniciar sesión

allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", 
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]

# Asigna `ip_addresses` a una lista de direcciones IP desde las que los usuarios han intentado iniciar sesión

ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]

# Asignamos lista vacia para almacenar las IP dudosas para futuras revisiones
ip_alert = []

# Para cada dirección IP de la lista de direcciones IP desde las que los usuarios han intentado iniciar sesión, 
# Si está entre las direcciones permitidas, muestra “Se permite la dirección IP”
# De lo contrario, muestra “No se permite la dirección IP”

for i in ip_addresses:
    if i in allow_list:
        print("\033[32m OK\033[39m: la ip ",i ," está permitida")
    else:         
        print("\033[31m ALERTA\033[39m: la IP", i," no está permitida")
        ip_alert.append(i)

print("\n IP enviadas para revision", ip_alert)
        
