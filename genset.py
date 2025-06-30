# Projecto de Gerador

import datetime

def calcular_gerador():
    print("=== Dimensionador de Gerador ===\n")
    equipamentos = []
    total_potencia = 0

    n = int(input("Quantos equipamentos deseja inserir? "))

    for i in range(n):
        print(f"\nEquipamento {i+1}:")
        nome = input("Nome: ")
        tipo = input("Tipo (iluminacao/motor/equipamento comum/sensível): ").lower()
        potencia = float(input("Potência (W): "))
        quantidade = int(input("Quantidade: "))
        tempo_uso = float(input("Horas de uso por dia (opcional - 0 se desconhecido): "))

        # Factor de arranque para motores (multiplica a potência por 2.5)
        if tipo == "motor":
            factor_arranque = 2.5
            potencia *= factor_arranque

        equipamentos.append({
            "nome": nome,
            "tipo": tipo,
            "potencia": potencia,
            "quantidade": quantidade,
            "tempo_uso": tempo_uso
        })

        total_potencia += potencia * quantidade

    
    # Factor de potência (customizável por tipo)
    factor_potencia = float(input("\nEscreva o factor de potência (ex: 0.8): ") or 0.8)
    factor_seguranca = float(input("\nEscreva o factor de segurança (ex: 1.2)") or 1.2)

    #
    
