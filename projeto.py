from tkinter import *
from modulo_projeto import *



	


#GUI
root = Tk()
root['bg'] = 'green'
root.title('Cadastro de equipes')
root.iconbitmap('soccerball.ico')
root.state('zoomed')



#Widgets
label_titulo = Label(master = root,
	                 text = 'CADASTRO DE EQUIPES',
	                 font = 'Times 30',
	                 bg = 'green')

frame_cadastro = Frameinicial(parent = root) 



#Layout
label_titulo.pack()
frame_cadastro.place(x = 240, y = 130)

root.mainloop()
