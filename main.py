from tkinter import *

window = Tk()
#config de la fenetre
window.title("BlueAi")
window.geometry("1080x720")
window.iconbitmap("./src/icon.ico")
window.config(background="#212121")

titleContainer = Frame(window,bg="#212121")

titre = Label(titleContainer, text="Bienvenue sur BlueBrain", font=("Futura",40), bg=("#212121"), fg=("white"))
titre.pack()


startButton = Button(titleContainer, text="Commencer", font=("Futura",20), bg=("#0074D9"), fg=("white"), relief="solid", borderwidth=0, highlightthickness=10)
startButton.pack()
titleContainer.pack(expand=YES)
window.mainloop()
