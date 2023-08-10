Procedimentos = ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Desfibrilação", "Toracocentese de alívio", "Pericardiocentese", "Intubação orotraqueal"]
Medicações = ["Adrenalina", "Amiodarona", "Sulfato de magnésio", "Glucanato de cálcio", "Glico-insulina", "Bicarbonato de sódio", "Soro fisiológico", "Ringer lactato", "Cloreto de potássio"]

listona = [Procedimentos, Medicações]
#print(listona)

q1 = {"P0": ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Desfibrilação", "Adrenalina"],
        "P1": ["Compressão torácica por 2 minutos", "Desfibrilação", "Amiodarona"],
        "P2":["Compressão torácica por 2 minutos", "Desfibrilação", "Adrenalina"],
        "P3": ["Compressão torácica por 2 minutos", "Desfibrilação", "Amiodarona"]}
numero = 2
teste = f'P{numero}'
print(q1[teste])