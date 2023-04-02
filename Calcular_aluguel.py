import tkinter as tk
from tkinter import ttk

# Cria a janela principal
janela = tk.Tk()
janela.title('Aluguel de carros')
janela.configure(bg='LightGray')






                        ##  DADOS DO CLIENTE  ##
##Insere o nome do cliente
nome_cliente_label = tk.Label(janela, text='Nome completo do cliente:', bg='LightGray', fg='black', anchor='center')
nome_cliente_label.pack()
nome_cliente_entry = tk.Entry(janela, width=50, bg='White', fg='black', insertbackground='black')
nome_cliente_entry.pack()





##Tipo de documento
lista_documento = ['','CPF','RG','CNH']

##Menu suspenso para selecionar o Tipo de documento
documento_tipo_label = tk.Label(janela, text='Tipo de Documento', bg='LightGray', fg='black', anchor='center')
documento_tipo_label.pack()
combobox = ttk.Combobox(janela, values=lista_documento,  width=5)
combobox.pack()




##Insere o documento do cliente
documento_cliente_label = tk.Label(janela, text='Documento do cliente:', bg='LightGray', fg='black', anchor='center')
documento_cliente_label.pack()
documento_cliente_entry = tk.Entry(janela, width=50, bg='White', fg='black', insertbackground='black')
documento_cliente_entry.pack()


##Insere a data de nascimento do cliente
data_nascimento_label = tk.Label(janela, text='Data de nascimento do cliente:', bg='LightGray', fg='black', anchor='center')
data_nascimento_label.pack()
data_nascimento_entry = tk.Entry(janela, width=10, bg='White', fg='black', insertbackground='black')
data_nascimento_entry.pack()



                        ##  VALORES A SER COBRADO  ##
##Insere o valor cobrado por dia
valor_dia_label = tk.Label(janela, text='Valor cobrado por dia R$ ', bg='LightGray', fg='black', anchor='center')
valor_dia_label.pack()
valor_dia_entry = tk.Entry(janela, width=50, bg='White', fg='black', insertbackground='black')
valor_dia_entry.pack()


##Insere o valor a ser cobrado a cada 1 km
valor_km_label = tk.Label(janela, text='Valor a cada 1 KM rodado R$ ', bg='LightGray', fg='black', anchor='center')
valor_km_label.pack()
valor_km_entry = tk.Entry(janela, width=50, bg='White', fg='black', insertbackground='black')
valor_km_entry.pack()






                        ##   INFORMAÇÕES DOS VEÍCULOS   ##
##Veículos Cadastrado pela empresa
lista_opcoes = ['','Renault Kwid', 'Renault Sandero', 'Chevrolet Onix', 'Renault Logan', 'Nissan Versa', 'Chevrolet Spin', 'Hyundai HB20 S', 'Volkswagen Voyage', 'Fiat Grand Siena']

##Cadastro  de Placa de Cada Modelo de Carro
carros_placas = {
    'Renault Kwid': 'ABC-1234',
    'Renault Sandero': 'DEF-5678',
    'Chevrolet Onix': 'GHI-9012',
    'Renault Logan': 'JKL-3456',
    'Nissan Versa': 'MNO-7890',
    'Chevrolet Spin': 'PQR-1235',
    'Hyundai HB20 S': 'STU-6789',
    'Volkswagen Voyage': 'VWX-0123',
    'Fiat Grand Siena': 'YZA-4567'
}


##Menu suspenso para selecionar o veículo cadastrado
carro_label = tk.Label(janela, text='Modelo do carro:', bg='LightGray', fg='black', anchor='center')
carro_label.pack()
combobox = ttk.Combobox(janela, values=lista_opcoes,  width=45)
combobox.pack()


##Placa dos veículos
placa_label = tk.Label(janela, text='Placa do veículo:', bg='LightGray', fg='black')
placa_label.pack()
placa_entry = tk.Entry(janela, width=50, bg='White', fg='black', insertbackground='black')
placa_entry.pack()

##Quando a placa é atualizada no momento em que o veículo é selecionada o usuário não consigue remover ou alterar a informação da placa
def atualiza_placa(*args):
    carro = combobox.get()
    placa = carros_placas.get(carro, '')
    placa_entry.delete(0, tk.END)
    placa_entry.config(state='normal')
    placa_entry.delete(0, tk.END)
    placa_entry.insert(0, placa)
    placa_entry.config(state='disabled')



##Associa a função de atualização à combobox
combobox.bind("<<ComboboxSelected>>", atualiza_placa)


##KM atual do veículo selecionado
km_incial_label = tk.Label(janela, text='KM atual do veículo:', bg='LightGray', fg='black', anchor='center')
km_incial_label.pack()
km_incial_entry = tk.Entry(janela, width=50, bg='White', fg='black', insertbackground='black')
km_incial_entry.pack()






                        ##  INFORMAÇÕES PARA CHECKOUT  ##
##Insere a quilometragem rodada pelo cliente
km_rodado_label = tk.Label(janela, text='Quantos quilometros o cliente rodou?', bg='LightGray', fg='black', anchor='center')
km_rodado_label.pack()
km_rodado_entry = tk.Entry(janela, width=50, bg='White', fg='black', insertbackground='black')
km_rodado_entry.pack()

##Insere a quantidade de dias com que o cliente ficou com o carro
dias_aluguel_label = tk.Label(janela, text='Quantos dias o cliente rodou?', bg='LightGray', fg='black', anchor='center')
dias_aluguel_label.pack()
dias_aluguel_entry = tk.Entry(janela, width=50, bg='White', fg='black', insertbackground='black')
dias_aluguel_entry.pack()






                        ##   CALCULO DO VALOR FINAL   ##
valor_final_label = tk.Label(janela, text='', bg='LightGray', fg='black')
valor_final_label.pack()


##Faz o calculo final de acordo com as informações inseridas
def calcular_valor_final():
    valor_dia = float(valor_dia_entry.get())
    valor_km = float(valor_km_entry.get())
    km_rodado = float(km_rodado_entry.get())
    dias_aluguel = int(dias_aluguel_entry.get())
    valor_final = (valor_dia*dias_aluguel) + (valor_km*km_rodado)
    valor_final_label.config(text=f'O valor total a ser pago é R$: {valor_final:.2f}', bg='LightGray', fg='black')

##Botão para Calcular
calcular_button = tk.Button(janela, text='Calcular', command=calcular_valor_final, bg='LightGray', fg='black')
calcular_button.pack()






                                    ##  FORMAS DE PAGAMENTO  ##

##Seleciona a forma de pagamento
def selecionar_forma_pagamento():
    if forma_pag.get() == '1':
        forma_pagamento_label.config(text='A forma de pagamento selecionada foi: DINHEIRO')
    elif forma_pag.get() == '2':
        forma_pagamento_label.config(text='A forma de pagamento selecionada foi: CARTÃO')
    elif forma_pag.get() == '3':
        forma_pagamento_label.config(text='A forma de pagamento selecionada foi: PIX')
    else:
        forma_pagamento_label.config(text='Opção inválida. Por favor, escolha 1, 2 ou 3')


##Selecionar a forma de pagamento que o cliente irá utilizar
label = tk.Label(janela, text="Selecione a forma de pagamento:", bg='LightGray', fg='black')
label.pack()


##Função para verificar a escolha do usuário na forma de pagamento
def escolher_pagamento(escolha):
    if escolha == "Dinheiro":
        forma_pag = "DINHEIRO"
    elif escolha == "Cartão":
        forma_pag = "CARTÃO"
    elif escolha == "pix":
        forma_pag = "PIX"        
    else:
        forma_pag = "OUTRO"
    return forma_pag






                        ##  BOTÕES DE PAGAMENTO  ##
##Frame para os botões
frame = tk.Frame(janela)
frame.pack()

##Cria os botões da forma de pagamento
dinheiro = tk.Button(frame, text="Dinheiro", bg='White', fg='black')
cartao = tk.Button(frame, text="Cartão", bg='White', fg='black')
PIX = tk.Button(frame, text="PIX", bg='White', fg='black')

##Define as ações dos botões
forma_pagamento = tk.StringVar()
rb_cartao = tk.Radiobutton(text="Cartão", variable=forma_pagamento, value="cartao", bg='LightGray', fg='black')
rb_dinheiro = tk.Radiobutton(text="Dinheiro", variable=forma_pagamento, value="dinheiro", bg='LightGray', fg='black')
rb_pix = tk.Radiobutton(text="PIX", variable=forma_pagamento, value="pix", bg='LightGray', fg='black')

rb_cartao.config(width=10, bg='LightGray', fg='black')
rb_dinheiro.config(width=10, bg='LightGray', fg='black')
rb_pix.config(width=10, bg='LightGray', fg='black')

##Posicionando os Radiobuttons na janela
rb_cartao.pack()
rb_dinheiro.pack()
rb_pix.pack()

janela.mainloop()
