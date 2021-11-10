import tkinter
import tkinter as tk
from doctest import master

class Contact():
    def __init__(self, nombre="",telefono="",correo=""):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def setName(self, nombre=""):
            self.nombre = nombre

    def setPhone(self, telefono=""):
        self.telefono = telefono

    def setMail(self, correo=""):
        self.correo = correo

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("Mi Lista de Contactos")
        self.rute = 'contact.dat'
        self.contactos = tk.Listbox(self.master)

        file = open(self.rute, 'r')
        with file as f:
            for linea in f:
                self.contactos.insert(self.contactos.size(), linea)
				
		
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.addBtn = tk.Button(self.master, text="Add", command=self.add)
        self.addBtn.grid(row=0, column=0, sticky="nsew")

        self.modBtn = tk.Button(self.master, text="Modify", command=self.modify)
        self.modBtn.grid(row=0, column=1, sticky="nsew")

        self.delBtn = tk.Button(self.master, text="Delete", command=self.delete)
        self.delBtn.grid(row=0, column=2, sticky="nsew")


        self.contactos.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.nameText = tk.StringVar()
        self.phoneText = tk.StringVar()
        self.mailText = tk.StringVar()

        self.labelName = tk.Label(self.master, text="Nombre :")
        self.labelName.grid(row=4, column=0)
        self.name = tk.Entry(self.master, textvariable=self.nameText, width=20)
        self.name.grid(row=4, column=1, columnspan=2, sticky="nsew")

        self.labelTelefono = tk.Label(self.master, text="Telefono :")
        self.labelTelefono.grid(row=5, column=0)
        self.telefono = tk.Entry(self.master, textvariable=self.phoneText, width=20)
        self.telefono.grid(row=5, column=1, columnspan=2, sticky="nsew")

        self.labelCorreo = tk.Label(self.master, text="Correo :")
        self.labelCorreo.grid(row=6, column=0)
        self.correo = tk.Entry(self.master, textvariable=self.mailText, width=20)
        self.correo.grid(row=6, column=1, columnspan=2, sticky="nsew")

        self.saveBtn = tk.Button(self.master, text="Save", command=self.save)
        self.saveBtn.grid(row=7, column=0, columnspan=3, sticky="nsew")

    def add(self):
        print("hola")
        self.contactos.insert(self.contactos.size(), self.name.get()+"#"+self.telefono.get()+"#"+self.correo.get())

    def modify(self):

        self.contactos.delete(self.contactos.curselection())
        self.contactos.insert(self.contactos.size(),
                              self.name.get() + "#" + self.telefono.get() + "#" + self.correo.get())
    def delete(self):
        self.contactos.delete(self.contactos.curselection())
    def save(self):
        contactosString = ""
        for x in range(0, self.contactos.size()):
            contactosString += self.contactos.get(x) + "\n"
		
        with open(self.rute, 'w') as f: f.write(contactosString)


root = tk.Tk()
app = Application(master=root)
app.mainloop()