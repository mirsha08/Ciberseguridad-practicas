Wireshark es un analizador de protocolos de red de código abierto. Utiliza una interfaz gráfica de usuario (GUI), lo que facilita la visualización de las comunicaciones de red con fines de análisis de paquetes. 
Wireshark permite personalizar los filtros.

**Filtros de visualización**
Wireshark permite usar filtros a archivos de captura de paquetes. 
Se pueden filtrar paquetes en función de protocolos, direcc IP, puertos o cualquier propiedad encontrada en un paquete.

**Operadores de comparación**
Se pueden usar operadores tanto en abreviaturas como en simbolos, ej: ip.srec==8.8.8.8

**Operador contains**
Se utiliza para filtrar paquetes que contienen una coincidencia EXACTA de una cadena de texto, ej: http contains "login"

**Operador matches**
Se utiliza para filtrar paquetes en la expresión regular (regex) que se especifica. (expresión regular es un patrón)

**Barra de herramientas de filtrado**
Se pueden aplicar los filtros en la barra de herramientas

## EJEMPLOS DE FILTRADO
* Por protocolos, (dns, http, ftp, ssh, arp, telnet, icmp..)
* Dirección IP.  
  -que contienen una direcc ip--> ip.addr==127.168.0.1  
  -que se originan desde una direcc ip --> ip.src==8.8.8.8  
  -filtrar por ip de destino --> ip.dst==268.251.2.62  
* Direcc MAC, --> eth.addr==00:70:f4:23:15:c5
* Por Puertos, udp.port==53 or tcp.port == 25
* Seguir flujos, se permite filtrar paquetes específicos para un protocolo y ver flujos.

  //más info en  https://www.wireshark.org/docs/wsug_html/
