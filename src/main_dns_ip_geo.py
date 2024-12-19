from dns_ip_resolver import validar_dominio, obtener_registro_a
from ip_geolocation import get_ip_details, draw_map, draw_multiple_maps, verificar_puerto
from dotenv import load_dotenv
import os
import sys
import csv

# Cargar las variables de entorno desde un archivo .env
load_dotenv()

# Obtener el token de acceso desde las variables de entorno
ACCESS_TOKEN = os.getenv("IPINFO_API_KEY")
if not ACCESS_TOKEN:
    print("Error: La variable de entorno IPINFO_API_KEY no está configurada.")
    sys.exit(1)

def exportar_a_csv(data, filename="geolocalizacion.csv"):
    """
    Exporta los datos a un archivo CSV.

    Args:
        data (list of dict): Datos a exportar.
        filename (str): Nombre del archivo de salida.
    """
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["IP", "Dominio", "Latitud", "Longitud", "Ubicación", "Puerto Abierto"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Datos exportados a {filename}")

def main():
    print("=== Resolución de IP y Geolocalización ===")
    dominio = input("Introduce el nombre del dominio (e.g., example.com): ").strip()

    # Validar el dominio ingresado
    if not validar_dominio(dominio):
        print("El dominio ingresado no es válido. Inténtalo de nuevo.")
        return

    # Resolver las direcciones IP del dominio
    print(f"\nResolviendo direcciones IP para el dominio: {dominio}")
    ips = obtener_registro_a(dominio)

    if not ips:
        print(f"No se encontraron direcciones IP para {dominio}.")
        return

    print(f"\nDirecciones IP encontradas para {dominio}: {', '.join(ips)}")

    # Geolocalizar cada IP y verificar puertos
    ip_locations = []
    for ip in ips:
        print(f"\nObteniendo información de geolocalización para la IP: {ip}")
        details = get_ip_details(ip, ACCESS_TOKEN)

        if not details:
            print(f"Error al obtener detalles de la IP {ip}.")
            continue

        # Extraer latitud, longitud y región del diccionario de detalles
        try:
            latitude = float(details["latitude"])
            longitude = float(details["longitude"])
            location = details.get("region", "Ubicación Desconocida")
            if not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
                raise ValueError("Coordenadas fuera de rango.")
        except (KeyError, ValueError) as e:
            print(f"Error al extraer coordenadas de la IP {ip}: {e}")
            continue

        # Verificar si el puerto 80 está abierto
        puerto_abierto = verificar_puerto(ip, 80)

        # Agregar al diccionario de ubicaciones
        ip_locations.append({
            "IP": ip,
            "Dominio": dominio,
            "Latitud": latitude,
            "Longitud": longitude,
            "Ubicación": location,
            "Puerto Abierto": "Sí" if puerto_abierto else "No"
        })

    # Generar mapa interactivo único con todas las ubicaciones
    if ip_locations:
        map_file_path = draw_multiple_maps({loc["IP"]: (loc["Latitud"], loc["Longitud"], loc["Ubicación"]) for loc in ip_locations})
        print(f"Mapa interactivo con todas las IPs guardado en: {map_file_path}")
        exportar_a_csv(ip_locations)
    else:
        print("No se generaron mapas debido a errores en los datos de geolocalización.")

if __name__ == "__main__":
    main()
