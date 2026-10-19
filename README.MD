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

Respuestas: Una limitación de TF-IDF es que busca coincidencias entre palabras, pero no comprende su significado esto puede provocar que no se encuentren libros relacionados que utilicen palabras diferentes



| Caso | Consulta utilizada | Resultado observado           | Estado |
|------|--------------------|-------------------------------|--------|
| T1   |    life            |Se recuperó un libro           |cumple  |
| T2   |   ajhsdjas123      |No se encontraron coincidencias|cumple  |
| T3   |      LIFE          |Mismo ranking de T1            |cumple  |
| T4   |    [Vacía]         |"Ingrese una consulta no vacia"|cumple  |
