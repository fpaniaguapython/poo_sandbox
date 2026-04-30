import tkinter as tk
from tkinter import messagebox
from game_object import GameObject

game_objects=[]

def draw_scene():
    canvas.delete("all")
    for game_object in game_objects:
        game_object.draw()
    show_game_objects_info()
    
def show_game_objects_info():
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, "Game objects:\n")
    output_text.insert(tk.END, game_objects)
    output_text.insert(tk.END, "\n")
    output_text.config(state=tk.DISABLED)

def execute_code():
    """Obtiene el código del área de texto y simula su ejecución."""
    code_content = code_text.get("1.0", tk.END).strip()
    if not code_content:
        messagebox.showwarning("Advertencia", "El área de código está vacía.")
        return
    
    # Ejecuta el código
    try:
        exec(code_content, globals())
    except Exception as e:
        messagebox.showerror("Error", "Se ha producido un error:"+str(e))

    # Edita la caja de texto de salida
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"Ejecutando:\n{code_content}\n")
    output_text.config(state=tk.DISABLED)
    
    draw_scene()
    show_game_objects_info()
    
    
def reset_sandbox():
    """Limpia todas las áreas de la aplicación."""
    code_text.delete("1.0", tk.END)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)
    canvas.delete("all")
    print("Sandbox reiniciado")


# Configuración de la ventana principal
root = tk.Tk()
root.title("Python Sandbox IDE")
root.geometry("900x600")

# --- MENÚ ---
menu_bar = tk.Menu(root)

# Menú Archivo
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

# --- DISTRIBUCIÓN DE PANTALLA ---

# Lado Izquierdo
canvas = tk.Canvas(root, bg="white", highlightbackground="gray", relief=tk.SUNKEN)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

# Lado Derecho
right_frame = tk.Frame(root, width=400) # Definimos el ancho inicial aquí
right_frame.pack_propagate(False)       # ¡IMPORTANTE! Evita que el frame se encoja
right_frame.pack(side=tk.RIGHT, fill=tk.Y, expand=False, padx=5, pady=5)

# Etiqueta y área de Code
tk.Label(right_frame, text="Code:", font=("Arial", 10, "bold")).pack(anchor=tk.W)
code_text = tk.Text(right_frame, height=15, font=("Consolas", 10))
code_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

# Etiqueta y área de Output
tk.Label(right_frame, text="Output:", font=("Arial", 10, "bold")).pack(anchor=tk.W)
output_text = tk.Text(right_frame, height=10, bg="#f0f0f0", state=tk.DISABLED, font=("Consolas", 10))
output_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

# Botón Ejecutar
btn_execute = tk.Button(right_frame, text="Ejecutar", command=execute_code, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
btn_execute.pack(fill=tk.X, pady=5)

# Creación de objetos del juego
bg = GameObject(canvas, 'bg', 'bg.png', 0, 0, 0)
spaceship_1 = GameObject(canvas, 'spaceship_1', 'spaceship.png', 100, 100, 1)
spaceship_2 = GameObject(canvas, 'spaceship_2', 'spaceship.png', 200, 200, 1)
game_objects.append(bg)
game_objects.append(spaceship_1)
game_objects.append(spaceship_2)

# Dibujado de escena
draw_scene()

root.mainloop()