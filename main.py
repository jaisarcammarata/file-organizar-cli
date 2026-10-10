import os
import shutil

# Directorio de trabajo
DIRECTORIO_DESTINO = "./prueba"

# Diccionario de categorías y sus extensiones asociadas
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
    print(f"\n--- Iniciando organización (Día 3) ---")

    for archivo in archivos:
        ruta_archivo = os.path.join(DIRECTORIO_DESTINO, archivo)
        
        # Ignorar si es una carpeta
        if os.path.isdir(ruta_archivo):
            continue

        extension = os.path.splitext(archivo)[1].lower()
        archivo_movido = False

        for categoria, extensiones in CATEGORIAS.items():
            if extension in extensiones:
                subcarpeta = os.path.join(DIRECTORIO_DESTINO, categoria)
                os.makedirs(subcarpeta, exist_ok=True)
                
                ruta_destino = os.path.join(subcarpeta, archivo)
                
                # Validación de seguridad: Si ya existe un archivo con el mismo nombre
                if os.path.exists(ruta_destino):
                    print(f"⚠️ El archivo '{archivo}' ya existe en /{categoria}/. Se omite para evitar duplicados.")
                    archivo_movido = True
                    break

                try:
                    shutil.move(ruta_archivo, ruta_destino)
                    print(f"✅ Movido con éxito: {archivo} -> /{categoria}/")
                except Exception as e:
                    print(f"❌ Error al mover '{archivo}': {e}")
                
                archivo_movido = True
                break
        
        if not archivo_movido and extension:
            print(f"ℹ️ Sin categoría para: '{archivo}' (extensión {extension})")

if __name__ == "__main__":
    organizar_archivos()