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
    - set_image_from_file(nombre_fichero_png)
    - set_image_from_url(url_fichero_png) # Puede no funcionar con algunos formatos.

### Inicialmente existen los objetos siguientes:
    - bg
    - spaceship_1
    - spaceship_2

<img width="902" height="652" alt="image" src="https://github.com/user-attachments/assets/36dd7d68-e849-426a-841c-54202032765c" />


<img width="902" height="652" alt="image" src="https://github.com/user-attachments/assets/c8e4030a-d839-4b10-bbe8-ae7ad5859d03" />



