import tkinter as tk
from tkinter import messagebox
import urllib.request

class GameObject:
    def __init__(self, canvas, name, image, x, y, speed):
        try:
            self.canvas = canvas
            self.name = name
            self.image = tk.PhotoImage(file=f"./images/{image}")
            self.x = x
            self.y = y
            self.speed = speed
        except tk.TclError:
            messagebox.showerror("Error", f"No se pudo encontrar el archivo en ./images/{image}")    

    def set_image_from_file(self, image):
        self.image = tk.PhotoImage(file=f"./images/{image}")

    def set_image_from_url(self, url):
        """Descarga una imagen desde una URL y la asigna al objeto."""
        try:
            # Descargamos los datos de la imagen
            with urllib.request.urlopen(url) as response:
                data = response.read()
            # Creamos el PhotoImage usando el parámetro 'data' en lugar de 'file'
            self.image = tk.PhotoImage(data=data)
            
        except Exception as e:
            messagebox.showerror("Error de Red", f"No se pudo cargar la imagen desde la URL:\n{e}")

    def draw(self):
        self.canvas.create_image(self.x, self.y, image=self.image, anchor=tk.NW)

    def move_forward(self):
        self.y -= self.speed

    def move_backward(self):
        self.y += self.speed

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def scale_up(self):
        """Duplica el tamaño de la imagen actual (2x)."""
        self.image = self.image.zoom(2, 2)
        # Nota: Esto aumenta los píxeles, puede verse pixelado.

    def scale_down(self):
        """Reduce a la mitad el tamaño de la imagen actual (1/2)."""
        self.image = self.image.subsample(2, 2)

    def __repr__(self):
        return f"{self.name}:{self.x}:{self.y}"
