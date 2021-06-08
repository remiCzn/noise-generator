from tkinter import *
from random import randrange
from perlin_noise import PerlinNoise

haut = 200
larg = 200
cote = 3

layers = 3
scale = 7

void = 1
solid = 0
wall = 2

cell = [[0 for row in range(haut)] for col in range(larg)]
etat = [[solid for row in range(haut)] for col in range(larg)]

def init():
    generateNoise()
    delete_thick_walls()
    delete_thick_walls()
    draw_wall()
    

def generateNoise():
    noises = []
    for x in range(layers):
        noises.append(PerlinNoise(octaves = scale * pow(2, x)))

    for y in range(haut):
        for x in range(larg):
            noise = 0
            for i in range(layers):
                noise += noises[i]([x/larg, y/haut]) * pow(0.5, i)

            if(noise > 0):
                etat[x][y] = solid
            else:
                etat[x][y] = void

def delete_thick_walls():
    for y in range(haut):
        for x in range(larg):
            if(y>0 and y<haut-1 and etat[x][y-1] == void and etat[x][y+1] == void):
                etat[x][y] = void

            if(x>0 and x < larg-1 and etat[x-1][y] == void and etat[x+1][y] == void):
                etat[x][y] = void

def draw_wall():
    for y in range(haut):
        for x in range(larg):
            if(y > 0 and y < haut - 1 and etat[x][y] == solid):
                if etat[x][y+1] == void:
                    etat[x][y] = wall
            cell[x][y] = canvas.create_rectangle((x*cote, y*cote, (x+1)*cote, (y+1)*cote), outline="", fill="white")

def dessiner():
    for y in range(haut):
        for x in range(larg):
            if etat[x][y]==void:
                coul = "bisque"
            elif etat[x][y] == solid:
                coul = "black"
            else:
                coul = "brown"
            canvas.itemconfig(cell[x][y], fill=coul)

fenetre = Tk()
fenetre.title("Noise map")
canvas = Canvas(fenetre, width=cote * larg, height = cote*haut, highlightthickness = 0)
canvas.pack()
init()
dessiner()
fenetre.mainloop()