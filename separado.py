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

class BigLabel(Frame):
    def __init__(self, master):
        self.quadro = StringVar()
        self.quadro.set(f"Quadro 1 - 45% ocorrência")
        Frame.__init__(self, master, background= "#AFA")
        Label(self, textvariable=self.quadro, background="#AFA", font=19, width=50).grid(row=0, columnspan= 2)

class Mylabel(Frame):
        def __init__(self, master, key, value):
            Frame.__init__(self, master, background = "#666")
            Label(self, text=key, bg='#88F', width = 25).grid(row=0,column=1)
            Label(self, text=value, bg='#F29', width = 25).grid(row=0,column=2)

class Buttons(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, background= "#D23")
        self.mostra = StringVar()
        Label(self, textvariable=self.mostra, bg='#8FF', font=(19)).grid(row=0, columnspan=5)
        for procedimento in range(0, len(Procedimentos)):
            p = Procedimentos[procedimento]
            Button(self, text = p, bg='#DDD', width = 30, command=lambda text=p : self.ret_texto(text)).grid(row=procedimento+1, column=1) #Preciso definir o grid
        for medicamento in range(0,len(Medicações)):
            m = Medicações[medicamento]
            Button(self, text = m, bg='#DDD', width = 30, command=lambda text=m : self.ret_texto(text)).grid(row=medicamento+1, column=2) #Preciso definir o grid
        for exame in range(0,len(Exames)):
            e = Exames[exame]
            Button(self, text = e, bg='#DDD', width = 30, command=lambda text=e : self.ret_texto(text)).grid(row=exame+1, column=3) #Preciso definir o grid

    def ret_texto(self, text):
        self.mostra.set(f"Ação usada: {text}")

root = Tk()
BigLabel(root).pack(expand=True, fill='x',)
for k, v in condicoes.items():
    Mylabel(root, k, v).pack(expand=True, fill="x", padx=149)
Buttons(root).pack(expand=True, fill='x')

root.mainloop()