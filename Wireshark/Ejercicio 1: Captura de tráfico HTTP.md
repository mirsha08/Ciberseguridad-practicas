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

## Ejercicio 1: Captura de tráfico HTTP

### Objetivo
Capturar tráfico HTTP generado al acceder a una página web y analizar los paquetes transmitidos.
Como el trafico http está siendo reemplazado por cifrado, usamos la web http://neverssl.com para ver http sin cifrar en el ejercicio.
Ejercicios realizados en entorno Kali Linux y windows..

### Herramientas
- Wireshark
- Npap (entorno Windows)
- Navegador web

### Pasos realizados

1. Abrir **Wireshark** -->Seleccionar interfaz de red activa (ej:`wlan0`).
2. Aplicar filtro HTTP
3. Iniciar captura --> acceder a http://neverssl.com desde el navegador.
4. Detener la captura tras unos segundos (F5 para recargar la página y generar tráfico).
5. Analizar los paquetes capturados:
   - Se puede identificar la solicitud `GET` al servidor.
   - Observamos la respuesta `HTTP/1.1 200 OK`.
   - Revisar los encabezados y el contenido HTML.

###  Observaciones
- El tráfico HTTP no está cifrado, por lo que se puede ver el contenido de las páginas y los datos enviados.
- Es posible identificar el User-Agent del navegador y la IP del servidor remoto.

###  Archivos adjuntos
-Se puede realizar una captura de pantalla en formato pcanpg.
Exportar parte de la captura (opcional) Si quieres guardar solo los paquetes HTTP:
   Ve a Archivo > Export Specified Packets
   Marca “Displayed” (para exportar solo lo filtrado)
   Guarda como http-only.pcapng

### Analizar paquete HTTP
clic en una línea que diga GET / o HTTP/1.1 200 OK. 
Panel superior: muestra el resumen del paquete.
Panel medio: despliega detalles por capas (Ethernet, IP, TCP, HTTP).
Panel inferior: muestra el contenido hexadecimal y ASCII.

Busca:
Método HTTP (GET, POST)
Encabezados como Host, User-Agent, Accept
Respuesta del servidor (200 OK, Content-Type, etc.)

### Seguir una conversación TCP
Clic derecho en un paquete HTTP → Follow > TCP Stream. 
Esto te mostrará toda la conversación entre cliente y servidor.
---

##  Próximos ejercicios sugeridos

- Captura de tráfico DNS y análisis de resolución de nombres.
- Seguimiento de una sesión TCP completa (3-way handshake).
- Análisis de tráfico HTTPS y comparación con HTTP.
