# A Simple Python Game with Pygame

## Descripción

Este es un ejemplo de un juego sencillo escrito en Python y la libreria PyGame. Este pequeño juego se desarrolló con el fin de motivar a los jovenes a descubir lo interesante que resulta ser el aprendizaje de la programación, y como se relacionan las instrucciones escritas con los efectos visuales en motores de juego simples.

## Instrucciones del juego

1. Se deben utilzar las flechas del teclado para escapar de los enemigos, entre más rápido se presionen las flechas para moverse, más posibilidades hay de escapar. 
2. Si el jugador es alcanzado por cualquiera de los enemigos la partida terminará'
3. La velocidad de los enemigos dependerá de la dificultad que escogida en el menú principal

## Librerias usadas

PyGame, PyGame-Menu

## Detalles sobre el código

### characters.py
1. La clase "Character" solo se define con el método "draw" para que el personaje aparezca en pantalla. 
2. La clase "Enemy" hereda de "Character" y define los métodos necesarios para que un enemigo pueda "perseguir" al jugador. Esto lo hace a través de hilos de procesamiento que crean el movimiento independiente de cada enemigo.
3. La clase "MainPlayer" hereda de "Character" y define los métodos necesarios para que el jugador pueda dezplazar el personaje.
4. Las clases "Zombie", "Witch" y "Bat" heredan de "Enemy" y representan los 3 enemigos que aparecen en la partida.

### config.py
1. La clase "Resources" define recursos como imágenes para el uso del juego
2. La clase "LoopStates" establece el estado del juego, por ejemplo, si el usuario está en el menú, viendo las instrucciones, jugando o si ha perdido la partida
3. La clase "CustomFonts" define los tipos de fuentes y tamaños usados en los textos
4. La clase "TextColors" define las tuplas con los valores RGB de los colores a usar en los textos.
5. La clase "Settings" define la resolución del juego y del menú principal

### game.py
En este archivo se define la dinámica general del juego a través de la clase "Game":

1. El método "run" le da inicio a la aplicación y muestra el menú
2. El método "play_game" se ejecuta al dar click en "Jugar" sobre el menú y renderiza al jugador y los enemigos
3. El método "game_over" se ejecuta cuando el jugador es alcanzado por uno de los enemigos y renderiza un contador en retroceso para regresar al menú
4. El método "show_instructions" se ejecuta al dar click en "Instrucciones" sobre el menú y muestra la descripción y el modo de juego.
5. El método "check_events" se ejecuta para leer la tecla "Escape" para volver al menú en cualquier situcación y al mismo tiempo determina las flechas usadas por el usuario para mover su personaje a través de la pantalla.

### main.py
Archivo principal para la ejecución del proyecto:
1. Instalar las librerias:
`pip install -r requirements.txt`
2. Ejecutar el juego:
`python main.py`