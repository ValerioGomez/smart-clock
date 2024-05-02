import tkinter as tk
import bluetooth
import threading
import pyautogui
#instalar bibliotecas bluetooth y pyautogui

def conectar_dispositivo():
    global dispositivo_conectado, socket
    try:
        direccion = direccion_entry.get()
        socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        socket.connect((direccion, 1))
        dispositivo_conectado = True
        estado_label.config(text="Conectado", fg="green")
        # Iniciar hilo para recibir datos
        threading.Thread(target=recibir_datos).start()
    except Exception as e:
        print(e)
        estado_label.config(text="Desconectado", fg="red")

def desconectar_dispositivo():
    global dispositivo_conectado, socket
    try:
        socket.close()
        dispositivo_conectado = False
        estado_label.config(text="Desconectado", fg="red")
    except Exception as e:
        print(e)

def recibir_datos():
    while True:
        if dispositivo_conectado:
            try:
                data = socket.recv(1024)
                if data:#aqui se usa biblioteca, cabalelros
                    decoded_data = data.decode()
                    if decoded_data == "A":
                        # Presionar tecla derecha (código ASCII 39)
                        pyautogui.press('right')
                        print("Tecla Derecha presionada")
                    elif decoded_data == "B":
                        # Presionar tecla izquierda (código ASCII 37)
                        pyautogui.press('left')
                        print("Tecla Izquierda presionada")
            except Exception as e:
                print(e)

app = tk.Tk()
app.title("Aplicación Bluetooth")

direccion_label = tk.Label(app, text="Dirección del dispositivo:")
direccion_label.pack()
direccion_entry = tk.Entry(app)
direccion_entry.pack()

conectar_button = tk.Button(app, text="Conectar", command=conectar_dispositivo)
conectar_button.pack()

desconectar_button = tk.Button(app, text="Desconectar", command=desconectar_dispositivo)
desconectar_button.pack()

estado_label = tk.Label(app, text="Desconectado", fg="red")
estado_label.pack()

# Variable global para verificar si el dispositivo está conectado
dispositivo_conectado = False

app.mainloop()
