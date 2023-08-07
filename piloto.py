from random import randint

Quadro_1 = {
    'Pressão Arterial': 0, 
    'Frequência Cardíaca':0, 
    'Frequência Respiratória': 0, 
    'Saturação de Oxigênio': 0, 
    'Monitor ECG' : 'Fibrilação Ventricular',
    'Conciencia' : 'Inconsciente'
}

Quadro_2 = {
    'Pressão Arterial': 0, 
    'Frequência Cardíaca':0, 
    'Frequência Respiratória': 0, 
    'Saturação de Oxigênio': 0, 
    'Monitor ECG' : 'Torsades de pointes',
    'Conciencia' : 'Inconsciente'
}

Quadro_3 = {
    'Pressão Arterial': 0, 
    'Frequência Cardíaca':0, 
    'Frequência Respiratória': 0, 
    'Saturação de Oxigênio': 0, 
    'Monitor ECG' : 'Assistolia',
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

class Q1():

    def __init__(self):
        self.condicoes = {
        'Pressão Arterial': 0, 
        'Frequência Cardíaca':0, 
        'Frequência Respiratória': 0, 
        'Saturação de Oxigênio': 0, 
        'Monitor ECG' : 'Fibrilação Ventricular',
        'Conciencia' : 'Inconsciente'
        },
        self.lp1_q1 = ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Desfibrilação", "Adrenalina"],
        self.lp1_q2 = ["Compressão torácica por 2 minutos", "Desfibrilação", "Amiodarona"],
        self.lp1_q3 = ["Compressão torácica por 2 minutos", "Desfibrilação", "Adrenalina"],
        self.lp1_q4 = ["Compressão torácica por 2 minutos", "Desfibrilação", "Amiodarona"]
    
    def loop(self, proc : list):
        acertos = 0
        while True:
            procedimentos = input("Quais são os procedimentos que deverão ser realizados: ")
            #if procedimentos == proc[acertos]:
            if procedimentos == '1':
                acertos+=1
            else:
                print("Procedimento errado")
                return 'Morto'
            if acertos == 4:
                print("Procedimentos certos")
                if sucesso >= 10:
                    print("Paciente Salvo")
                    return 'Vivo'
                else:
                    return 'Errado'

    def p1_q1(self):
        acertos = 0
        sucesso = randint(0,20)
        return self.loop(self.lp1_q1)

    def p1_q2(self, estado : str):
        acertos = 0
        sucesso = randint(0,20)
        return self.loop(self.lp1_q2)
    
    def p1_q3(self, estado : str):
        acertos = 0
        sucesso = randint(0,20)
        return self.loop(self.lp1_q3)
        
    def p1_q4(self, estado : str):
        acertos = 0
        sucesso = 20
        return self.loop(self.lp1_q4)

    def p1_completo(self):
        salvo = self.p1_q1()
        if salvo == 'Morto':
            return False
        elif salvo == 'Errado':
            salvo = self.p1_q2(salvo)
            if salvo == 'Morto':
                return False
            elif salvo == 'Errado':
                salvo = self.p1_q3(salvo)
                if salvo == 'Morto':
                    return False
                elif salvo == 'Errado':
                    salvo = self.p1_q4(salvo)
        return salvo
            
p1_q1 = ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Desfibrilação", "Adrenalina"]
acertos = 0
sucesso = randint(0,20)

qua1 = Q1()
qua1.p1_completo()

#while True:
#    procedimentos = input("Quais são os procedimentos que deverão ser realizados: ")
#    #if procedimentos == p1_q1[acertos]:
#    if procedimentos == '1':
#        acertos+=1
#    else:
#        print("Procedimento errado")
#        break
#    if acertos == 4:
#        print("Procedimentos certos")
#        if sucesso >= 10:
#            print("Paciente Salvo")
#        else:
#            print("Paciente Morto")
#        break
#
