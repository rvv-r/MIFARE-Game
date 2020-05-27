import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry('1000x600')
fenetre.title("Test fenêtre graphique")

champ_label = tk.Label(fenetre, text="Choix des ports")
champ_label.pack()
OptionList = ["1","2","3","4","5","6"]


variable = tk.StringVar(fenetre)
variable.set(OptionList[0])

opt = tk.OptionMenu(fenetre, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack()
bouton_quitter = tk.Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack()
fenetre.mainloop()