# Projecto de Gerador

import datetime

def calcular_gerador():
    print("=== Dimensionador de Gerador ===\n")
    equipamentos = []
    potencia_total = 0

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

        potencia_total += potencia * quantidade

    
    # Factor de potência (customizável por tipo)
    factor_potencia = float(input("\nEscreva o factor de potência (ex: 0.8): ") or 0.8)
    factor_seguranca = float(input("\nEscreva o factor de segurança (ex: 1.2)") or 1.2)

    # Conversão para kVA
    potencia_kva = (potencia_total / 1000) / factor_potencia
    potencia_kva *= factor_seguranca

    print("\n====== RESULTADO FINAL =====")
    print(f"Potência total em W: {round(potencia_total, 2)} W")
    print(f"Potência ideal do gerador: {round(potencia_kva, 2)} kVA")

    # Energia diária estimada (se tempos de uso forem fornecidos)
    energia_total_diaria = sum(e['potencia'] * e['quantidade'] * e['tempo_uso'] for e in equipamentos)
    if energia_total_diaria > 0:
        print(f"Consumo diário estimado: {round(energia_total_diaria/1000, 2)} kWh/dia")

    # Exportar para TXT
    exportar = input("\nDeseja exportar o relatório pra .txt? (s/n): ").lower()
    if exportar == 's':
        with open("relatorio_gerador.txt", "w") as f:
            f.write("RELATÓRIO DE DIMENSIONAMENTO DE GERADOR\n")
            f.write(f"Data: {datetime.datetime.now()}\n\n")
            for eq in equipamentos:
                f.write(f"- {eq['quantidade']}x {eq['nome']} ({eq['potencia']}W) - Tipo: {eq['tipo']}\n")
            f.write(f"\nPotência total: {potencia_total: .2f} W\n")
            f.write(f"Factor de potência: {factor_potencia}\n")
            f.write(f"Factor de segurança: {factor_seguranca}\n")
            f.write(f"Potência ideal do gerador: {round(potencia_kva, 2)} kVA\n")
            if energia_total_diaria > 0:
                f.write(f"Consumo estimado diário: {round(energia_total_diaria/1000, 2)} kWh\n")
        print("Relatório exportado com sucesso: relatorio_gerador.txt")

# Executar a função principal
if __name__ == "__main__":
    calcular_gerador()
