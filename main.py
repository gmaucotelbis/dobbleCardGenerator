#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from _tkinter import *
from Tkinter import *
import os



SCREEN_WIDTH=1920
SCREEN_HEIGHT=1080

fenetre=Tk()
leftPanel=Frame(fenetre,width=758,height=500,borderwidth=1)

leftPanel.pack(fill=BOTH)
listeImgParCarte=Listbox(leftPanel)
listeImgParCarte.insert(END,3)
listeImgParCarte.insert(END,4)
listeImgParCarte.insert(END,6)
listeImgParCarte.insert(END,8)
listeImgParCarte.insert(END,12)


listeImgParCarte.pack(side="top",fill=X)


fenetre.mainloop()
