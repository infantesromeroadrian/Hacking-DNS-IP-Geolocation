import dns.resolver
import re

def validar_dominio(dominio):
    """
    Valida que un dominio tenga un formato correcto.

    Args:
        dominio (str): Nombre del dominio a validar.

    Returns:
        bool: True si el dominio es válido, False en caso contrario.
    """
    regex = r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
    return re.match(regex, dominio)

def obtener_registro_a(dominio):
    """
    Obtiene las direcciones IP asociadas al registro A de un dominio.

    Args:
        dominio (str): Nombre del dominio a consultar.

    Returns:
        list: Lista de direcciones IP asociadas al dominio.
    """
    try:
        respuesta = dns.resolver.resolve(dominio, 'A')
        return [rdata.address for rdata in respuesta]
    except dns.resolver.NoAnswer:
        print(f"El dominio {dominio} no tiene registros A.")
    except dns.resolver.NXDOMAIN:
        print(f"El dominio {dominio} no existe.")
    except Exception as e:
        print(f"Error al resolver el dominio {dominio}: {e}")
    return []
