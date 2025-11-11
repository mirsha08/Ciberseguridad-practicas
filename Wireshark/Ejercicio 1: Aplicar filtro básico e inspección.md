# ANALISIS DE PAQUETES CON WIRESHARK_ practicas  

Archivo de captura de paquetes *.pcap
descripción general de las columnas de propiedades clave que se muestran para cada paquete:
•	No.: el número de índice del paquete en este archivo de captura de paquetes  
•	Time: la marca de tiempo del paquete  
•	Source: la dirección IP de origen  
•	Destination: la dirección IP de destino  
•	Protocol: el protocolo contenido en el paquete  
•	Length: la longitud total del paquete  
•	Info: cierta información sobre los datos en el paquete (la carga útil) según la interpretación de Wireshark  

## Filtros
### Filtro para tráfico asociado con una dirección IP específica: 
**ip.addr==142.252.1.139**
Muestra solo paquetes que contienen la direcc IP de origen o destino que coincide.
Muestra también los datos del paquete sin procesar en formato texto y hexadecimal y ASCII.

Frame --> Info sobre todo del paquete de datos, detalles del paquete o marco de red general, incluye longitud del marco, hora de llegada del paquete.   
Ethernet II --> detalles del paquete a nivel Ehernet, incluye direcc MAC de origen y destino, tipo de protocolo interno
Internet Protocol Version 4 -->datos del protocolo de internet (IP) contenidos en el paquete.  
  subarbol Transmission control Protocol --> Flags -->vista detallada de las marcas TCP

### Filtro según origen o destino
Filtro de paquetes de ip de origen **ip.src==142.252.1.139**  
Filtro de paquetes de ip de destino **ip.dst==142.252.1.139**  
Filtro tráfico hacia o desde una direcc MAC **eth.addr==12:fc:15:e0:02:42** esta direcc mac aparece en el subarbol EthernetII

Dentro de Internet Protocol Version 4 / Time to Live y Protocol (indica el protocolo interno de IP del contenido del paquete)  

### Filtro para paquetes DNS:  
el trafico DNS usa el puerto UDP 53, por lo tanto: **udp.port==53**  
Dentro del paquete Domain Name System (query)/  
  /Queries nos muestra nombre de sitio que consulta en el paquete  
  /Answers incluye el nombre que se consultó y direcc asociadas con ese nombre.

### Filtro para paquetes TCP:  
El tráfico TCP usa el puerto 80: **tcp.port==80**

Podemos ver el Time to Live (Internet Protocol Version 4), el Frame Lenght del paquete (Frame), el Header Lenght y Destination Address (Internet Protocol Version 4)

Para filtrar datos de paquetes TCP que contengan datos de texto específicos:  
**tcp conatins "curl"**  
así filtramos los paquetes que contienen solicitudes web realizadas con el comando "curl" en ese archivo de captura de paquetes.

