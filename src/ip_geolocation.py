import ipinfo
from folium import Map, Marker, FeatureGroup
import os
import socket

def get_ip_details(ip_addr, access_token):
    """
    Obtiene detalles de geolocalización de una dirección IP utilizando la API de ipinfo.

    Args:
        ip_addr (str): La dirección IP de la cual obtener la información.
        access_token (str): El token de acceso para la API de ipinfo.

    Returns:
        dict: Un diccionario con todos los detalles obtenidos.
    """
    try:
        handler = ipinfo.getHandler(access_token)
        details = handler.getDetails(ip_addr)
        return details.all
    except Exception as e:
        print(f"Error al obtener los detalles de la IP '{ip_addr}': {e}")
        return None

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

def draw_multiple_maps(ip_locations, filename="multi_map.html"):
    """
    Genera un único mapa HTML con múltiples marcadores.

    Args:
        ip_locations (dict): Diccionario con IPs como clave y una tupla (lat, lon, descripción) como valor.
        filename (str): Nombre del archivo donde se guardará el mapa.

    Returns:
        str: Ruta absoluta al archivo del mapa generado.
    """
    my_map = Map(location=[0, 0], zoom_start=2)  # Vista inicial global
    fg = FeatureGroup(name="Geolocalización de IPs")

    for ip, (latitude, longitude, location) in ip_locations.items():
        Marker([latitude, longitude], popup=f"{ip}: {location}").add_to(fg)

    fg.add_to(my_map)
    my_map.save(filename)
    return os.path.abspath(filename)

def verificar_puerto(ip, puerto):
    """
    Verifica si un puerto está abierto en una dirección IP.

    Args:
        ip (str): Dirección IP a comprobar.
        puerto (int): Puerto a verificar.

    Returns:
        bool: True si el puerto está abierto, False en caso contrario.
    """
    try:
        with socket.create_connection((ip, puerto), timeout=2):
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False