from tkinter import *

window = Tk()
#config de la fenetre
window.title("BlueAi")
window.geometry("1080x720")
window.iconbitmap("./src/icon.ico")
window.config(background="#212121")

titre = Label(window, text="Bienvenue sur BlueBrain", font=("Futura",40), bg=("#212121"), fg=("white"))

titre.pack(expand=YES)
window.mainloop()
