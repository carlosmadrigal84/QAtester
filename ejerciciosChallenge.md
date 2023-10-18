
## task 2

Plan de Pruebas parala API

1. Prueba de que la Recuperación de la Información del Personaje salió bien
Contexto: Verificar que el código pueda recuperar exitosamente información de un personaje válido.
Pasos a seguir:            :
Ingresar un nombre de personaje válido (por ejemplo, "Rick Sanchez").
Asegurarse de que el código devuelva información precisa sobre el personaje, incluyendo especie, tipo y detalles del episodio.
Resultado Esperado: El código debería recuperar y mostrar información correcta sobre el personaje.
En mi código, al poner un personaje real de la serie, la api devuelve la información que le pido.

2. Prueba de Nombre de Personaje Inválido
Contexto: Validar el comportamiento del código cuando se proporciona un nombre de personaje inválido.
Pasos a seguir:
Ingresar un nombre de personaje inválido (por ejemplo, "InvalidCharacter123").
Verificar cómo maneja el código la ausencia de información del personaje.
Resultado Esperado: El código debería devolver un mensaje indicando que no se encontró al personaje.
En mi código, el mensaje mostrado de error es el siguiente:
Traceback (most recent call last):
  File "C:\Users\Carlos\Desktop\FP DAW\Cursos Cisco\Python Cisco\QA_tester.py", line 68, in <module>
    print("Información del personaje ->", informacion_personaje["Información del personaje"])
TypeError: string indices must be integers, not 'str'

3. Prueba de Nombre de Personaje Vacío
Contexto: Verificar la respuesta del código cuando se proporciona un nombre de personaje vacío.
Pasos a seguir:
Ingresar un nombre de personaje vacío.
Observar cómo reacciona el código ante la entrada vacía.
Resultado Esperado: El código debería devolver un mensaje indicando que se requiere un nombre de personaje.
En mi código, tarda mucho en salir una respuesta, y después de unos segundos, aparece mucha información, como si fueran todas las localizaciones y episodios que hay en la API

4. Prueba de Recuperación de Personaje con Caracteres Especiales en el Nombre
Contexto: Asegurar que el código pueda manejar nombres de personajes con caracteres especiales.
Pasos a seguir:
Ingresar un nombre de personaje con caracteres especiales (por ejemplo, "Birdperson (Special)").
Verificar que el código recupere con precisión y muestre información sobre el personaje.
Resultado Esperado: El código debería manejar y procesar correctamente nombres de personajes con caracteres especiales.
En mi código, el mensaje mostrado de error es el siguiente:
Traceback (most recent call last):
  File "C:\Users\Carlos\Desktop\FP DAW\Cursos Cisco\Python Cisco\QA_tester.py", line 68, in <module>
    print("Información del personaje ->", informacion_personaje["Información del personaje"])
TypeError: string indices must be integers, not 'str'

5. Prueba de Nombre de Personaje Revertido
Contexto: Validar el comportamiento del código cuando se proporciona el nombre del personaje en orden inverso.
Pasos a seguir:
Ingresar un nombre de personaje en orden inverso (por ejemplo, "sknaht").
Verificar cómo procesa y maneja el código la entrada revertida.
Resultado Esperado: El código debería manejar nombres de personajes revertidos y devolver un mensaje indicando que no se encontró al personaje.
En mi código, el mensaje mostrado de error es el siguiente:
Traceback (most recent call last):
  File "C:\Users\Carlos\Desktop\FP DAW\Cursos Cisco\Python Cisco\QA_tester.py", line 68, in <module>
    print("Información del personaje ->", informacion_personaje["Información del personaje"])
TypeError: string indices must be integers, not 'str'

6. Prueba de Disponibilidad de la API y Tiempo de Respuesta
Contexto: Asegurar que la API sea accesible y tenga una respuesta rápida.
Pasos a seguir:
Enviar una solicitud al punto final de la API utilizado en el código.
Medir el tiempo de respuesta y verificar si hay errores.
Resultado Esperado: La API debería estar disponible y el tiempo de respuesta debería estar dentro de un rango aceptable.
En mi código, el tiempo de respuesta tiene un rango de entre 2 y 3 segundos

7. Prueba de Manejo de Solicitudes Masivas
Contexto: Evaluar el rendimiento del código al manejar múltiples solicitudes.
Pasos a seguir:
Simular un escenario con un gran volumen de solicitudes (por ejemplo, 100 solicitudes).
Observar cómo el código gestiona y responde a estas solicitudes.
Resultado Esperado: El código debería manejar las solicitudes masivas de manera adecuada sin errores graves ni un aumento significativo en los tiempos de respuesta.
Al llevar a cabo estas pruebas, asegurarás que el código de Python que interactúa con la API de Rick and Morty funcione correctamente, maneje varios escenarios y proporcione información confiable y precisa sobre los personajes.
En mi código, convierto la variable en una lista para meter varios personajes de la API, y da este error:
Traceback (most recent call last):
  File "C:\Users\Carlos\Desktop\FP DAW\Cursos Cisco\Python Cisco\QA_tester.py", line 69, in <module>
    print("Información del personaje ->", informacion_personaje["Información del personaje"])
TypeError: string indices must be integers, not 'str'

## Task 3

Buscando por internet, he visto que Python incorpora una librería llamada "unittest", que es un marco de pruebas que permite realizar pruebas de integración.

Se utiliza junto con la librería "requests".

Primero se tiene que crear un archivo en el cual definiremos y ejecutaremos varias pruebas de integración.
En él, crearemos el código donde podemos plantear supuestos para ver si falla el código, como meter un nombre correcto, meter un nombre incorrecto, un nombre "vacío", poner las urls por separado o meter caracteres especiales para ver si falla.

A continucación se tiene que ejecutar un comando para iniciar las pruebas de integración:

python -m unittest [nombre del archivo]

Con los resultados obtenidos, verificaremos si funcionan bien las funciones creadas y su integración.

## Extra task

Como idea estando más tranquilo y sin tanta presión como esta mañana, a mi, que vengo del Front, se me ocurre poder interactuar con el usuario.
En vez de poner una variable con un personaje guardado como he puesto en el código enviado, se me ocurre hacer un input donde el usuario pueda introducir el personaje que quiera y que la API me devuelva la información establecida en el código.

En este caso, utilizaría un método trim() para quitar los posibles espacios en blanco que introduzca el usuario, para evitar errores a la hora de buscar el personaje en la API, y a parte, lo pasaría todo a "lowercase", o a "capitalize", por que he visto en la API que los nombres vienen con la primera letra en mayúscula.
A parte creo que podría separar la obtención de datos de alguna URL fuera de la función principal para optimizar la cantidad de datos que obtiene la función y que así tardaría un poco menos en ejecutar el programa.


