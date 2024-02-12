#from tkinter import *
#from tkinter import ttk
#from tkinter import messagebox
import time
from random import randint
from dados import planilha
import customtkinter
from customtkinter import StringVar, IntVar
from CTkMessagebox import CTkMessagebox

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

procedimento_escolhido = randint(0, 2)
procedimento_extra = randint(0, 6)
quadro_select = planilha['Quadros'][procedimento_escolhido]

cont_tent = tentativas = 0
procedimentos_usados = []

def salvamento(master, clock, acao):
    
    global procedimentos_usados
    
    proc = quadro_select["Procedimentos_salvamento"]
    if len(quadro_select["Caso_especial"]) > 0:
        proc = quadro_select["Caso_especial"][procedimento_extra]
    max_tentativas  = len(proc)
    lista_procedimentos = proc[f"P{cont_tent}"]
    procedimentos_usados.append(acao)
    if len(lista_procedimentos) == len(procedimentos_usados):
        if lista_procedimentos == procedimentos_usados:
            tentativas_totais = cont_tent + 1
            clock.mostra.set("Primeira parte do procedimento correto")
            if tentativas_totais == max_tentativas:
                msg = CTkMessagebox(title = "Procedimentos Correto", option_1="Ok", message= "Você seguiu todos os procedimentos da maneira correta\nO Paciente foi salvo", icon = "check")
                resp = msg.get()
                master.destroy()
            procedimentos_usados = []
            #clock.mostra.set(f"Quantidade de Tentativas: {tentativas_totais}")
        else:
            msg = CTkMessagebox(title = "Procedimentos Errados", option_1="Ok", message= "Você não seguiu os procedimentos da maneira correta\nPor causa disso o paciente morreu\nLink para a aula:", icon = "cancel")
            resp = msg.get()
            master.destroy()

def ret_texto(master, text, clock, tempo = 10):
        if text == "Compressão torácica por 2 minutos" or (text == "Amiodarona" and procedimento_escolhido == 1):
            tempo = 120
        tempo_atual = clock.timer.get()
        m,s = int(tempo_atual[0:2]), int(tempo_atual[3:5])
        tempo_convertido = (m*60)+s - tempo
        clock.timer_ajuste.set(tempo_convertido)
        clock.change.set("True")

        clock.mostra.set(f"Ação usada: {text}")
        salvamento(master, clock, text)

def clicked(btn_text, clock):
    clock.mostra.set(f"Ação usada: {btn_text}")

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
            msg = CTkMessagebox(title = "Tempo esgotado", option_1="Ok", message= "Você não conseguiu ajudar o paciente dentro do tempo", icon = "Error")
            resp = msg.get()
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

class BigLabel(customtkinter.CTkFrame): #Mostrar qual quadro foi selecionado
    def __init__(self, master):
        self.quadro = StringVar()
        self.quadro.set(quadro_select['Quadro Clinico'])
        customtkinter.CTkFrame.__init__(self, master)
        customtkinter.CTkLabel(self, textvariable=self.quadro, font=("",19), width=30).pack()

class Mylabel(customtkinter.CTkFrame): #Dados no Painel
    def __init__(self, master, key, value):
        tamanho_label = 300
        customtkinter.CTkFrame.__init__(self, master)
        customtkinter.CTkLabel(self, text=key, width = tamanho_label,font =("" ,19)).pack(side = "left", expand = True, fill = "x")
        customtkinter.CTkLabel(self, text=value, width = tamanho_label,font =("" ,19)).pack(side = "right", expand = True, fill = "x")

class MostrarTimer(customtkinter.CTkFrame, Counter):
    def __init__(self, master):
        customtkinter.CTkFrame.__init__(self, master)
        self.timer = StringVar()
        self.timer_ajuste = IntVar()
        self.change = StringVar()
        self.mostra = StringVar()
        customtkinter.CTkLabel(self, textvariable=self.timer, font=('', 30)).pack()
        customtkinter.CTkLabel(self, textvariable=self.mostra, font=('',19)).pack()
        self.countdown(quadro_select['Tempo'])

class BotoesSeparados(customtkinter.CTkFrame, Counter):
    def __init__(self, master, key, clock):
        customtkinter.CTkFrame.__init__(self, master)
        self.procedimentos_usados = []
        self.tentativas = IntVar()
        self.timer = StringVar()
        self.timer_ajuste = IntVar()
        self.change = StringVar()
        self.mostra = StringVar()
        
        tamanho_botao = 230
        
        customtkinter.CTkButton(self, text = key, width = tamanho_botao, command=lambda text=key : ret_texto(master, text, clock)).pack(fill="x")
            
root = customtkinter.CTk()
root.title("Simulação de casos")
root.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
root.geometry("1000x800")
root.columnconfigure((0,1,2), weight=1)
timer = Counter()
BigLabel(root).grid(row=0, columnspan=3)

for k, v in quadro_select["Condições Quadros"].items():
    Mylabel(root, k, v).grid(columnspan=3, pady=0)

if len(quadro_select["Caso_especial"]) > 0:
   Mylabel(root, "Extra", quadro_select["Caso_especial"][procedimento_extra]['Extra']).grid(columnspan=3, pady=0)

clock = MostrarTimer(root)
clock.grid(columnspan = 3)

customtkinter.CTkLabel(root, text = "Procedimentos", font = ("",20)).grid(columnspan=3, row = 9)
coluna = 0
linha = 10
for index, e in enumerate(planilha['Procedimentos']):
    if coluna == 3:
        coluna = 0
        linha += 1
    BotoesSeparados(root, e, clock).grid(column=coluna, pady=5, row = linha)
    coluna += 1

customtkinter.CTkLabel(root, text = "Medicações", font = ("",20)).grid(columnspan=3, row= linha + 1)
linha += 2
coluna = 0
for index, e in enumerate(planilha['Medicações']):
    if coluna == 3:
        coluna = 0
        linha += 1
    BotoesSeparados(root, e, clock).grid(column=coluna, pady=5, row = linha)
    coluna += 1

customtkinter.CTkLabel(root, text = "Exames", font = ("",20)).grid(columnspan=3, row=linha + 1)
linha += 2
coluna = 0
for index, e in enumerate(planilha['Exames']):
    if coluna == 3:
        coluna = 0
        linha += 1
    BotoesSeparados(root, e, clock).grid(column=coluna, pady=5, row = linha)
    coluna += 1
    
root.mainloop()