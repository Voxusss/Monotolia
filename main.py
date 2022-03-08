import tkinter as tk
import random
from mapgen import arr
from tkinter import Text, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry
#Initialisation Tkinter
root = tk.Tk()
root.title("Monotolia / Tour Bleu")
#Déclaration des variables
redTurn = False
troops=[]
toDestroy=[]
clicked = False
Window = tk.Toplevel()
Window.title("Fenêtre d'infos")
canvas = tk.Canvas(Window, height=200, width=200)
canvas.pack()
frame1 = Frame(canvas)
frame1.pack(fill=X)
lbl1 = Label(frame1, text="Classe", width=6, font='Helvetica 12 bold')
lbl1.pack(side=LEFT, padx=5, pady=5)
frame2 = Frame(canvas)
frame2.pack(fill=X)
lbl2 = Label(frame2, text="HP : ", width=6)
lbl2.pack(side=LEFT, padx=5, pady=5)
def Set_Window(classe,hp):
    global lbl1
    global lbl2
    lbl1.config(text=classe)
    lbl2.config(text="HP : "+str(hp))
#Fonction RGB pour Tkinter
def rgb(rgb):
    return "#%02x%02x%02x" % rgb
#Création de la map
for i,row in enumerate(arr):
    for j,column in enumerate(row):
        if arr[i][j] == "*":
            color=rgb((24,92,21))
        elif arr[i][j] == "#":
            color=rgb((13,61,37))
        if arr[i][j] == "/":
            color=rgb((23,173,248))
        if arr[i][j] == "%":
            color=rgb((136,247,103))
        L = tk.Label(root,text='    ',bg=color)
        L.grid(row=i,column=j)
        L.bind('<Button-1>',lambda e, i=i,j=j: on_click(i,j,e))
lastPixel = root.winfo_children()[-1]

from sprites import (cavalierrouge,cavalierbleu,epeistebleu,epeisterouge,archerbleu,archerrouge,bateaubleu,bateaurouge, cb, cr)
#cliked = True quand l'user a cliqué sur une troop et la range s'affiche



#Chaque pixel est un bouton qui quand il est cliqué,
#apelle on_click avec ses coords i,j et le pixel: event
def on_click(i,j,event):
    global clicked
    global toDestroy
    clicked = False
    for i in toDestroy:
        i.destroy()
    print("Ceci Est la case", i,j)
  
#Chaque troupe est un bouton qui quand il est cliqué,
#apelle troop_click avec ses coords i,j et a troop: label



def troop_click(i,j,label):
  global clicked
  global toDestroy
  #On localise quelle troupe c'est dans la liste troops a partir du label
  if arr[i][j] == "*":
      curr_case = "Foret"
      print("La case est Foret")
  elif arr[i][j] == "#":
      curr_case = "Marecage"
      print("La case est Marécage")
  if arr[i][j] == "/":
      curr_case = "Eau"
      print("La case est Eau")
  if arr[i][j] == "%":
      curr_case = "Plaine"
      print("La case est Plaine")
  for b in troops:
      if b[0]==label:
          curr_index = troops.index(b)
  Set_Window(troops[curr_index][3], troops[curr_index][5])
  rangeList=[]
  if curr_case == "Marecage":
    rangeDico={"Epeiste":(-1,2), "Archer":(-1,2),"Cavalier":(-2,3),"Bateau":(-1,2) }
  elif curr_case == "Eau":
    rangeDico={"Epeiste":(-2,3), "Archer":(-2,3),"Cavalier":(-4,5),"Bateau":(-4,5) }
  else:
    rangeDico={"Epeiste":(-2,3), "Archer":(-2,3),"Cavalier":(-4,5),"Bateau":(-1,2) }
  for c in range(rangeDico[troops[curr_index][3]][0],rangeDico[troops[curr_index][3]][1]):
    for v in range(rangeDico[troops[curr_index][3]][0],rangeDico[troops[curr_index][3]][1]):
      rangeList.append((c,v))
  rangeList.remove((0,0))
  #Système d'attaque (pour l'instant c'est one shot)      
  if clicked and troops[curr_index][4]=="rouge" and redTurn == False:
    troops[curr_index]=(troops[curr_index][0],troops[curr_index][1],troops[curr_index][2],troops[curr_index][3],troops[curr_index][4],troops[curr_index][5]-5)
    clicked = False
    Set_Window(troops[curr_index][3], troops[curr_index][5])
    if troops[curr_index][5]<=0:
      label.destroy()
    for i in toDestroy:
        i.destroy()
  if clicked and troops[curr_index][4]=="bleu" and redTurn == True:
    troops[curr_index]=(troops[curr_index][0],troops[curr_index][1],troops[curr_index][2],troops[curr_index][3],troops[curr_index][4],troops[curr_index][5]-5)
    if troops[curr_index][5]<=0:
      label.destroy()
    clicked = False
    Set_Window(troops[curr_index][3], troops[curr_index][5])
    for i in toDestroy:
        i.destroy()
      
  if (redTurn and troops[curr_index][4] == "rouge") or (redTurn==False and troops[curr_index][4] == "bleu"):
    #Variables Globales
    curr_classe = troops[curr_index][3]
    #On a cliqué sur une troop donc clicked = true
    clicked = True
    #On enlève les potentiels pixels de range précédents
    for a in toDestroy:
      a.destroy()
    print("Clic sur une troupe en",i,j)
    toDestroy=[]
    #Création des pixels de range / On leur attribue un bouton qui apelle MoveTroop
    for pix in range(len(rangeList)):
      
      
      def make_lambda(x):
          return lambda ev:MoveTroop(curr_index,x)
      newLabel = tk.Label(root,text='    ',bg=rgb((28,28,16)), image=cb)
      newLabel.grid(row=i+rangeList[pix][0],column=j+rangeList[pix][1])
      toDestroy.append(newLabel)
      newLabel.bind('<Button-1>', make_lambda(rangeList[pix]))
      newLabel.lower()  
      newLabel.lift(lastPixel)
  

def placeTroop(i,j,classe,equipe):
  #Méthode à appeler au début de game ou achat d'une troop (prendra en compte la classe plus tard)
  print("Troop placed at ",i,j)
  if classe == "Archer":
    if equipe == 'rouge':
      L = tk.Label(root,text='    ',bg='black', image=archerrouge)
    else:
      L = tk.Label(root,text='',bg='black',image=archerbleu)
    
  elif classe == "Epeiste":
    if equipe == 'rouge':
      L = tk.Label(root,text='    ',bg='black', image=epeisterouge)
    else:
      L = tk.Label(root,text='',bg='black',image=epeistebleu)
  elif classe == "Bateau":
    if equipe == 'rouge':
      L = tk.Label(root,text='    ',bg='black', image=bateaurouge)
    else:
      L = tk.Label(root,text='',bg='black',image=bateaubleu)
  elif classe == "Cavalier":
    if equipe == 'rouge':
      L = tk.Label(root,text='    ',bg='black', image=cavalierrouge)
    else:
      L = tk.Label(root,text='',bg='black',image=cavalierbleu)
  L.grid(row=i,column=j)
  L.bind('<Button-1>',lambda e, i=i,j=j: troop_click(i,j,L))
  troops.append((L,i,j,classe,equipe,10))




def MoveTroop(i,dir):
  global clicked
  global redTurn
  #Méthode pour bouger une troop avec son index dans la liste troops et la direction
  curr_label = troops[i][0]
  curr_ipos = troops[i][1]
  curr_jpos = troops[i][2]
  sprite=""
  if troops[i][3] == "Archer":
    if troops[i][4] == "rouge":
      sprite = archerrouge
    else:
      sprite = archerbleu
  elif troops[i][3] == "Bateau":
    if troops[i][4] == "rouge":
      sprite = bateaurouge
    else:
      sprite = bateaubleu
  elif troops[i][3] == "Cavalier":
    if troops[i][4] == "rouge":
      sprite = cavalierrouge
    else:
      sprite = cavalierbleu
  elif troops[i][3] == "Epeiste":
    if troops[i][4] == "rouge":
      sprite = epeisterouge
    else:
      sprite = epeistebleu 
  imove=dir[0]
  jmove=dir[1]
  print(imove,jmove)
  newLabel = tk.Label(root,text='    ',bg='black',image=sprite)
  newLabel.grid(row=curr_ipos+imove,column=curr_jpos+jmove)
  newLabel.bind('<Button-1>',lambda e, i=curr_ipos+imove,j=curr_jpos+jmove: troop_click(i,j,newLabel))
  curr_label.destroy()
  troops[i] = (newLabel,curr_ipos+imove,curr_jpos+jmove,troops[i][3],troops[i][4],troops[i][5])
    
  global toDestroy
  clicked = False
  for i in toDestroy:
      i.destroy()  

  if redTurn == False:
    redTurn = True
    root.title("Monotolia / Tour Rouge")
  else:
    redTurn=False
    root.title("Monotolia / Tour Bleu")



    
#Génération de troupes de l'équipe bleu
troupededépart = ["Archer", "Archer", "Cavalier", "Epeiste", "Epeiste", "Bateau"]
for k in range(len(troupededépart)):
  icord = random.randint(5,15)
  jcord = random.randint(5,15)
  placeTroop(icord, jcord, troupededépart[k], "bleu")

#Génération de troupes de l'équipe rouge
for k in range(len(troupededépart)):
  icord = random.randint(30,40)
  jcord = random.randint(30,40)
  placeTroop(icord,jcord,troupededépart[k], "rouge")

#Loop tkinter
root.mainloop()
