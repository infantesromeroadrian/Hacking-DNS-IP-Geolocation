import ipinfo
from folium import Map, Marker
import os
import sys

def get_ip_details(ip_addr, access_token):
    """
    Obtiene detalles de geolocalización de una dirección IP utilizando la API de ipinfo.

    Args:
        ip_addr (str): La dirección IP de la cual obtener la información.
        access_token (str): El token de acceso para la API de ipinfo.

    Returns:
        dict: Un diccionario con todos los detalles obtenidos.

    Raises:
        SystemExit: Termina el script si hay un error al obtener los detalles de la IP.
    """
    try:
        handler = ipinfo.getHandler(access_token)
        details = handler.getDetails(ip_addr)
        return details.all
    except Exception as e:
        print(f"Error al obtener los detalles de la IP '{ip_addr}': {e}")
        sys.exit(1)

def draw_map(latitude, longitude, location, filename="map.html"):
    """
    Genera un mapa HTML utilizando la librería Folium.

    Args:
        latitude (float): Latitud del punto a marcar.
        longitude (float): Longitud del punto a marcar.
        location (str): Descripción de la ubicación para el marcador.
        filename (str): Nombre del archivo donde se guardará el mapa.

    Returns:
        str: Ruta absoluta al archivo del mapa generado.
    """
    my_map = Map(location=[latitude, longitude], zoom_start=9)
    Marker([latitude, longitude], popup=location).add_to(my_map)
    my_map.save(filename)
    return os.path.abspath(filename)