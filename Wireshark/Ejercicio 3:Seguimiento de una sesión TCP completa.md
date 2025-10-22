# Ejercicios para Wireshark
Software de captura de paquetes.
La captura de paquetes completos es el tipo de captura que obtiene los datos más detallados de la red. 
La captura completa de paquetes contiene todo el material de las conversaciones, como los mensajes de texto o correo electrónico, el HTML de las páginas web y los archivos que ingresan o salen de la red. 
El contenido que se extrae de las capturas de paquetes completos puede recuperarse y analizarse en busca de malware o comportamiento del usuario que viole las políticas de la empresa y de seguridad. 
Ejercicios básicos realizadas con Wireshark, objetivo: captura y análisis de tráfico de red.

---

## Ejercicio 3: Seguimiento de una sesión TCP completa (3-way handshake)

### Objetivo
Capturar y analizar el proceso de establecimiento de una conexión TCP entre tu equipo y un servidor remoto.

### Herramientas
- Wireshark
- Npap (entorno Windows)
- Navegador web o terminal ('curl', 'ping'

### Pasos realizados

1. Abrir **Wireshark** -->Seleccionar interfaz de red activa (ej:`wlan0`).
2. Aplicar filtro tcp
3. Iniciar captura --> acceder a una página web para generar tráfico.
4. Detener la captura tras unos segundos.
5. Analizar los paquetes capturados:
   

###  Observaciones
Busca tres paquetes consecutivos entre tu IP y la del servidor:
  -**SYN** → Tu equipo inicia la conexión.
  -**SYN-ACK** → El servidor responde aceptando la conexión.
  -**ACK** → Tu equipo confirma y se establece la sesión.

Haz clic derecho en el primer paquete SYN → Follow > TCP Stream para ver toda la conversación.

###  Observaciones sobre el ejercicio
- El handshake se completó en menos de 0.1 segundos.
- La IP del servidor fue identificada correctamente. 
- El puerto destino fue el 443 (HTTPS).
- El seguimiento de la conversación TCP mostró el intercambio cifrado posterior.

---

##  Próximos ejercicios sugeridos
- Seguimiento de una sesión TCP completa (3-way handshake).
- Análisis de tráfico HTTPS y comparación con HTTP.
