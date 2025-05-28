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

## Errores a solucionar
- He detectado un error y es el siguiente. Cuando le añado un alimento a un dia de la semana, si vuelvo a añadir ese alimento a otro dia de esa misma semana no se puede, eso quiere decir que hay algo que esta diciendo que ese alimento es unico en ese dia, cosa que no es óptima.

## ¿Que falta?
- Migracion para precargar dietas personalizadas y meter muchisimos alimentos.
- Modificar la migracion de workout para personalizar más los workout dependiendo del nivel.

### Del 24 de marzo al 7 de abril
- A día 2 de abril lo que llevo realizado es la creación de las apps diets, persons y workout_routines. En diets lo unico que tengo montado ahora mismo es el models.py, en la app persons tengo el models.py, tambien tengo los forms para la creación del usuario, y algunas vistas como los detalles del usuario, el login y el register. En workout_routines tengo el models.py y algunas vistas de los formularios para crear una rutina y crear un entrenamiento
- A día 3 de abril he detectado un problema que solucionaré sobre el calculo de grasa corporal. Estoy avanzando en el tema vistas me gustaria hacer vistas de listas de entrenamientos ya creados para que los usuarios puedan realizar y que tambien puedan crear sus propios entrenamientos.
- A día 7 de abril, he añadido la lista de los entrenamientos por usuarios y también que los usuarios puedan ver detalladamente los ejercicios que hacen los lunes, martes, etc... Aparte, he creado la carpeta static/pdfs, donde voy a poner el manual de uso de la página para que puedan descargarlo y verlo.

### Del 8 de abril al 21 de abril
- A día 8 de abril, he añadido el metodo para calcular calorias diarias dependiendo de su altura, peso, si es sedentario, activo, muy activo, etc... También, me he dado cuenta que el método de calcular el porcentaje de grasa necesita un cambio ya que dependiendo de los datos que introduzca da un error matemático, por lo cual debo de hacer las comprobaciones para que el resultado de lo más acertado posible y ponerle ciertas condiciones a los datos.
- A día 21 de abril, he mejorado la vista previa del html de profile pero sobre todo he encontrado un error que tengo que solucionar. He visto que al crear una rutina para añadir al entrenamiento aparecen todos los workouts de la base de datos, no solamente los del usuario, es algo que tenemos que modificar.
- A día 21 de abril, ya he podido solucionar ese error, filtrando en el formulario solamente los workouts creados por el usuario.

### Del 22 de abril al 5 de mayo
- A día 25 de abril, he añadido una view para eliminar rutinas y tambien una lista con armas precargadas. Ahora mismo, la parte de workout_routine esta terminada, solo falta empezar el diseño con Bootstrap. He terminado todo el diseño de la app persons y también de la app workout_routines, solo me falta de esta última app el preloaded.html. Solo me quedaría empezar a plantear como hacer la app diets y hacerla.
- A día 28 de abril, ya he terminado con el apartado de workouts. He terminado el diseño de todas las vistas que tengo de workout. Cuando acabe la parte de dietas me faltaría poner unas vistas de apiRest por ejemplo, usuarios con mas entrenamientos creados, es decir, los mas activos, etc... Ya he empezado el tema de las dietas, en este caso la SemanalDiets, que las pueda crear cada usuario, verificar que solo tenga una con el mismo nombre, etc... El apartado de la vista de crear dieta semanal, una list view de las dietas del usuario y otra view para eliminar esa dieta semanal.
- A día 29 de abril, he remodelado la app diets, ya que lo tenía demasiado rebuscado y mirandolo en frío hay ciertas funciones que es mejor que el usuario no haga para no liarse, por lo tanto he intentado hacerlo de la mejor manera posible. También he añadido la vista de detalles de la deta semanal porque quiero poner un elemento gráfico que sea algo como (el nº de calorias actuales de la semana/el nº de calorias que dependiendo de su objeto necesita tener a la semana) y que al lado ponga algo como el rango es bueno, o si se pasa de calorias poner el numero de calorias es excesivo, etc... Algo para que el usuario vea cuantas calorias lleva en la semana y cuantas necesita realmente.
- A día 30 de abril, he creado una view con ApiRest Framework para que me muestre los 5 usuarios con mas entrenamientos creados, digamos como si fueran los usuarios más activos en el tema de entrenamientos, ya que no cuentan los entrenamientos vacíos, debe haberle introducido al menos una rutina. Mejorado el modelo dieta.

### Del 6 de mayo al 19 de mayo
- A día 6 de mayo, he solucionado un problema que había que era bastante importante, ya que en los formularios que había el select de Dieta Semanal, mostraba el de todos los usuarios, y al formulario le he tenido que pasar un filter que solo muestre los del usuario, pillado el usuario desde los kwargs. Me falta mejorar el html de los detalles de las dietas semanales ya que la view esta creada pero todavia no le he podido meter mano al template. Html mejorado y listo, solo me faltaria ir cambiando los title de los html y haciendo el base.html para que todo el contenido parta de ahí, pero lo que es lo importante está realizado.
- A día 7 de mayo, cambios a realizar, mejorar el tema de usabilidad en el sentido de la navegación, poner views que se pueda modificar los workouts y las dietas, poner dietas y entrenamientos precargados adaptadas al nivel de entrenamiento del usuario y de las calorias diarias del usuario. Formulario de DayDietForm mejorado, para que cuando seleccione una semana le salgan los días creados por el usuario en esa semana, para que no se pueda confundir con otros dias.
- A día 8 de mayo, he mejorado y he puesto vistas para que se puedan editar y borrar los entrenamientos y las rutinas. Las dietas también pero no me gusta del todo como ha quedado, lo voy a dejar así y ya voy viendo que cambios puedo hacerle. He mejorado el diseño un poco sobre todo en el del ranking de usuarios más activos, pero me gustaría añadirle css ya que el diseño solo con bootstrap no me llega a gustar del todo. También le he añadido la descarga del archivo instrucciones.pdf para que el usuario pueda guiarse a través de un manual. Aparte, quiero añadir un video explicativo del funcionamiento de la app tanto como para la entrega del proyecto como para el funcionamiento de la web, para que los usuarios puedan tener un video explicativo de como usar la página web, por si prefieren verlo visualmente antes que leerse el pdf.
- A día 9 de mayo, he mejorado un poco la navegación de la página añadiendo botones de retroceso por si has entrado en algun formulario y quieres volver atras, que no tengas que hacerlo desde el navegador, si no que la página sea lo más intuitiva posible.
- A día 10 de mayo, he creado css para vistas principales y formularios, inicio de sesion, registrar usuario, etc... Falta todavía alguna que otra.
- A día 15 de mayo, he estado creando los css restantes para que la aplicacion quede más estética pero sobre todo he estado creando una vista para editar los datos de las dietas semanales creadas y la creación de los archivos Dockerfile, docker-compose y requirements para el funcionamiento en el despliegue en docker. Mi idea, es poder desplegarlo en una máquina en AWS con una ip elástica que apunte a nuestro dominio en ".tech". He remodelado la mayoria de htmls (faltan sobre todo el de dietas y algunos de workout_routine) para que partan desde un base.html, para tener el contenido digamos más recogido y no con tanto código html repetido.
- A día 16 de mayo, he terminado de poner todos los htmls lo más optimizados posibles. Me falta algunos css como el de eliminar dietas, entrenamientos, etc... Css de perfil modificado y error solucionado, no se mostraba la imagen de perfil correctamente.

### Del 20 de mayo al 2 de junio
- A día 20 de mayo, he añadido la imagen default.png para los usuario que no quieran añadir foto de perfil.
- A día 21 de mayo, he creado el css de los detalles de las dietas, me falta el css para las vistas que sean de eliminar. **Error**: He detectado un error y es el siguiente. Cuando le añado un alimento a un dia de la semana, si vuelvo a añadir ese alimento a otro dia de esa misma semana no se puede, eso quiere decir que hay algo que esta diciendo que ese alimento es unico en ese dia, cosa que no es óptima, para mañana lo tendré ya solucionado.
- A día 27 de mayo, ya he mejorado el html de profile con un diseño más parecido al que tienen a día de hoy las redes sociales. Error que tenia pendiente sobre las dietas ya lo acabo de solucionar.
- A día 28 de mayo he mejorado la migracion de poblar datos de entrenamiento ya que solo estaba creando los ejercicios, ahora tambien crea un workout precargado para los usuarios y les aparece el semejante a su nivel, aunque todavia falta por meter workouts de nivel amateur, profesional y culturista. También falta crear las dietas precargadas y ya estaría todo casi listo. Ya estan creado para los workouts de distintos niveles, pero falta cambiar la dificultad de los ejercicios y crear la migración de las dietas.
