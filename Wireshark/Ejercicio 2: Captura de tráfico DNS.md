# Ejercicios para Wireshark
Software de captura de paquetes.
La captura de paquetes completos es el tipo de captura que obtiene los datos más detallados de la red. 
La captura completa de paquetes contiene todo el material de las conversaciones, como los mensajes de texto o correo electrónico, el HTML de las páginas web y los archivos que ingresan o salen de la red. 
El contenido que se extrae de las capturas de paquetes completos puede recuperarse y analizarse en busca de malware o comportamiento del usuario que viole las políticas de la empresa y de seguridad. 
Todo esto lo vemos con Registros de redes.
La herramienta de línea de comando tcpdump es un analizador de paquetes. 
Puede mostrar capturas de paquetes en tiempo real o escribir capturas de paquetes en un archivo. 
Las capturas incluyen protocolos de paquetes detallados y datos de contenido que se pueden ver con Wireshark

Ejercicios básicos realizadas con Wireshark, objetivo: captura y análisis de tráfico de red.

---

## Ejercicio 2: Captura de tráfico DNS

### Objetivo
Capturar y analizar solicitudes y respuestas DNS al acceder a una página web, identificando cómo se traduce un nombre de dominio en una dirección IP.

### Herramientas
- Wireshark
- Npap (entorno Windows)
- Navegador web

### Pasos realizados

1. Abrir **Wireshark** -->Seleccionar interfaz de red activa (ej:`wlan0`).
2. Aplicar filtro DNS
3. Iniciar captura --> acceder a una página web que no se haya visitado recientemente. (http://example.org) para forzar una nueva consulta DNS.
4. Detener la captura tras unos segundos.
5. Analizar los paquetes capturados:
   - Standard query--> solicitud del cliente al servidor DNS.
   - Standard query response --> respuesta con la IP correspondiente.

###  Observaciones
-Nombre consultado: por ejemplo, example.org.
-Tipo de registro: normalmente A (IPv4) o AAAA (IPv6).
-Dirección IP devuelta.
-Tiempo entre solicitud y respuesta.

###  Archivos adjuntos
-Se puede realizar una captura de pantalla en formato pcanpg.


---

##  Próximos ejercicios sugeridos
- Seguimiento de una sesión TCP completa (3-way handshake).
- Análisis de tráfico HTTPS y comparación con HTTP.
