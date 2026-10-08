import os
import shutil

# Usamos la carpeta 'prueba' que vimos en tu captura
DIRECTORIO_DESTINO = "./prueba"

CATEGORIAS = {
    "Imagenes": ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
    "Documentos": ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
    "Comprimidos": ['.zip', '.rar', '.tar', '.gz']
}

def organizar_archivos():
    if not os.path.exists(DIRECTORIO_DESTINO):
        print(f"La carpeta {DIRECTORIO_DESTINO} no existe.")
        return

    archivos = os.listdir(DIRECTORIO_DESTINO)
    print(f"--- Archivos encontrados en 'prueba': {archivos} ---")

    for archivo in archivos:
        ruta_archivo = os.path.join(DIRECTORIO_DESTINO, archivo)
        
        if os.path.isdir(ruta_archivo):
            continue

        extension = os.path.splitext(archivo)[1].lower()
        print(f"Revisando archivo: '{archivo}' con extensión: '{extension}'")
        
        archivo_movido = False

        for categoria, extensiones in CATEGORIAS.items():
            if extension in extensiones:
                subcarpeta = os.path.join(DIRECTORIO_DESTINO, categoria)
                os.makedirs(subcarpeta, exist_ok=True)
                
                shutil.move(ruta_archivo, os.path.join(subcarpeta, archivo))
                print(f" ¡Movido con éxito: {archivo} -> /{categoria}/")
                archivo_movido = True
                break
        
        if not archivo_movido:
            print(f"⚠️ La extensión '{extension}' del archivo '{archivo}' no está en ninguna categoría.")

if __name__ == "__main__":
    organizar_archivos()