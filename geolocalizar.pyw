import requests
import tkinter as tk
from tkinter import scrolledtext
import tkinter.font as tkFont
def fetch_data():
    ip_address = entry.get()
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    text_area.delete("1.0", tk.END) 
    if response.status_code == 200:
        data = response.json()
        for key, value in data.items():
            key=key.replace("city", "Ciudad").replace("query", "IP").replace("country", "Pais").replace("lat", "Latitud").replace("lon", "Longitud").replace("timezone", "Zona Horaria").replace("regionName", "Estado")
            if key == "zip" and value == "" or key == "isp" and value == "" or key == "org" and value == "":
             pass
            else:
             key=key.title()
             text_area.insert(tk.END, f"{key}: {value}\n")
    else:
        text_area.insert(tk.END, f"Error en la solicitud: {response.status_code}\n")
root = tk.Tk()
root.title("Geolocalizar IP Pública")
root.geometry("400x450")
font_style = tkFont.Font(family="Calibri", size=11)
label = tk.Label(root, text="Introduzca la IP:", font=font_style)
label.pack(pady=5)
entry = tk.Entry(root, width=30, font=font_style)
entry.pack(pady=5)
fetch_button = tk.Button(root, text="Obtener Datos", command=fetch_data, font=font_style)
fetch_button.pack(pady=10)
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=45, height=18, font=font_style)
text_area.pack(padx=10, pady=10)
root.mainloop()