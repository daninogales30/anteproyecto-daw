# Anteproyecto Daniel Nogales Mateos
## Título del proyecto
- MyFitSpace

## Autor del proyecto
- Daniel Nogales Mateos

## Introducción al proyecto
- Quiero hacer un proyecto que creo que es muy original y puede ser de mucha ayuda para los usuarios mas fitness. Me gustaría hacer con Django una aplicación web donde un usuario pueda crear rutinas de entrenamiento, dietas, haya dietas predefinidas, registros de pesos del usuario, gestiones futuras del proyecto como contactar con entrenadores personales, integrar apis de nutricion como Edamam, CalorieKing, etc...

## Finalidad
- Puede servir para que los usuarios que son poco fitness se motiven a entrenar, a registrar sus comidas, sus entrenamientos, etc...
- También puede servir para las personas más avanzadas para poder registrar sus entrenamientos de una forma mucho más cómodas en vez de usar folios o el bloc de notas.
- En general, este proyecto serviría para que la gente sea un poco mas "healthy", mejoren su salud tanto física, como mental, ya que es una aplicacion intuitiva para que se les haga todo mas ameno.

## Objetivos 
- Los objetivos de esta aplicación, una vez se hiciera real y se pusiera en marcha es tener una versión con anuncios, luego tener otra versión de pago sin anuncios y otra version premium más cara pero con alguna funcionalidad extra.
- Una vez puesta en marcha, el objetivo es que el usuario que la use pueda empezar a realizar rutinas predefinidas, crear sus propias rutinas e inclusive registrar su alimentacion

## Medios hardware y software a utilizar
- En este caso como medio de hardware voy a utilizar mi ordenador.
- Si hablamos de software, el proyecto que voy a realizar es una aplicación web con Python, usando el framework Django. Para la parte del fronted, intentaré usar React pero no prometo nada, ya que ahora mismo no tengo muchos conocimientos sobre el framework. En el caso de que no llegue a poder implementarlo con React, usare HTML, CSS Y Javascript.

## Planificación 
- Ahora mismo al ser una idea muy general tengo una pequeña idea de como puedo empezar a meterle mano pero no lo sé al 100%
- Probablente usare la api de CalorieKing, ya que es gratuita. Para el tema de los alimentos, pero empezare creando apps de rutina, entrenamiento, persona. Probablemente despues de terminar lo principal de la página y dentro de un tiempo le implementaré algo más opcional como foros, seguir a usuarios fitness, ranking de usuarios con más rutinas hechas, etc... Es un campo tan amplio que la creatividad vuela.

### Del 24 de marzo al 7 de abril
- A día 2 de abril lo que llevo realizado es la creación de las apps diets, persons y workout_routines. En diets lo unico que tengo montado ahora mismo es el models.py, en la app persons tengo el models.py, tambien tengo los forms para la creación del usuario, y algunas vistas como los detalles del usuario, el login y el register. En workout_routines tengo el models.py y algunas vistas de los formularios para crear una rutina y crear un entrenamiento
- A día 3 de abril he detectado un problema que solucionaré sobre el calculo de grasa corporal. Estoy avanzando en el tema vistas me gustaria hacer vistas de listas de entrenamientos ya creados para que los usuarios puedan realizar y que tambien puedan crear sus propios entrenamientos.
- A día 7 de abril, he añadido la lista de los entrenamientos por usuarios y también que los usuarios puedan ver detalladamente los ejercicios que hacen los lunes, martes, etc... Aparte, he creado la carpeta static/pdfs, donde voy a poner el manual de uso de la página para que puedan descargarlo y verlo.

### Del 8 de abril al 21 de abril
- A día 8 de abril, he añadido el metodo para calcular calorias diarias dependiendo de su altura, peso, si es sedentario, activo, muy activo, etc... También, me he dado cuenta que el método de calcular el porcentaje de grasa necesita un cambio ya que dependiendo de los datos que introduzca da un error matemático, por lo cual debo de hacer las comprobaciones para que el resultado de lo más acertado posible y ponerle ciertas condiciones a los datos.
- A día 21 de abril, he mejorado la vista previa del html de profile pero sobre todo he encontrado un error que tengo que solucionar. He visto que al crear una rutina para añadir al entrenamiento aparecen todos los workouts de la base de datos, no solamente los del usuario, es algo que tenemos que modificar.
- A día 21 de abril, ya he podido solucionar ese error, filtrando en el formulario solamente los workouts creados por el usuario.

### Del 22 de abril al 5 de mayo
- A día 25 de abril, he añadido una view para eliminar rutinas y tambien una lista con armas precargadas. Ahora mismo, la parte de workout_routine esta terminada, solo falta empezar el diseño con Bootstrap.
