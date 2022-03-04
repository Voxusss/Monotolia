import tkinter as tk
import random
from mapgen import arr

#Initialisation Tkinter
root = tk.Tk()
root.title("Monotolia / Tour Bleu")
redTurn = False
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
troops=[]

from sprites import (cavalierrouge,cavalierbleu,epeistebleu,epeisterouge,archerbleu,archerrouge,bateaubleu,bateaurouge, cb)
#cliked = True quand l'user a cliqué sur une troop et la range s'affiche
clicked = False
#les pixels montrant la range d'une troop sont toDestroy
toDestroy=[]

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
rangeList=[]
for c in range(-3,4):
  for v in range (-3,4):
    rangeList.append((c,v))
rangeList.remove((0,0))


def troop_click(i,j,label):
  #On localise quelle troupe c'est dans la liste troops a partir du label
  for b in troops:
      if b[0]==label:
          curr_index = troops.index(b)
  if (redTurn and troops[curr_index][4] == "rouge") or (redTurn==False and troops[curr_index][4] == "bleu"):
    #Variables Globales
    global clicked
    global toDestroy
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
      print("pixelc")
      newLabel = tk.Label(root,text='    ',bg=rgb((28,28,16)), image=cb)
      newLabel.grid(row=i+rangeList[pix][0],column=j+rangeList[pix][1])
      toDestroy.append(newLabel)
      newLabel.bind('<Button-1>', make_lambda(rangeList[pix]))
      newLabel.lower()  
      newLabel.lift(lastPixel)
      print('LFG')

  

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
  troops.append((L,i,j,classe,equipe))




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
  troops[i] = (newLabel,curr_ipos+imove,curr_jpos+jmove,troops[i][3],troops[i][4])
    
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
equipe = "bleu"
for k in range(len(troupededépart)):
  icord = random.randint(5,15)
  jcord = random.randint(5,15)
  placeTroop(icord, jcord, troupededépart[k], equipe)

#Génération de troupes de l'équipe rouge
equipe = "rouge"
for k in range(len(troupededépart)):
  icord = random.randint(30,40)
  jcord = random.randint(30,40)
  placeTroop(icord,jcord,troupededépart[k], equipe)

#Loop tkinter
root.mainloop()
