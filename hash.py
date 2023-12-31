import hashlib

while True:
    animeName = input("Nombre del anime: ")
    animeId = hashlib.sha256(animeName.encode('utf-8')).hexdigest()[:16]
    print(f"Id: {animeId}\n")
