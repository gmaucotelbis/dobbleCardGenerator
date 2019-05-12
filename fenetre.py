from tkinter import tix
from tkinter import *
from tkinter.filedialog import *
import os

class Fenetre(Tk):

    def listSelected(evt):
        print("test")

    def __init__(self):
        fenetre=Tk()

        selected=0
        listValues=[3,4,6,8,12]

        labNCartes=Label(fenetre,text=self.textSelected(listValues,selected))
        labNCartes.grid(row=1,column=0)

        listSel = self.init_list(fenetre,selected,listValues,labNCartes)



        #listImgPerCard=Listbox(fenetre,values=listValues,dropdown=1,command=Fenetre.listSelected)
        #listeImgPerCard.pack()
        fenetre.mainloop()

    def init_list(self,fenetre,selected,listValues,labelCartes):

        yDefilB = Scrollbar(fenetre, orient='vertical')
        yDefilB.grid(row=0, column=1, sticky='ns')

        listSel = Listbox(fenetre,
            yscrollcommand=yDefilB.set,
            height=1)
        listSel.grid(row=0, column=0, sticky='nsew')
        yDefilB['command'] = listSel.yview
        for i in range(0,len(listValues)):
            listSel.insert(i,listValues[i])
        listSel.selection_set(0)
        return listSel

    def textSelected(self,listeValues,selected):
        return str(listeValues[selected])
