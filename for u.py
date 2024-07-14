import tkinter as tk
from tkinter import messagebox
import random
import webbrowser
import urllib.parse

whatsapp_number = "Your number"
pesan = "I want,"

def pindah_button(button):
    new_x = random.randint(0, window.winfo_width() - button.winfo_width())
    new_y = random.randint(0, window.winfo_height() - button.winfo_width())
    button.place(x=new_x, y=new_y)

def tekan_ya():
     messagebox.showinfo("Jawaban", "now you are my partner")
     buka_whatsapp()

def tekan_tidak():
     pindah_button(tidak_button)

def buka_whatsapp():
     encoded_message = urllib.parse.quote(pesan)
     webbrowser.open_new(f"https://api.whatsapp.com/send?phone=081287939099$text=test")

window = tk.Tk()
window.title("bisakah kita bersama lagi:)")
window.geometry("400x600")
window.configure(bg='#FFC0CB')

frame = tk.Frame(window, bg='#FFC0CB', bd=5)
frame.place(relx=0.5, rely=0.5, anchor='center')

label = tk.Label(frame, text="hai bisakah kita bersama lagi", font=("Helvetica",16, "bold"), bg='#FFC0CB', fg='#FF69B4', justify=tk.CENTER)
label.pack(pady=20)

ya_button = tk.Button(frame, text="Yes", Font=("Helvetica", 14), command=tekan_ya,
bg='#FF69B4', fg='white', width=8)
ya_button.pack(side=tk.LEFT, padx=10)

tidak_button = tk.Button(window, text="no", font=("Helvetica", 14), command=tekan_tidak,
bg='#FF69B4', fg='white', width=8)
tidak_button.place(x=50, y=50)

window.mainloop()