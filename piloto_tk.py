from tkinter import *
from tkinter import ttk

condicoes = {
        'Pressão Arterial': 0, 
        'Frequência Cardíaca':0, 
        'Frequência Respiratória': 0, 
        'Saturação de Oxigênio': 0, 
        'Monitor ECG' : 'Fibrilação Ventricular',
        'Conciencia' : 'Inconsciente'
        }
Procedimentos = ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Desfibrilação", "Toracocentese de alívio", "Pericardiocentese", "Intubação orotraqueal"]
Medicações = ["Adrenalina", "Amiodarona", "Sulfato de magnésio", "Glucanato de cálcio", "Glico-insulina", "Bicarbonato de sódio", "Soro fisiológico", "Ringer lactato", "Cloreto de potássio"]

listona = [Procedimentos, Medicações]

#def mudarTexto(event):
#    if self.msg["text"] == "Sei lá":
#        self.msg["text"] = "O botão recebeu um clique"
#    else:
#        self.msg["text"] = "Sei lá"
#app = Tk()
#
#frm = ttk.Frame(app, padding = 10)
#frm.grid()
#ttk.Label(frm, text='Hello World').grid(column=0, row = 0)
#ttk.Button(frm, text='Destoy', command=app.destroy).grid(column=1, row =0)
#ttk.Button(frm, text='Teste' ).grid(column=2, row =0)
#teste = ttk.Button(frm, text='Sei lá').grid(column=1, row =1)
#teste.bind('<Button-1>', mudarTexton)
#app.mainloop()
class Mylabel(Frame):
        def __init__(self, master, key, value):
            Frame.__init__(self, master, background = "#666")
            #Place usa cordenadas
            #Grig usa o esquema de linha e colunas
            #Pack usa Lados
            Label(self, text=key, bg='#88F', width = 18).grid(row=0, column=1) #Preciso definir o grid
            Label(self, text=value, bg='#F29', width = 18).grid(row=0, column=2)

class Funcs():
    def ret_texto(self, text = "Foda"):
        print(text)

    def clicked(self, event):
        btn_text = self.cget('text')
        message = Label(root, text=f'You clicked button "{btn_text}".')
        message.pack()

class Main(Funcs):
    def __init__(self, master = None):
        self.root = root    
        self.dividindo_tela()
        self.criando_botoes()
        root.mainloop()
    
    def dividindo_tela(self):
        self.topFrame = Frame(self.root, width = 1200 , height = 30 , bg = "blue")
        self.topFrame.grid(row = 0, column = 0)

        self.middleFrame = Frame(self.root, width = 1200, height = 600)
        self.middleFrame.grid(row = 1, column = 0)

        self.bottomFrame = Frame(self.root, width = 1200, height = 70, bg = "yellow")
        self.bottomFrame.grid(row = 2, column = 0)

        self.leftFrame = Frame(self.middleFrame, width = 240, height = 600, bg = "gray")
        self.leftFrame.grid(row=1, column=0)

        self.rightFrame = Frame(self.middleFrame, width = 240, height = 600, bg = "cyan")
        self.rightFrame.grid(row=1, column=4)

        self.center_rigth_Frame = Frame(self.middleFrame, width = 240, height = 600, bg = "red")
        self.center_rigth_Frame.grid(row=1, column=3)

        self.center_left_Frame = Frame(self.middleFrame, width = 240, height = 600, bg = "purple")
        self.center_left_Frame.grid(row=1, column=1)

        self.center_center_Frame = Frame(self.middleFrame, width = 240, height = 600, bg = "black")
        self.center_center_Frame.grid(row=1, column=2)

    def criando_botoes(self):
        self.btn1 = Button(self.center_center_Frame, text="Teste", bg='#DDD', width = 30, command=lambda text="btn-teste": self.ret_texto(text)) #Preciso definir o grid
        #self.btn1.bind("<Button-1>", self.ret_texto(text = self.btn1['text']))
        self.btn1.pack()

        self.btn2 = Button(self.center_center_Frame, text="Algo", bg='#DDD', width = 30,command=lambda text="btn-novo": self.ret_texto(text), ) #Preciso definir o grid
        self.btn2.bind("<Button-2>", self.clicked)
        self.btn2.pack()

class MyOptions(Frame):
        def __init__(self, master, elemento, coluna):
            Frame.__init__(self, master)
            #Place usa cordenadas
            #Grig usa o esquema de linha e colunas
            #Pack usa Lados
            self.btn = Button(self, text=elemento, bg='#DDD', width = 30) #Preciso definir o grid
            self.btn.bind("<Button-1>", self.ret_texto)
            self.btn.pack()
        
        def ret_texto(self, event):
            print(self.btn['text'])

        

class Application(Tk):
    def __init__(self, master=None):
        master.title('Perguntas Medicina')
        #master.geometry("350x350")
        self.cont = 0
        self.top_frame = Frame(master)
        self.top_frame.pack(side=TOP)
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.top_frame, text="Top-Left1", bg="#44C")
        self.msg.pack(side = LEFT)
        self.msg1 = Label(self.top_frame, text="Top-Left2",width=10, bg="#11F")
        self.msg1.pack(side = LEFT)
        self.msg2 = Label(self.top_frame, text="Top-Left3",width=10, bg="#D23")
        self.msg2.pack(side = LEFT)
        self.sair = Button(self.widget1, text='Clique Aqui', width=10)
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack(side = LEFT)
        self.btn1 = Button(self.widget1, text='BTN1', width=10)
        self.btn1.pack(side = LEFT)
        self.btn2 = Button(self.widget1, text='BTN2', width=10)
        self.btn2.pack(side =LEFT)
        #self.teste = self.criar_texto()

    def mudarTexto(self, event):
        if self.cont == 3:
            self.msg["text"] = "Apertado 3 vezes"
            self.cont = 0
        self.cont += 1
    
#class Teste(Frame):
#    def __init__(self,master):
#        self.widget2 = Frame(master)
#        self.widget2.grid()
#        self.q = Label(self.widget2, text='Quadro 1').grid(row=0,column=1)
root = Tk()
Main(root)
#for b in range(0, len(listona)):
#    sub = listona[b]
#    for e in range(0, len(sub)):
#        MyOptions(root, sub[e], b).pack()
#
#Application(root)
#Teste(root)
#root.mainloop()