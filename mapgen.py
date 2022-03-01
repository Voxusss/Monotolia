#Imports
import numpy as np
import sys
from scipy.ndimage.interpolation import zoom

#Longueur d'un côté de map
mapsize=60
np.set_printoptions(threshold=sys.maxsize)
#Creation d'une array random avec Numpy
arr = np.random.uniform(size=(6,6))
#Zoom dans l'array pour obtenir un truc smooth
arr = zoom(arr, 10)
#Transformation de l'array Numpy en liste python
arr = arr.tolist()
#En fonction de la valeur random, on donne un signe qui est utilisé pour les biomes dans le gui
for z in arr:
    for count, value in enumerate(z):
        if value < 0.2:
            z[count] = "*"
        elif value < 0.4:
            z[count]  = "#"
        elif value < 0.6:
            z[count]  = "/"
        else:
            z[count]  = "%"
