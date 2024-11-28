import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación de Ejemplo con Tkinter")
root.geometry("400x300")  # Establece el tamaño de la ventana

# Función que se ejecuta al presionar el botón
def on_button_click():
    label.config(text="¡Has presionado el botón!")

# Crear la etiqueta (label)
label = tk.Label(root, text="¡Hola, esta es una aplicación con Tkinter!", font=("Arial", 14))
label.pack(pady=20)  # Agrega la etiqueta con un margen vertical

# Crear el botón
button = tk.Button(root, text="Presióname", command=on_button_click)
button.pack(pady=10)

# Crear el campo de entrada (entry)
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Función para actualizar la etiqueta con el texto ingresado
def update_label():
    name = entry.get()  # Obtener el texto de la entrada
    label.config(text=f"¡Hola, {name}!")

# Botón para actualizar el saludo
button_update = tk.Button(root, text="Actualizar saludo", command=update_label)
button_update.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()

