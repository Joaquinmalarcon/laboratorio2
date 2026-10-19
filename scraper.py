
import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"

def obtener_libros():
    respuesta = requests.get(URL, timeout=10)
    respuesta.raise_for_status()
    respuesta.encoding = "utf-8"

    soup = BeautifulSoup(respuesta.text, "html.parser")

    libros = []

    estrellas = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    for libro in soup.select("article.product_pod"):
        try:
            titulo = libro.select_one("h3 a")["title"]

            precio = libro.select_one(".price_color").text
            precio = float(precio.replace("£", ""))

            disponibilidad = libro.select_one(".availability").text.strip()

            clase = libro.select_one(".star-rating")["class"][1]
            calificacion = estrellas[clase]

            libros.append({
                "titulo": titulo,
                "precio": precio,
                "disponibilidad": disponibilidad,
                "calificacion": calificacion
            })

        except (AttributeError, KeyError, ValueError, TypeError, IndexError) as error:
            print("Libro omitido:", error)

    return libros


if __name__ == "__main__":
    libros = obtener_libros()

    print("Total de libros extraidos:", len(libros))

    print("\nPrimeros 5 libros:")
    for libro in libros[:5]:
        print(libro)
