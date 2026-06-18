import sys
import time
from pathlib import Path
import wikipedia
from requests.exceptions import JSONDecodeError


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Debes pasar un parámetro")
        sys.exit(0)

    nombre_wiki = sys.argv[1]
    carpeta_wikis = Path("wikis")
    carpeta_wikis.mkdir(exist_ok=True)
    archivo = carpeta_wikis / f"{nombre_wiki}.txt"

    if archivo.exists():
        print(f"El archivo '{archivo}' ya existe.")
        sys.exit(0)

    max_intentos = 10

    for intento in range(max_intentos):
        try:
            print(f"Descargando '{nombre_wiki}'...")

            texto_wiki = wikipedia.page(
                nombre_wiki,
                auto_suggest=False
            ).content

            archivo.write_text(texto_wiki, encoding="utf-8")

            print(f"Página guardada en '{archivo}'.")
            break

        except JSONDecodeError as e:
            print(
                f"Intento {intento + 1}/{max_intentos} falló: {e}"
            )

            if intento < max_intentos - 1:
                time.sleep(10)
            else:
                print(
                    f"No se pudo descargar '{nombre_wiki}' "
                    f"después de {max_intentos} intentos."
                )
                sys.exit(1)