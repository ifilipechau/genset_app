# genset_app

# ⚡ Dimensionador de Gerador Residencial/Comercial

Este é um projecto em Python que calcula a **potência ideal de um gerador** para residências, pequenas empresas ou edifícios, com base nos equipamentos utilizados, tempo de uso, tipo de carga e factores técnicos como factor de potência e factor de segurança.

---

## 🧠 Funcionalidades

✅ Cadastro de múltiplos equipamentos (nome, tipo, potência, quantidade, tempo de uso)  
✅ Consideração de **tipos de carga**: iluminação, motores, cargas sensíveis  
✅ Aplicação automática de **factor de arranque** para motores  
✅ Cálculo da **potência total em watts (W)**  
✅ Conversão para **potência em kVA**, com:
- Factor de potência personalizável
- Factor de segurança ajustável

✅ Estimativa de **consumo diário em kWh/dia**  
✅ Exportação do resultado para um **relatório `.txt`** automático

---

## 💻 Como usar

### 1. Clone ou baixe este repositório
Se preferir, pode baixar o código fonte como um arquivo ZIP e extrair.
Se tiver o Git instalado, use o comando abaixo para clonar o repositório:
```bash
git clone https://github.com/ifilipechau/genset_app.git
cd genset_app
```

### 2. Execute o script
Certifique-se de ter o Python instalado (versão 3.6 ou superior).
```bash
python genset.py
```

### 3. Siga as instruções no terminal
O programa irá:
- Solicitar a quantidade de equipamentos
- Coletar dados sobre cada equipamento
- Calcular e mostrar os resultados no terminal
- Perguntar se deseja salvar um relatório .txt

### 4. Exemplo de uso

Quantos equipamentos deseja inserir? 3

Equipamento 1:
Nome: Geladeira
Tipo: motor
Potência (W): 200
Quantidade: 1
Horas de uso por dia: 24

Equipamento 2:
Nome: Lâmpadas
Tipo: iluminacao
Potência (W): 60
Quantidade: 6
Horas de uso por dia: 5

Equipamento 3:
Nome: Computador
Tipo: sensível
Potência (W): 250
Quantidade: 2
Horas de uso por dia: 8

### 👨‍💻 Autor
Filipe Chau
Data Center Engineer • Engenheiro em Segurança Eletrônica • Educador em Tecnologia
📧 [filipechau@outlook.pt ou [linkedin](https://www.linkedin.com/in/filipe-chau-b25820211)]

### 📜 Licença
Este projecto está licenciado sob a licença MIT. Sinta-se livre para usar e adaptar.