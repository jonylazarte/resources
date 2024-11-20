import os

def renombrar_archivos(carpeta):
    """Renombra todos los archivos en una carpeta, convirtiéndolos a minúsculas y reemplazando espacios por guiones.

    Args:
        carpeta (str): Ruta de la carpeta donde se encuentran los archivos.
    """

    for archivo in os.listdir("./"):
        ruta_antigua = os.path.join(carpeta, archivo)
        nombre_nuevo = archivo.lower().replace(" ", "-")
        ruta_nueva = os.path.join(carpeta, nombre_nuevo)
        os.rename(ruta_antigua, ruta_nueva)

# Ejemplo de uso:
carpeta_a_procesar = r"C:\Users\shaka\OneDrive\Escritorio\3DS - Pokemon Sun Moon - Attack Move Sound Effects"  # Reemplaza con la ruta de tu carpeta
renombrar_archivos(carpeta_a_procesar)
