# smart-clock ⌚
Reloj inteligente para exposiciones en la U (rescatado del tacho 2016) 🚮
## Proyecto de Reloj Bluetooth Controlado por Arduino

Este proyecto consiste en la creación de un reloj que, aunque no muestra la hora, permite controlar funciones en un dispositivo externo (como una laptop) a través de una conexión Bluetooth. 
El reloj está diseñado para ser compacto y llevarlo en la muñeca, y utiliza botones para enviar señales Bluetooth al dispositivo conectado.

El planteamiento del problema es lógico, pues a quien no le paso que desearia tener un dispositivo compacto independiente que pueda ayudarte a cambiar de diapositiva en tu presentación 🥲, sin la necesidad de presionar una tecla del computador, un puntero es una opcion, pero nada elegante, el reloj tendra un boton touch que con una palmada en la muñeca, la diapositiva avanzara, y ahora si quieres regresar, un boton análogo al costado de la pantalla se encargara de retroceder con cada pulsación. 

El proyecto esta orientado a la adaptación de un reloj clásico en un diseño impreso en 3D. Solo se realizo el diseño del circuito y la programación. 😁

## Funcionamiento 🔌

El reloj utiliza un Arduino Nano y un módulo Bluetooth HC-06 para la comunicación inalámbrica. Dos botones están conectados al Arduino para controlar las funciones "derecha" y "izquierda". Cuando se presiona un botón, el Arduino envía un carácter a través de Bluetooth al dispositivo emparejado, que puede ser interpretado por una aplicación en el dispositivo para realizar acciones específicas.
 ##Diseño del Circuito
 <div id="header" align="center">
  <img src="https://raw.githubusercontent.com/ValerioGomez/smart-clock/main/jugando.png" height="100%"/>
  <hr>
</div>
## Materiales Utilizados

- Arduino Nano
- Módulo Bluetooth HC-06
- Botones táctiles para las funciones "derecha" y "izquierda"
- Batería recargable para la alimentación del circuito
- Impresión 3D para crear una carcasa compacta para el reloj

## Diseño Compacto para la Muñeca ⌚

Se proporciona un diseño compacto para la carcasa del reloj que puede ser impreso en 3D. El diseño incluye espacio para alojar el Arduino, el módulo Bluetooth y la batería, así como botones accesibles para el usuario.

## Alternativa de Batería 🔋🪫

Se sugiere el uso de una batería recargable de litio de tamaño pequeño para alimentar el circuito. La capacidad de la batería dependerá de la duración deseada de funcionamiento entre recargas. imaginancion de cada quien ... 😅

## Versión II: Implementación de Inteligencia Artificial 😎

Para la versión II de este proyecto, se tiene previsto implementar inteligencia artificial para contrarrestar las pulsaciones no intencionadas del botón táctil al momento de la exposición. Esto se logrará mediante algoritmos de aprendizaje automático que identificarán y filtrarán las pulsaciones involuntarias, mejorando así la experiencia del usuario y la precisión del control del dispositivo conectado.

¡Diviértete creando tu propio reloj Bluetooth controlado por Arduino, que vean que parece magia 😁

