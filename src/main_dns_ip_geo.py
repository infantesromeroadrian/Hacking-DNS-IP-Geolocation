from dns_ip_resolver import obtener_registro_a
from ip_geolocation import get_ip_details, draw_map
from dotenv import load_dotenv
import os
import sys

# Cargar las variables de entorno desde un archivo .env
load_dotenv()

# Obtener el token de acceso desde las variables de entorno
ACCESS_TOKEN = os.getenv("IPINFO_API_KEY")
if not ACCESS_TOKEN:
    print("Error: La variable de entorno IPINFO_API_KEY no está configurada.")
    sys.exit(1)

def main():
    print("=== Resolución de IP y Geolocalización ===")
    dominio = input("Introduce el nombre del dominio (e.g., example.com): ").strip()

    # Resolver las direcciones IP del dominio
    print(f"\nResolviendo direcciones IP para el dominio: {dominio}")
    ips = obtener_registro_a(dominio)

    if not ips:
        print(f"No se encontraron direcciones IP para {dominio}.")
        return

    print(f"\nDirecciones IP encontradas para {dominio}: {', '.join(ips)}")

    # Geolocalizar cada IP y generar mapas
    for ip in ips:
        print(f"\nObteniendo información de geolocalización para la IP: {ip}")
        details = get_ip_details(ip, ACCESS_TOKEN)

        # Imprimir detalles de la IP
        print("\n=== Detalles de la IP ===")
        for key, value in details.items():
            print(f"{key}: {value}")

        # Extraer latitud, longitud y región del diccionario de detalles
        try:
            latitude = float(details["latitude"])
            longitude = float(details["longitude"])
            location = details.get("region", "Ubicación Desconocida")
        except KeyError as e:
            print(f"Error al extraer coordenadas de la IP {ip}: {e}")
            continue

        # Generar y guardar el mapa interactivo
        map_file_path = draw_map(latitude, longitude, location, filename=f"map_{ip}.html")
        print(f"Mapa para la IP {ip} guardado en: {map_file_path}")

if __name__ == "__main__":
    main()