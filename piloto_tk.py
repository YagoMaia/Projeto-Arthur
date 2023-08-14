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
Exames = ["Hemoglobina",
"Leucograma",
"Plaquetas",
"Uréia",
"Creatinina",
"Potássio",
"Sódio",
"Magnésio",
"Proteína C reativa",
"Lactato",
"pH",
"Pco2",
"Po2",
"HCO3",
"Base excess",
"Saturação do oxigênio",
"Raio X de tórax",
"ECG"]

class Mylabel(Frame):
        def __init__(self, master, key, value):
            Frame.__init__(self, master, background = "#666")
            Label(self, text=key, bg='#88F', width = 18).grid(row=0, column=1) #Preciso definir o grid
            Label(self, text=value, bg='#F29', width = 18).grid(row=0, column=2)

class Funcs():
    def ret_texto(self, text):
        self.acoes.set(f"Ação usada: {text}")
        self.salvamento(text)
        

    def clicked(self,btn_text):
        print(btn_text)
        self.acoes.set(f"Ação usada: {btn_text}")

    def salvamento(self, acao):
        print(self.tentativas.get())
        valido = True
        if (self.tentativas.get()) == 4:
            self.root.destroy()
            valido = False
        if(valido):
            lista_procedimentos = self.q1[f"P{self.tentativas.get()}"]
            self.procedimentos_usados.append(acao)
            if len(lista_procedimentos) == len(self.procedimentos_usados):
                print(lista_procedimentos)
                print(self.procedimentos_usados)
                self.procedimentos_usados = []
                tentativas_totais = self.tentativas.get() + 1
                self.tentativas.set(tentativas_totais)
                self.mostra.set(f"Quantidade de Tentativas: {tentativas_totais}")


class Main(Funcs):
    def __init__(self, master = None):
        self.acoes = StringVar()
        self.tentativas = IntVar()
        self.mostra = StringVar()
        self.root = root
        self.altura = root.winfo_screenheight()
        self.largura = root.winfo_screenwidth()/2
        self.altura_quero = 600
        self.largura_quero = 600
        self.procedimentos_usados = []
        self.q1 = {"P0": ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Desfibrilação", "Adrenalina"],
        "P1": ["Compressão torácica por 2 minutos", "Desfibrilação", "Amiodarona"],
        "P2":["Compressão torácica por 2 minutos", "Desfibrilação", "Adrenalina"],
        "P3": ["Compressão torácica por 2 minutos", "Desfibrilação", "Amiodarona"]}
        self.posx = self.largura/2 - self.largura_quero/2
        self.posy = self.altura/2 - self.altura_quero/2
        self.dividindo_tela()
        self.criando_frame()
        self.criando_botoes2()
        root.mainloop()
        
    
    def dividindo_tela(self):
        self.topFrame = Frame(self.root, width = self.largura , height = self.altura/5, bg = "blue")
        self.topFrame.grid(row = 0, column = 0)

        self.middleFrame = Frame(self.root, width = self.largura, height = self.altura/3)
        self.middleFrame.grid(row = 1, column = 0)

        self.bottomFrame = Frame(self.root, width = self.largura, height = self.altura/10, bg = "yellow")
        self.bottomFrame.grid(row = 2, column = 0)

        self.leftFrame = Frame(self.middleFrame, width = self.largura/5, height = self.altura/3, bg = "gray")
        self.leftFrame.grid(row=1, column=0)

        self.rightFrame = Frame(self.middleFrame, width = self.largura/5, height = self.altura/3, bg = "cyan")
        self.rightFrame.grid(row=1, column=4)

        self.center_rigth_Frame = Frame(self.middleFrame, width = self.largura/5, height = self.altura/3, bg = "red")
        self.center_rigth_Frame.grid(row=1, column=3)

        self.center_left_Frame = Frame(self.middleFrame, width = self.largura/5, height = self.altura/3, bg = "purple")
        self.center_left_Frame.grid(row=1, column=1)

        self.center_center_Frame = Frame(self.middleFrame, width = self.largura/5, height =  self.altura/3, bg = "black")
        self.center_center_Frame.grid(row=1, column=2)
    
    def criando_botoes2(self):
        r = 1
        for p in Procedimentos:
            Button(self.center_left_Frame, text = p, bg='#DDD', width = 30, command=lambda text=p : self.ret_texto(text)).grid(row=r, column=1) #Preciso definir o grid
            r+=1
        r = 1
        for m in Medicações:
            Button(self.center_rigth_Frame, text = m, bg='#DDD', width = 30, command=lambda text=m : self.ret_texto(text)).grid(row=r, column=1) #Preciso definir o grid
            r+=1
        r = 1
        for e in Exames:
            Button(self.center_center_Frame, text = e, bg='#DDD', width = 30, command=lambda text=e : self.ret_texto(text)).grid(row=r, column=1) #Preciso definir o grid
            r+=1
        
    def criando_frame(self):
        a = 1
        self.tentativas.set(0)
        Label(self.topFrame, textvariable=self.mostra, bg='#8FF', font=(19)).grid(row=0, columnspan=2)
        Label(self.topFrame, text="Quadro Número 1 - 45%", bg='#88F', font=(19)).grid(row=1, columnspan=2)
        for k, v in condicoes.items():
            Label(self.topFrame, text=k, bg='#88F', width = 18, font=(19)).grid(row=a, column=0) #Preciso definir o grid
            Label(self.topFrame, text=v, bg='#F29', width = 18, font=(19)).grid(row=a, column=1)
            a+=1
        Label(self.topFrame, textvariable=self.acoes, bg = "#Df9", font = (19)).grid(row=a+1,columnspan=2)

class MyOptions(Frame):
        def __init__(self, master, elemento, coluna):
            Frame.__init__(self, master)
            self.btn = Button(self, text=elemento, bg='#DDD', width = 30) #Preciso definir o grid
            self.btn.bind("<Button-1>", self.ret_texto)
            self.btn.pack()
        
        def ret_texto(self, event):
            print(self.btn['text'])

        

class Application(Tk):
    def __init__(self, master=None):
        master.title('Perguntas Medicina')
        master.resizable(0,0)
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

    def mudarTexto(self, event):
        if self.cont == 3:
            self.msg["text"] = "Apertado 3 vezes"
            self.cont = 0
        self.cont += 1
    
root = Tk()
Main(root).pack()

root.mainloop()