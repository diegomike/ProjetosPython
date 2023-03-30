import tkinter as tk
from tkinter import ttk



# Cria a janela principal
janela = tk.Tk()
janela.title('Aluguel de carros')
janela.configure(bg='white')

def calcular_valor_final():
    valor_dia = float(valor_dia_entry.get())
    valor_km = float(valor_km_entry.get())
    km_rodado = float(km_rodado_entry.get())
    dias_aluguel = int(dias_aluguel_entry.get())
    valor_final = (valor_dia*dias_aluguel) + (valor_km*km_rodado)
    valor_final_label.config(text=f'O valor total a ser pago é R$: {valor_final:.2f}', bg='white', fg='black')



def selecionar_forma_pagamento():
    if forma_pag.get() == '1':
        forma_pagamento_label.config(text='A forma de pagamento selecionada foi: DINHEIRO')
    elif forma_pag.get() == '2':
        forma_pagamento_label.config(text='A forma de pagamento selecionada foi: CARTÃO')
    else:
        forma_pagamento_label.config(text='Opção inválida. Por favor, escolha 1 ou 2.')

def imprimir_forma_pagamento():
    print("Forma de pagamento escolhida:", forma_pagamento.get())




# Cria os rótulos e caixas de entrada para o nome do cliente
nome_cliente_label = tk.Label(janela, text='Nome completo do cliente:', bg='white', fg='black')
nome_cliente_label.pack()
nome_cliente_entry = tk.Entry(janela, width=50, bg='white', fg='black', insertbackground='black')
nome_cliente_entry.pack()


# Cria os rótulos e caixas de entrada para o CPF do cliente
cpf_cliente_label = tk.Label(janela, text='Documento do cliente:', bg='white', fg='black')
cpf_cliente_label.pack()
cpf_cliente_entry = tk.Entry(janela, width=50, bg='white', fg='black', insertbackground='black')
cpf_cliente_entry.pack()



# Cria os rótulos e caixas de entrada para a data de nascimento do cliente
data_nascimento_label = tk.Label(janela, text='Data de nascimento do cliente:', bg='white', fg='black')
data_nascimento_label.pack()
data_nascimento_entry = tk.Entry(janela, width=50, bg='white', fg='black', insertbackground='black')
data_nascimento_entry.pack()




# Cria os rótulos e caixas de entrada para os valores por dia
valor_dia_label = tk.Label(janela, text='Valor cobrado por dia R$ ', bg='white', fg='black')
valor_dia_label.pack()
valor_dia_entry = tk.Entry(janela, width=50, bg='white', fg='black', insertbackground='black')
valor_dia_entry.pack()


# Cria os rótulos e caixas de entrada para os valores por km
valor_km_label = tk.Label(janela, text='Valor por KM rodado R$ ', bg='white', fg='black')
valor_km_label.pack()
valor_km_entry = tk.Entry(janela, width=50, bg='white', fg='black', insertbackground='black')
valor_km_entry.pack()



# Cria os rótulos e caixas de entrada para ao modelo do veículo
carro_label = tk.Label(janela, text='Modelo do carro:', bg='white', fg='black')
carro_label.pack()
carro_entry = tk.Entry(janela, width=50, bg='white', fg='black', insertbackground='black')
carro_entry.pack()



# Cria os rótulos e caixas de entrada para a placa do veículo
placa_label = tk.Label(janela, text='Placa do veículo:', bg='white', fg='black')
placa_label.pack()
placa_entry = tk.Entry(janela, width=50, bg='white', fg='black', insertbackground='black')
placa_entry.pack()


# Cria os rótulos e caixas de entrada para a KM atual do veículo
km_incial_label = tk.Label(janela, text='KM atual do veículo:', bg='white', fg='black')
km_incial_label.pack()
km_incial_entry = tk.Entry(janela, width=50, bg='white', fg='black', insertbackground='black')
km_incial_entry.pack()



# Cria os rótulos e caixas de entrada para o checkout com a km rodada
km_rodado_label = tk.Label(janela, text='Quantos quilometros o cliente rodou?', bg='white', fg='black')
km_rodado_label.pack()
km_rodado_entry = tk.Entry(janela, width=50, bg='white', fg='black', insertbackground='black')
km_rodado_entry.pack()

# Cria os rótulos e caixas de entrada para o checkout com os dias de aluguel
dias_aluguel_label = tk.Label(janela, text='Quantos dias o cliente rodou?', bg='white', fg='black')
dias_aluguel_label.pack()
dias_aluguel_entry = tk.Entry(janela, width=50, bg='white', fg='black', insertbackground='black')
dias_aluguel_entry.pack()

#valor final
valor_final_label = tk.Label(janela, text='')
valor_final_label.pack()


#Botão Calcular
calcular_button = tk.Button(janela, text='Calcular', command=calcular_valor_final, bg='white', fg='black')
calcular_button.pack()

# Cria um label para a forma de pagamento
label = tk.Label(janela, text="Selecione a forma de pagamento:", bg='white', fg='black')
label.pack()

# Cria um frame para os botões
frame = tk.Frame(janela)
frame.pack()

# Cria os botões
dinheiro = tk.Button(frame, text="Dinheiro", bg='white', fg='black')
cartao = tk.Button(frame, text="Cartão", bg='white', fg='black')

# Função para verificar a escolha do usuário
def escolher_pagamento(escolha):
    if escolha == "Dinheiro":
        forma_pag = "DINHEIRO"
    else:
        forma_pag = "CARTÃO"

# Define as ações dos botões
forma_pagamento = tk.StringVar()
rb_cartao = tk.Radiobutton(text="Cartão", variable=forma_pagamento, value="cartao", bg='white', fg='black')
rb_dinheiro = tk.Radiobutton(text="Dinheiro", variable=forma_pagamento, value="dinheiro", bg='white', fg='black')

rb_cartao.config(width=10, bg='white', fg='black')
rb_dinheiro.config(width=10, bg='white', fg='black')

# Posicionando os Radiobuttons na janela
rb_cartao.pack()
rb_dinheiro.pack()

janela.mainloop()