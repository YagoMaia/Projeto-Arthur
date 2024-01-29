planilha = {
    'Procedimentos' : 
        [
        "Compressão torácica por 2 minutos", "Ventilação com AMBU", "Desfibrilação", "Toracocentese de alívio", "Pericardiocentese", "Intubação orotraqueal", "Verificar Painel", "Tratar Alteração"
        ],
    'Medicações' : 
        [
        "Adrenalina", "Amiodarona", "Sulfato de magnésio", "Glucanato de cálcio", "Glico-insulina", "Bicarbonato de sódio", "Soro fisiológico", "Ringer lactato", "Cloreto de potássio"
        ],
    'Exames' : 
        [
            "Hemoglobina", "Leucograma", "Plaquetas", "Uréia", "Creatinina", "Potássio", "Sódio", "Magnésio", "Proteína C reativa", "Lactato", "pH", "Pco2", "Po2", "HCO3", "Base excess", "Saturação do oxigênio", "Raio X de tórax", "ECG"
        ],
    'Quadros' : 
    [
        {
            "Quadro Clinico": 
            "Quadro 1 - 45% dos casos", 
            "Tempo": 420,
            "Probabilidades":[2,2,2,1], 
            "Procedimentos_salvamento": {
                "P0": ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Desfibrilação", "Adrenalina"],
                "P1": ["Compressão torácica por 2 minutos", "Desfibrilação", "Amiodarona"],
                "P2":["Compressão torácica por 2 minutos", "Desfibrilação", "Adrenalina"],
                "P3": ["Compressão torácica por 2 minutos", "Desfibrilação", "Amiodarona"]},
            "Condições Quadros": {
                'Pressão Arterial': 0, 
                'Frequência Cardíaca':0, 
                'Frequência Respiratória': 0, 
                'Saturação de Oxigênio': 0, 
                'Monitor ECG' : 'Fibrilação Ventricular',
                'Conciencia' : 'Inconsciente'},
            "Condiçoes":{
                "Ação": "Amiodarona",
                "Perda_tempo":120
            },
            "Caso_especial":[]
        },
        {
            "Quadro Clinico": 
            "Quadro 2 - 10% dos casos", 
            "Probabilidades":[1],
            "Tempo":300,
            "Procedimentos_salvamento":{
                "P0": ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Desfibrilação", "Sulfato de magnésio"]
                }, 
            "Condições Quadros": {
                'Pressão Arterial': 0, 
                'Frequência Cardíaca':0, 
                'Frequência Respiratória': 0, 
                'Saturação de Oxigênio': 0, 
                'Monitor ECG' : 'Torsades de pointes',
                'Conciencia' : 'Inconsciente'},
            "Caso_especial":[]
        },
        {
            "Quadro Clinico": 
            "Quadro 3 - 45% dos casos", 
            "Probabilidades":[1], 
            "Tempo": 300,
            "Procedimentos_salvamento": {
                "P0": ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Adrenalina","Verificar Painel", "Tratar Alteração"]
            },
            "Condições Quadros": 
                {
                'Pressão Arterial': 0, 
                'Frequência Cardíaca':0, 
                'Frequência Respiratória': 0, 
                'Saturação de Oxigênio': 0, 
                'Monitor ECG' : 'Assistolia',
                'Conciencia' : 'Inconsciente'
                },
            "Caso_especial":
            [
                {
                    "Extra":"Nada"
                },
                {
                    "Extra": "Hiperpotassemia",
                    "P0": ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Adrenalina", "Verificar Painel", "Tratar Alteração","Glucanato de cálcio", "Glico-insulina", "Bicarbonato de sódio"]
                },
                {
                    "Extra": "Ph 6,9 e bicarbonato de 5 mEq/l",
                    "P0": ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Adrenalina", "Verificar Painel", "Tratar Alteração","Bicarbonato de sódio"]
                },
                {
                    "Extra": "pO2 de 45 mmHg e SO2 de 60%",
                    "P0": ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Adrenalina", "Verificar Painel", "Tratar Alteração", "Intubação orotraqueal"]
                },
                {
                    "Extra": "Hipopotassemia",
                    "P0": ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Adrenalina", "Verificar Painel", "Tratar Alteração", "Cloreto de potassio"]
                },
                {
                    "Extra": "Lactato, ureia, creatinina aumentados",
                    "P0": ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Adrenalina", "Verificar Painel", "Tratar Alteração", "Soro fisiológico ou ringer lactato"]
                },
                {
                    "Extra": "Raio X com pneumotórax ",
                    "P0": ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Adrenalina", "Verificar Painel", "Tratar Alteração", "Toracocentese de alívio"]
                },
                {
                    "Extra": "ECG com baixa voltagem e raio X de tórax com coração em moringa",
                    "P0": ["Compressão torácica por 2 minutos", "Ventilação com AMBU", "Adrenalina", "Verificar Painel", "Tratar Alteração", "Pericardiocentese"]
                },
            ],
        }
    ]
}