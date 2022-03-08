from PIL import ImageTk, Image

#Ouverture des sprites e transformations en objets avec une méthode Tkinter pour les rendre utilisables par la suite dans le jeu

cb = Image.open("static/carrejaune.png")
cb = ImageTk.PhotoImage(cb)
cr = Image.open("static/CarréRose.png")
cr = ImageTk.PhotoImage(cr)

archerbleu = Image.open("static/ArcherBlueSide.png")
archerbleu = ImageTk.PhotoImage(archerbleu)
archerrouge= Image.open("static/ArcherRedSide.png")
archerrouge = ImageTk.PhotoImage(archerrouge)

epeistebleu = Image.open("static/EpeisteBlueSide.png")
epeistebleu = ImageTk.PhotoImage(epeistebleu)
epeisterouge = Image.open("static/EpeisteRedSide.png")
epeisterouge = ImageTk.PhotoImage(epeisterouge)

bateaubleu = Image.open("static/BateauBlueSide.png")
bateaubleu = ImageTk.PhotoImage(bateaubleu)
bateaurouge = Image.open("static/BateauRedSide.png")
bateaurouge = ImageTk.PhotoImage(bateaurouge)

cavalierbleu = Image.open("static/CavalierBlueSide.png")
cavalierbleu = ImageTk.PhotoImage(cavalierbleu)
cavalierrouge = Image.open("static/CavalierRedSide.png")
cavalierrouge = ImageTk.PhotoImage(cavalierrouge)