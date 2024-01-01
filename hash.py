import hashlib

while True:
    # Solicita al usuario ingresar un nombre de anime
    anime_name = input("Ingresa el nombre del anime (o 'exit' para salir): ")

    # Verifica si el usuario desea salir
    if anime_name.lower() == 'exit':
        break

    # Calcula el hash SHA-256 y muestra los primeros 16 caracteres
    hash_value = hashlib.sha256(anime_name.encode('utf-8')).hexdigest()[:16]
    print(f"Hash SHA-256 del nombre '{anime_name}': {hash_value}")
    print()

# Mensaje de despedida
print("¡Adiós!")
