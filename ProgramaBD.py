from tkinter import *
from tkinter import messagebox
import sqlite3	

raiz=Tk()
raiz.title("Mi primer programa")
raiz.resizable(width=False, height=False)

miframe=Frame(raiz)
miframe.pack()



#------------FUNCION BARRA DE HERRAMIENTAS
#------------------------BBDD
def salirapp():
	valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")

	if valor==True:
		raiz.destroy()

def conectarbbdd():
	global basededatos
	
	miconexion=sqlite3.connect("PrimeraBase")
	micursor=miconexion.cursor()
	

	try:
		micursor.execute('''
			CREATE TABLE REGISTROS (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE VARCHAR(50),
			PASSWORD VARCHAR(50),
			APELLIDO VARCHAR(20),
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(400))
			''')
		messagebox.showinfo(message="Base de datos creada con éxito.", title="Base de datos.")
				
		
		
	except:
		messagebox.showwarning(message="Ya existe una base de datos", title="Atencion!")
					
	
	


#------------------------BORRAR

def borrarcampos():
	pantallaid.set("")
	pantallanomb.set("")
	pantallapass.set("")
	pantallaapel.set("")
	pantalladirec.set("")
	cuadrocomen.delete('1.0', END)


#------------------------CRUD

def crudcrear():


	regpersonas=[pantallanomb.get(),pantallapass.get(),pantallaapel.get(),pantalladirec.get(),cuadrocomen.get('1.0', END)]
	miconexion=sqlite3.connect("PrimeraBase")
	micursor=miconexion.cursor()
	micursor.execute("INSERT INTO REGISTROS VALUES(NULL,?,?,?,?,?)", regpersonas)		
	miconexion.commit()
	messagebox.showinfo(message="Se agregó el registro con éxito.")
	pantallaid.set("")
	pantallanomb.set("")
	pantallapass.set("")
	pantallaapel.set("")
	pantalladirec.set("")
	cuadrocomen.delete('1.0', END)

	
		

def crudleer():
	
	
	cuadrocomen.delete('1.0', END)
	miconexion=sqlite3.connect("PrimeraBase")
	micursor=miconexion.cursor()
	micursor.execute("SELECT * FROM REGISTROS WHERE ID=" + pantallaid.get())
	resultado=micursor.fetchall()
	for datos in resultado:
		pantallanomb.set(datos[1])
		pantallapass.set(datos[2])
		pantallaapel.set(datos[3])
		pantalladirec.set(datos[4])
		cuadrocomen.insert(1.0,datos[5])

	miconexion.commit()
	


def crudactualizar():
	miconexion=sqlite3.connect("PrimeraBase")
	micursor=miconexion.cursor()
	micursor.execute("UPDATE REGISTROS SET NOMBRE='" + pantallanomb.get() +
		"', PASSWORD='" + pantallapass.get() +
		"', APELLIDO='" + pantallaapel.get() +
		"', DIRECCION='" + pantalladirec.get() +
		"', COMENTARIOS='" + cuadrocomen.get('1.0', END) +
		"' WHERE ID=" + cuadroid.get())
	miconexion.commit()
	messagebox.showinfo(message="Datos actualizados con éxito.", title="Update")

def crudborrar():
	valor=messagebox.askokcancel("ATENCION", "¿Deseas eliminar este registro?")

	if valor==True:
		
		miconexion=sqlite3.connect("PrimeraBase")
		micursor=miconexion.cursor()
		micursor.execute("DELETE FROM REGISTROS WHERE ID=" + pantallaid.get())
		miconexion.commit()
		messagebox.showinfo(message="Usuario eliminado.", title="Borrar registros.")


#------------------------AYUDA	

def infoapp():
	messagebox.showinfo(message="linkedin.com/in/alanferrari95/", title="Programa de prueba")

def acercade():
	messagebox.showinfo(message="Programa creado por Alan Ferrari.")


#------------BARRA DE HERRAMIENTAS
barramenu=Menu(raiz)
raiz.config(menu=barramenu)

bbddbh=Menu(barramenu, tearoff=0)
bbddbh.add_command(label="Conectar", command=conectarbbdd)
bbddbh.add_command(label="Salir", command=salirapp)

borrarbh=Menu(barramenu, tearoff=0)
borrarbh.add_command(label="Borrar campos", command=borrarcampos)

curdbh=Menu(barramenu, tearoff=0)
curdbh.add_command(label="Crear", command=crudcrear)
curdbh.add_command(label="Leer", command=crudleer)
curdbh.add_command(label="Actualizar", command=crudactualizar)
curdbh.add_command(label="Borrar", command=crudborrar)


ayudabh=Menu(barramenu, tearoff=0)
ayudabh.add_command(label="Licencia", command=acercade)
ayudabh.add_command(label="Acerca de", command=infoapp)

barramenu.add_cascade(label="BBDD", menu=bbddbh)
barramenu.add_cascade(label="Borrar", menu=borrarbh)
barramenu.add_cascade(label="CRUD", menu=curdbh)
barramenu.add_cascade(label="Ayuda", menu=ayudabh)


#------------ID
pantallaid=StringVar()
idlabel=Label(miframe, text="ID:", font=("Arial", 11))
idlabel.grid(row=0, column=0, sticky="w", padx=15, pady=5)
cuadroid=Entry(miframe, textvariable=pantallaid)
cuadroid.grid(row=0, column=2, padx=5, pady=5)



#------------NOMBRE
pantallanomb=StringVar()
nombrelabel=Label(miframe, text="Nombre:", font=("Arial", 11))
nombrelabel.grid(row=1, column=0, sticky="w", padx=15, pady=5)
cuadronombre=Entry(miframe, textvariable=pantallanomb)
cuadronombre.grid(row=1, column=2, padx=5, pady=5)


#------------PASSWORD
pantallapass=StringVar()
passlabel=Label(miframe, text="Password:", font=("Arial", 11))
passlabel.grid(row=2, column=0, sticky="w", padx=15, pady=5)
cuadropass=Entry(miframe, textvariable=pantallapass)
cuadropass.grid(row=2, column=2, padx=5, pady=5)
cuadropass.config(show="*")



#------------APELLIDO
pantallaapel=StringVar()
apellidolabel=Label(miframe, text="Apellido:", font=("Arial", 11))
apellidolabel.grid(row=3, column=0, sticky="w", padx=15, pady=5)
cuadroapellido=Entry(miframe, textvariable=pantallaapel)
cuadroapellido.grid(row=3, column=2, padx=5, pady=5)


#------------DIRECCION
pantalladirec=StringVar()
direclabel=Label(miframe, text="Dirección:", font=("Arial", 11))
direclabel.grid(row=4, column=0, sticky="w", padx=15, pady=5)
cuadrodirec=Entry(miframe, textvariable=pantalladirec)
cuadrodirec.grid(row=4, column=2, padx=5, pady=5)



#------------COMENTARIO
comenlabel=Label(miframe, text="Comentarios:", font=("Arial", 11))
comenlabel.grid(row=5, column=0, sticky="w", padx=15, pady=5)
cuadrocomen=Text(miframe, width=15, height=8)
cuadrocomen.grid(row=5, column=2, padx=5, pady=5)
scroll=Scrollbar(miframe, command=cuadrocomen.yview)
scroll.grid(row=5, column=4, sticky="nsew")
cuadrocomen.config(yscrollcommand=scroll.set)


#------------FUNCION DE BOTONES
def create():
	
	regpersonas=[pantallanomb.get(),pantallapass.get(),pantallaapel.get(),pantalladirec.get(),cuadrocomen.get('1.0', END)]
	miconexion=sqlite3.connect("PrimeraBase")
	micursor=miconexion.cursor()
	micursor.execute("INSERT INTO REGISTROS VALUES(NULL,?,?,?,?,?)", regpersonas)		
	miconexion.commit()
	messagebox.showinfo(message="Se agregó el registro con éxito.")
	pantallaid.set("")
	pantallanomb.set("")
	pantallapass.set("")
	pantallaapel.set("")
	pantalladirec.set("")
	cuadrocomen.delete('1.0', END)

def read():

	cuadrocomen.delete('1.0', END)
	miconexion=sqlite3.connect("PrimeraBase")
	micursor=miconexion.cursor()
	micursor.execute("SELECT * FROM REGISTROS WHERE ID=" + pantallaid.get())
	resultado=micursor.fetchall()
	for datos in resultado:
		pantallanomb.set(datos[1])
		pantallapass.set(datos[2])
		pantallaapel.set(datos[3])
		pantalladirec.set(datos[4])
		cuadrocomen.insert(1.0,datos[5])

	miconexion.commit()

def update():
	miconexion=sqlite3.connect("PrimeraBase")
	micursor=miconexion.cursor()
	micursor.execute("UPDATE REGISTROS SET NOMBRE='" + pantallanomb.get() +
		"', PASSWORD='" + pantallapass.get() +
		"', APELLIDO='" + pantallaapel.get() +
		"', DIRECCION='" + pantalladirec.get() +
		"', COMENTARIOS='" + cuadrocomen.get('1.0', END) +
		"' WHERE ID=" + cuadroid.get())
	miconexion.commit()
	messagebox.showinfo(message="Datos actualizados con éxito.", title="Update")


def delete():
	valor=messagebox.askokcancel("ATENCION", "¿Deseas eliminar este registro?")

	if valor==True:
		
		miconexion=sqlite3.connect("PrimeraBase")
		micursor=miconexion.cursor()
		micursor.execute("DELETE FROM REGISTROS WHERE ID=" + pantallaid.get())
		miconexion.commit()
		messagebox.showinfo(message="Usuario eliminado.", title="Borrar registros.")


#------------BOTONES

miframe2=Frame(raiz)
miframe2.pack()

botoncreate=Button(miframe2, text="Create", command=create)
botoncreate.grid(row=6, column=0, padx=15, pady=5)

botonread=Button(miframe2, text="Read", command=read)
botonread.grid(row=6, column=1, padx=5, pady=5)

botonupdate=Button(miframe2, text="Update", command=update)
botonupdate.grid(row=6, column=2, padx=15, pady=5)

botondelete=Button(miframe2, text="Delete", command=delete)
botondelete.grid(row=6, column=3, padx=5, pady=5)





raiz.mainloop()
