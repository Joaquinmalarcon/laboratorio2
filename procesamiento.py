
import pandas as pd
from scraper import obtener_libros


libros = obtener_libros()

if not libros:
    raise SystemExit("No se extrajeron libros.")

df = pd.DataFrame(libros)

print("Primeros 5 libros:")
print(df.head())

print("\nInformacion del DataFrame:")
df.info()

print("\nFilas y columnas:")
print(df.shape)

df["titulo"] = df["titulo"].str.strip()
df = df.drop_duplicates(subset="titulo")

df["titulo_normalizado"] = df["titulo"].str.lower()

df["precio"] = pd.to_numeric(df["precio"])
df["calificacion"] = pd.to_numeric(df["calificacion"])

print("\nCantidad de libros:", len(df))
print("Precio promedio:", df["precio"].mean())

df.to_csv("libros.csv", index=False, encoding="utf-8")

print("\nArchivo libros.csv creado correctamente.")
