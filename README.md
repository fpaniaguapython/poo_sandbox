# POO SANDBOX

### Instanciar GameObject:

Nota: es útil darle como nombre el mismo nombre de la variable.

GameObject(canvas, nombre, nombre_fichero, x, y, speed)

    spaceship_1 = GameObject(canvas, 'spaceship_1',  'spaceship.png', 100, 100, 1)


### Añadir el GameObject a la lista de objetos del juego:

    game_objects.append(spaceship_1)

### Métodos de GameObject:

    - move_forward()
    - move_backward()
    - move_left()
    - move_right()
    - scale_up()
    - scale_down()
    - set_image(nombre_fichero_png)

### Inicialmente existen los objetos siguientes:
    - spaceship_1
    - spaceship_2

