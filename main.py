import tkinter as tk
from PIL import ImageTk, Image
from mapgen import arr
import time

#Initialisation Tkinter
root = tk.Tk()
cb = Image.open("static/carrejaune.png")
cb = ImageTk.PhotoImage(cb)
archerbleu = Image.open("static/ArcherBlueSide.png")
archerbleu = ImageTk.PhotoImage(archerbleu)


archerrouge = Image.open("static/ArcherRedSide.png")
archerrouge = ImageTk.PhotoImage(archerrouge)
#cliked = True quand l'user a cliqué sur une troop et la range s'affiche
clicked = False
#les pixels montrant la range d'une troop sont toDestroy
toDestroy=[]
#Fonction RGB pour Tkinter
def rgb(rgb):
    return "#%02x%02x%02x" % rgb
#Chaque pixel est un bouton qui quand il est cliqué,
#apelle on_click avec ses coords i,j et le pixel: event
def on_click(i,j,event):
    global clicked
    global toDestroy
    clicked = False
    for i in toDestroy:
        i.destroy()
    """"
    color = "red"
    event.widget.config(bg=color)
    L = tk.Label(root,text='    ',bg='red')
    L.grid(row=i,column=j+1)
    L = tk.Label(root,text='    ',bg='red')
    L.grid(row=i,column=j-1)
    L = tk.Label(root,text='    ',bg='red')
    L.grid(row=i+1,column=j)
    L = tk.Label(root,text='    ',bg='red')
    L.grid(row=i-1,column=j)
    """
    print("Ceci Est la case", i,j)
  
#Chaque troupe est un bouton qui quand il est cliqué,
#apelle troop_click avec ses coords i,j et a troop: label
def troop_click(i,j,label):
  #Variables Globales
  global clicked
  global toDestroy
  #On localise quelle troupe c'est dans la liste troops a partir du label
  for b in troops:
      if b[0]==label:
          curr_index = troops.index(b)
  #On a cliqué sur une troop donc clicked = true
  clicked = True
  #On enlève les potentiels pixels de rnage précédents
  for a in toDestroy:
    a.destroy()
  print("Clic sur une troupe en",i,j)
  toDestroy=[]
  #Création des pixels de range / On leur attribue un bouton qui apelle MoveTroop
  newLabel = tk.Label(root,text='    ',bg=rgb((28,28,16)), image=cb)
  newLabel.grid(row=i+1,column=j)
  toDestroy.append(newLabel)
  newLabel.bind('<Button-1>',lambda e, i=i,j=j: MoveTroop(curr_index,"DOWN"))

  newLabel = tk.Label(root,text='    ',bg=rgb((28,28,16)), image=cb)
  newLabel.grid(row=i-1,column=j)
  toDestroy.append(newLabel)
  newLabel.bind('<Button-1>',lambda e, i=i,j=j: MoveTroop(curr_index,"UP"))

  newLabel = tk.Label(root,text='    ',bg=rgb((28,28,16)), image=cb)
  newLabel.grid(row=i,column=j+1)
  toDestroy.append(newLabel)
  newLabel.bind('<Button-1>',lambda e, i=i,j=j: MoveTroop(curr_index,"RIGHT"))

  newLabel = tk.Label(root,text='    ',bg=rgb((28,28,16)), image=cb)
  newLabel.grid(row=i,column=j-1)
  toDestroy.append(newLabel)
  newLabel.bind('<Button-1>',lambda e, i=i,j=j: MoveTroop(curr_index,"LEFT"))

  newLabel = tk.Label(root,text='    ',bg=rgb((28,28,16)), image=cb)
  newLabel.grid(row=i-1, column=j+1)
  toDestroy.append(newLabel)
  newLabel.bind('<Button-1>',lambda e, i=i, j=j: MoveTroop(curr_index, "TOP_RIGHT"))

  newLabel = tk.Label(root,text='    ',bg=rgb((28,28,16)), image=cb)
  newLabel.grid(row=i-1, column=j-1)
  toDestroy.append(newLabel)
  newLabel.bind('<Button-1>',lambda e, i=i, j=j: MoveTroop(curr_index, "TOP_LEFT"))

  newLabel = tk.Label(root,text='    ',bg=rgb((28,28,16)), image=cb)
  newLabel.grid(row=i+1, column=j-1)
  toDestroy.append(newLabel)
  newLabel.bind('<Button-1>',lambda e, i=i, j=j: MoveTroop(curr_index, "BOTTOM_LEFT"))

  newLabel = tk.Label(root,text='    ',bg=rgb((28,28,16)), image=cb)
  newLabel.grid(row=i+1, column=j+1)
  toDestroy.append(newLabel)
  newLabel.bind('<Button-1>',lambda e, i=i, j=j: MoveTroop(curr_index, "BOTTOM_RIGHT"))
  
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

troops=[]

def placeTroop(i,j):
  #Méthode à appeler au début de game ou achat d'une troop (prendra en compte la classe plus tard)
  print("Troop placed at ",i,j)
  L = tk.Label(root,text='    ',bg='black', image=archerbleu)
  L.grid(row=i,column=j)
  L.bind('<Button-1>',lambda e, i=i,j=j: troop_click(i,j,L))
  troops.append((L,i,j))




def MoveTroop(i,dir):
  global clicked
  #Méthode pour bouger une troop avec son index dans la liste troops et la direction
  curr_label = troops[i][0]
  curr_ipos = troops[i][1]
  curr_jpos = troops[i][2]
  if dir=="UP":
    newLabel = tk.Label(root,text='    ',bg='red')
    newLabel.grid(row=curr_ipos-1,column=curr_jpos)
    newLabel.bind('<Button-1>',lambda e, i=curr_ipos-1,j=curr_jpos: troop_click(i,j,newLabel))
    curr_label.destroy()
    troops[i] = (newLabel,curr_ipos-1,curr_jpos)
  if dir=="DOWN":
    newLabel = tk.Label(root,text='    ',bg='red')
    newLabel.grid(row=curr_ipos+1,column=curr_jpos)
    newLabel.bind('<Button-1>',lambda e, i=curr_ipos+1,j=curr_jpos: troop_click(i,j,newLabel))
    curr_label.destroy()
    troops[i] = (newLabel,curr_ipos+1,curr_jpos)
  if dir=="LEFT":
    newLabel = tk.Label(root,text='    ',bg='red')
    newLabel.grid(row=curr_ipos,column=curr_jpos-1)
    newLabel.bind('<Button-1>',lambda e, i=curr_ipos,j=curr_jpos-1: troop_click(i,j,newLabel))
    curr_label.destroy()
    troops[i] = (newLabel,curr_ipos,curr_jpos-1)
  if dir=="RIGHT":
    newLabel = tk.Label(root,text='    ',bg='red')
    newLabel.grid(row=curr_ipos,column=curr_jpos+1)
    newLabel.bind('<Button-1>',lambda e, i=curr_ipos,j=curr_jpos+1: troop_click(i,j,newLabel))
    curr_label.destroy()
    troops[i] = (newLabel,curr_ipos,curr_jpos+1)

  if dir=="TOP_RIGHT":
    newLabel = tk.Label(root,text='    ',bg="red")
    newLabel.grid(row=curr_ipos-1,column=curr_jpos+1)
    newLabel.bind('<Button-1>', lambda e, i=curr_ipos-1,     j=curr_jpos+1:troop_click(i, j, newLabel))
    curr_label.destroy()
    troops[i] = (newLabel, curr_ipos-1, curr_jpos+1)

  if dir=="TOP_LEFT":
    newLabel = tk.Label(root,text='    ',bg="red")
    newLabel.grid(row=curr_ipos-1,column=curr_jpos-1)
    newLabel.bind('<Button-1>', lambda e, i=curr_ipos-1,     j=curr_jpos-1:troop_click(i, j, newLabel))
    curr_label.destroy()
    troops[i] = (newLabel, curr_ipos-1, curr_jpos-1)

  if dir=="BOTTOM_LEFT":
    newLabel = tk.Label(root,text='    ',bg="red")
    newLabel.grid(row=curr_ipos+1,column=curr_jpos-1)
    newLabel.bind('<Button-1>', lambda e, i=curr_ipos+1,     j=curr_jpos-1:troop_click(i, j, newLabel))
    curr_label.destroy()
    troops[i] = (newLabel, curr_ipos+1, curr_jpos-1)

  if dir=="BOTTOM_RIGHT":
    newLabel = tk.Label(root,text='    ',bg="red")
    newLabel.grid(row=curr_ipos+1,column=curr_jpos+1)
    newLabel.bind('<Button-1>', lambda e, i=curr_ipos+1,     j=curr_jpos+1:troop_click(i, j, newLabel))
    curr_label.destroy()
    troops[i] = (newLabel, curr_ipos+1, curr_jpos+1)
  
  global toDestroy
  clicked = False
  for i in toDestroy:
      i.destroy()  


#Tests
placeTroop(5,5)
placeTroop(10,10)
placeTroop(15,15)
placeTroop(7,9)
placeTroop(12,10)

#Loop tkinter
root.mainloop()
