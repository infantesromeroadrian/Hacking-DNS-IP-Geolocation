# Proyecto: DNS to IP Geolocation

## Descripción
Este proyecto combina las capacidades de resolución DNS con geolocalización de direcciones IP para proporcionar información completa sobre dominios y su ubicación geográfica. Consta de tres componentes principales:

1. **DNS Resolver**: Obtiene las direcciones IP asociadas a un dominio utilizando registros DNS.
2. **IP Geolocation**: Proporciona detalles geográficos de una dirección IP utilizando la API de `ipinfo`.
3. **Main Script**: Integra las funcionalidades anteriores en un flujo unificado que permite consultar un dominio y obtener información completa sobre él.

## Estructura del Proyecto
El proyecto está dividido en tres archivos principales:

1. `dns_resolver.py`
  * **Funcionalidad**: Resuelve las direcciones IP asociadas al registro A de un dominio.
  * **Input**: Nombre del dominio (por ejemplo, `example.com`).
  * **Output**: Lista de direcciones IP asociadas.

2. `ip_geolocation.py` 
  * **Funcionalidad**: Obtiene información de geolocalización para una dirección IP.
  * **Input**: Dirección IP.
  * **Output**: Detalles geográficos (país, región, ciudad, coordenadas, ISP, etc.) y un mapa interactivo generado con Folium.

3. `main.py`
  * **Funcionalidad**: Integra las capacidades de resolución DNS y geolocalización IP.
  * **Flujo**:
     1. Solicita un dominio al usuario.
     2. Resuelve el dominio a una dirección IP.
     3. Obtiene la información de geolocalización para la IP resuelta.
     4. Genera un mapa interactivo con la ubicación de la IP.

## Requisitos
* **Python**: >= 3.10
* **Dependencias**:
  * `dnspython`
  * `ipinfo`
  * `python-dotenv`
  * `folium`

## Instalación
1. Clona este repositorio:
```bash
git clone <URL-del-repositorio>
cd <directorio-del-proyecto>

Instala las dependencias con Poetry:

bashCopypoetry install

Crea un archivo .env para almacenar el token de acceso de ipinfo:

envCopyIPINFO_API_KEY=tu_token_aqui
Uso

Activa el entorno virtual:

bashCopypoetry shell

Ejecuta el script principal:

bashCopypython src/main.py

Introduce el dominio que deseas consultar cuando se te solicite.

Ejemplo
Entrada:
bashCopyIntroduce el nombre del dominio (e.g., example.com): google.com
Salida:
Copy=== Direcciones IP del dominio ===
8.8.8.8
8.8.4.4

=== Detalles de la IP ===
País: Estados Unidos
Región: California
Ciudad: Mountain View
Latitude: 37.386
Longitude: -122.083
ISP: Google LLC

Mapa guardado en: map.html
Autor
Este proyecto fue desarrollado para demostrar la combinación de resolución DNS y geolocalización de IP con Python.
Licencia
Este proyecto está licenciado bajo la MIT License.