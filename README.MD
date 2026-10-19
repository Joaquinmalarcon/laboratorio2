#INTEGRANTES: VICENTE CISTERNAS, JOAQUIN MUÑOZ

1 Para qué sirve BeautifulSoup y cómo se diferencia de requests?

Respuesta: Requests sirve para obtener el contenido HTML de una página web, mientras que BeautifulSoup permite analizar ese HTML y extraer información específica, como títulos, etc.

2 Qué riesgo existe al depender de selectores HTML específicos si el sitio cambia?

Respuesta: Si la estructura HTML de la página cambia, los selectores podrían dejar de funcionar y el programa no encontraría los datos correctos.

3 Por qué normalizar los títulos antes de implementar la búsqueda?

Respuesta: Se normalizan los títulos para eliminar espacios innecesarios y convertirlos a minúsculas permitimiento comparar los textos de forma más uniforme y facilita las búsquedas

4 Qué función cumple fit_transform() sobre los títulos y por qué se usa transform() para la consulta?

Respuesta: fit_transform() aprende el vocabulario de los títulos y los convierte en vectores TF-IDF. transform() convierte la consulta utilizando ese mismo vocabulario sin modificar el índice creado.

5 Si dos libros obtienen similitudes de 0.75 y 0.20, ¿cuál se muestra primero? ¿Qué indica una puntuación cercana a cero?

Respuesta: Se muestra primero el libro con similitud de 0.75 porque tiene mayor coincidencia con la consulta. Una puntuación cercana a cero indica que comparte pocas o ninguna palabra relevante con el título buscado.

6 Qué limitación tiene buscar solo por palabras presentes en títulos mediante TF-IDF? Proponga una mejora concreta.

Respuestas: Una limitación de TF-IDF es que busca coincidencias entre palabras, pero no comprende su significado esto puede provocar que no se encuentren libros relacionados que utilicen palabras diferentes. Una mejora sería implementar una búsqueda semántica que permita encontrar libros con significados similares

#EVIDENCIAS
PS C:\Users\Estudiante\Desktop\laboratorio2> py .\procesamiento.py
Primeros 5 libros:
                                  titulo  precio disponibilidad  calificacion
0                   A Light in the Attic   51.77       In stock             3
1                     Tipping the Velvet   53.74       In stock             1
2                             Soumission   50.10       In stock             1
3                          Sharp Objects   47.82       In stock             4
4  Sapiens: A Brief History of Humankind   54.23       In stock             5

Informacion del DataFrame:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20 entries, 0 to 19
Data columns (total 4 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   titulo          20 non-null     object
 1   precio          20 non-null     float64
 2   disponibilidad  20 non-null     object
 3   calificacion    20 non-null     int64
dtypes: float64(1), int64(1), object(2)
memory usage: 768.0+ bytes

Filas y columnas:
(20, 4)

Cantidad de libros: 20
Precio promedio: 38.048500000000004

Archivo libros.csv creado correctamente.


| Caso | Consulta utilizada | Resultado observado           | Estado |
|------|--------------------|-------------------------------|--------|
| T1   |    life            |Se recuperó 3 libros           |cumple  |
| T2   |   ajhsdjas123      |No se encontraron coincidencias|cumple  |
| T3   |      LIFE          |Mismo ranking de T1            |cumple  |
| T4   |    [Vacía]         |"Ingrese una consulta no vacia"|cumple  |
