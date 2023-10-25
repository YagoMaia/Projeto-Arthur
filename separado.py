from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
from random import randint

Procedimentos = ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Desfibrilação", "Toracocentese de alívio", "Pericardiocentese", "Intubação orotraqueal"]
Medicações = ["Adrenalina", "Amiodarona", "Sulfato de magnésio", "Glucanato de cálcio", "Glico-insulina", "Bicarbonato de sódio", "Soro fisiológico", "Ringer lactato", "Cloreto de potássio"]
Exames = ["Hemoglobina", "Leucograma", "Plaquetas", "Uréia", "Creatinina", "Potássio", "Sódio", "Magnésio", "Proteína C reativa", "Lactato", "pH", "Pco2", "Po2", "HCO3", "Base excess", "Saturação do oxigênio", "Raio X de tórax", "ECG"]

quadros = [{"Quadro Clinico": "Quadro 1 - 45% dos casos", "Probabilidades":[2,2,2,1], "Procedimentos_salvamento": {"P0": ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Desfibrilação", "Adrenalina"],"P1": ["Compressão torácica por 2 minutos", "Desfibrilação", "Amiodarona"],"P2":["Compressão torácica por 2 minutos", "Desfibrilação", "Adrenalina"],"P3": ["Compressão torácica por 2 minutos", "Desfibrilação", "Amiodarona"]}, "Condições Quadros": {'Pressão Arterial': 0, 'Frequência Cardíaca':0, 'Frequência Respiratória': 0, 'Saturação de Oxigênio': 0, 'Monitor ECG' : 'Fibrilação Ventricular','Conciencia' : 'Inconsciente'}},
        {"Quadro Clinico": "Quadro 2 - 10% dos casos", "Probabilidades":[1], "Procedimentos_salvamento":{"P0": ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Desfibrilação", "Sulfato de magnésio"]}, "Condições Quadros": {'Pressão Arterial': 0, 'Frequência Cardíaca':0, 'Frequência Respiratória': 0, 'Saturação de Oxigênio': 0, 'Monitor ECG' : 'Torsades de pointes','Conciencia' : 'Inconsciente'}},
        {"Quadro Clinico": "Quadro 3 - 45% dos casos", "Probabilidades":[1], "Procedimentos_salvamento": {"P0": ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Adrenalina"]},"Condições Quadros": {'Pressão Arterial': 0, 'Frequência Cardíaca':0, 'Frequência Respiratória': 0, 'Saturação de Oxigênio': 0, 'Monitor ECG' : 'Assistolia','Conciencia' : 'Inconsciente'}}]

procedimento_escolhido = randint(0, 2)
quadro_select = quadros[procedimento_escolhido]
cont_tent = 0

class Funcs():
    #Focar nas funções
    #Procurar um jeito de melhorar essas funções
    
    def countdown(self, num_sec):
        m, s = divmod(num_sec,60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        self.timer.set(min_sec_format)

        if num_sec > 0:
            if self.timer_ajuste.get() > 0 and self.change.get() == "True":
                tempo_total = self.timer_ajuste.get()
                self.change.set("False")
            else:
                tempo_total = num_sec
            root.after(1000, self.countdown, tempo_total-1)
        if num_sec == 0:
            messagebox.showinfo("Tempo esgotado", "Você não conseguiu ajudar o paciente dentro do tempo")
            self.master.destroy()
    
    def ret_texto(self, text, tempo = 30):
        if text == "Compressão torácica por 2 minutos":
            tempo = 120
        tempo_atual = self.timer.get()
        m,s = int(tempo_atual[0:2]), int(tempo_atual[3:5])
        tempo_convertido = (m*60)+s - tempo
        self.timer_ajuste.set(tempo_convertido)
        self.change.set("True")

        self.mostra.set(f"Ação usada: {text}")
        self.salvamento(text)

    def clicked(self,btn_text):
        self.mostra.set(f"Ação usada: {btn_text}")

    def salvamento(self, acao):
        valido = True
        proc = quadro_select["Procedimentos_salvamento"]
        max_tentativas  = len(proc)
        if (self.tentativas.get()) == max_tentativas:
            messagebox.showinfo("Quantidade de Procedimento Excedido", "Você realizou tentativas demais")
            self.master.destroy()
        if(valido):
            lista_procedimentos = proc[f"P{cont_tent}"]
            self.procedimentos_usados.append(acao)
            if len(lista_procedimentos) == len(self.procedimentos_usados):
                if lista_procedimentos == self.procedimentos_usados:
                    tentativas_totais = cont_tent + 1
                    if tentativas_totais == max_tentativas:
                        messagebox.showinfo("Procedimentos Correto", "Você seguiu todos os procedimentos da maneira correta\nO Paciente foi salvo")
                        self.master.destroy()
                    self.procedimentos_usados = []
                    self.tentativas.set(tentativas_totais)
                    self.mostra.set(f"Quantidade de Tentativas: {tentativas_totais}")
                else:
                    messagebox.showinfo("Procedimentos Errados", "Você não seguiu os procedimentos da maneira correta\nPor causa disso o paciente morreu")
                    self.master.destroy()

class Counter():
    def countdown(self, num_sec):
        m, s = divmod(num_sec,60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        self.timer.set(min_sec_format)

        if num_sec > 0:
            if self.timer_ajuste.get() > 0 and self.change.get() == "True":
                tempo_total = self.timer_ajuste.get()
                self.change.set("False")
            else:
                tempo_total = num_sec
            root.after(1000, self.countdown, tempo_total-1)
        if num_sec == 0:
            messagebox.showinfo("Tempo esgotado", "Você não conseguiu ajudar o paciente dentro do tempo")
            self.master.destroy()
            
    def tempo_acoes(self, text, tempo = 30):
        if text == "Compressão torácica por 2 minutos":
            tempo = 120
        tempo_atual = self.timer.get()
        m,s = int(tempo_atual[0:2]), int(tempo_atual[3:5])
        tempo_convertido = (m*60)+s - tempo
        self.timer_ajuste.set(tempo_convertido)
        self.change.set("True")

        self.mostra.set(f"Ação usada: {text}")

class BigLabel(Frame, Funcs):
    def __init__(self, master):
        self.quadro = StringVar()
        self.quadro.set(quadro_select['Quadro Clinico'])
        Frame.__init__(self, master, background= "#AFA",)
        Label(self, textvariable=self.quadro, background="#FFF", font=19, width=30).pack()

class Mylabel(Frame, Funcs):
        def __init__(self, master, key, value):
            Frame.__init__(self, master,)
            Label(self, text=key, width = 20, font = 19).pack(side = LEFT)
            Label(self, text=value, width = 20, font = 19).pack(side = RIGHT)

class Buttons(Frame, Funcs):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.procedimentos_usados = []
        self.timer = StringVar()
        self.timer_ajuste = IntVar()
        self.change = StringVar()
        self.mostra = StringVar()
        self.tentativas = IntVar()
        Label(self, textvariable=self.timer, bg='#8AD', font=(19)).grid(row=0, columnspan=5)
        Label(self, textvariable=self.mostra, bg='#8FF', font=(19)).grid(row=1, columnspan=5)
        self.countdown(1200)
        for procedimento in range(0, len(Procedimentos)):
            p = Procedimentos[procedimento]
            Button(self, text = p, bg='#DDD', width = 30, command=lambda text=p : self.ret_texto(text)).grid(row=procedimento+3, column=1) #Preciso definir o grid
        for medicamento in range(0,len(Medicações)):
            m = Medicações[medicamento]
            Button(self, text = m, bg='#DDD', width = 30, command=lambda text=m : self.ret_texto(text)).grid(row=medicamento+3, column=2) #Preciso definir o grid
        for exame in range(0,len(Exames)):
            e = Exames[exame]
            Button(self, text = e, bg='#DDD', width = 30, command=lambda text=e : self.ret_texto(text)).grid(row=exame+3, column=3) #Preciso definir o grid
root = Tk()
timer = Counter()
BigLabel(root).pack(expand=True, fill='x', anchor="center")
for k, v in quadro_select["Condições Quadros"].items():
    Mylabel(root, k, v).pack(expand=True, fill="y")

Buttons(root).pack(expand=True)

root.mainloop()