import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as mb
import nmap
import datetime
import os 

global dados
global valor_resp
valor_resp = ""

global data 
hora_atual = datetime.datetime.now()
data = str(hora_atual.strftime("%d_%m_%Y"))

def criar_pastas():
    global data
    try:
        dir =  'LOGS'
        os.makedirs(dir)
    except:
        pass
    try:
        
        os.makedirs(f"LOGS/{data}")
        if not os.path.exists(f"LOGS/{data}/Log do dia {data}.txt"): 
            open(f"LOGS/{data}/Log do dia {data}.txt", 'w')
        
    except:
        pass
    
    if not os.path.exists(f"LOGS/{data}/Log do dia {data}.txt"): 
            open(f"LOGS/{data}/Log do dia {data}.txt", 'w')

criar_pastas()

def logs(texto):
    hora_atual = datetime.datetime.now()
    try:
        with open(f"LOGS/{data}/Log do dia {data}.txt","a") as arquivo:
            arquivo.write(f"{hora_atual}:Ocorrẽncia {texto}")
        
    except:
        pass


def update_combobox():
    new_values = select()  # Chame a função select() para obter os novos valores
    entry2['values'] = new_values  # Atualize os valores da caixa de combinação

def select():
    global dados
    valores_select = []
    path = "FINGERPRINT/Database.txt"
    try:
        with open(f"{path}","r") as texto:
            dados = texto.read().replace(";","").lower().split()
        for valores in dados:
            valores_select.append(valores[:valores.find(",")])
    except:
        pass
    return valores_select

#Função para analisar as portas fiware,27017,1026,8666,1883,9001,4041;
def scan(ip, programa):
    global dados
    target = ip
    nm = nmap.PortScanner()
    validator = []
    programa_name = programa
    
    texto = f'Teste de fingerprint\n'
    logs(texto)
    for palavras in dados:
        if programa in palavras:
            programa_nmap = palavras
            programa_nmap = programa_nmap.replace(",", " ").split()
            programa_nmap.remove(f"{programa_name}")
            break
    for x in programa_nmap:
        res = nm.scan(target, str(x))
        res = res['scan'][target]['tcp'][int(x)]['state']
        validator.append(res)
        text_box.config(state="normal", foreground="black")
        text_box.insert(tk.END, f'port {x} is {res}.\n')
        text_box.config(state="disabled")
        text_box.update()
        texto = f'IP:{target} teste : port {x} is {res}.\n'
        logs(texto)
        
    for x in validator:
        if x == "closed":
            text_box.config(state="normal", foreground="red")
            text_box.insert(tk.END, f'FINGERPRINT NÃO ENCONTRADO.\n')
            text_box.config(state="disabled")
            text_box.update()
            tk.messagebox.showerror(
                title="ATENÇÃO!", message="FINGERPRINT NÃO ENCONTRADO")
            texto = f'FINGERPRINT NÃO ENCONTRADO\n'
            logs(texto)
            return
            
            
        else:
            text_box.config(state="normal", foreground="green")
            text_box.insert(tk.END, f'FINGERPRINT ENCONTRADO.\n')
            text_box.config(state="disabled")
            text_box.update()
            tk.messagebox.showwarning(
                title="ATENÇÃO!", message="FINGERPRINT ENCONTRADO")
            texto = f'FINGERPRINT ENCONTRADO\n'
            logs(texto)
            return
        
def scan_portas(ip, portas):
    target = ip
    nm = nmap.PortScanner()
   
    texto = f'Varredura de portas listadas\n'
    logs(texto)
        
    for x in portas:
        print(x)
        res = nm.scan(target, str(x))
        res = res['scan'][target]['tcp'][int(x)]['state']
        text_box.config(state="normal", foreground="black")
        text_box.insert(tk.END, f'port {x} is {res}.\n')
        text_box.config(state="disabled")
        text_box.update()
        texto = f'IP:{target} teste : port {x} is {res}.\n'
        logs(texto)
        
    return
  
def scan_intervalo(ip, intervalo):
    target = ip
    nm = nmap.PortScanner()
    inicio = int(intervalo[0])
    fim = int(intervalo[1])
    texto = f'Varredura de intervalo de portas\n'
    logs(texto)
        
    if inicio < fim:
        for x in range(inicio,fim+1):
            res = nm.scan(target, str(x))
            res = res['scan'][target]['tcp'][int(x)]['state']
            text_box.config(state="normal", foreground="black")
            text_box.insert(tk.END, f'port {x} is {res}.\n')
            text_box.config(state="disabled")
            text_box.update()
            texto = f'IP:{target} teste : port {x} is {res}.\n'
            logs(texto)
        return
    else:
        for x in range(fim,inicio+1):
            res = nm.scan(target, str(x))
            res = res['scan'][target]['tcp'][int(x)]['state']
            text_box.config(state="normal", foreground="black")
            text_box.insert(tk.END, f'port {x} is {res}.\n')
            text_box.config(state="disabled")
            text_box.update()
            texto = f'IP:{target} teste : port {x} is {res}.\n'
            logs(texto)
        return

def send_message():
    clear_text()
    choice = vl.get()
    ip = entry1.get()
    programa = entry2.get()
    intervalo = entry4.get()
    portas = entry5.get()
    portas = portas.split()
    
    if ip == "":
        tk.messagebox.showerror(
            title="IP não preenchido", message="Por favor Digite um IP")
        return
    
    if choice == "None":
        tk.messagebox.showerror(
            title="ERRO!!", message="Por favor escolha uma opção")
        return
    if choice == "serviço":
        if programa != "":
            programa = programa.lower()
            scan(ip, programa)
        else:
            tk.messagebox.showerror(
                title="ERRO!!", message="Por favor Escolha um programa!!!")
            return
    if choice == "intervalo":
        if intervalo != "" or intervalo != " " and intervalo.find("-") != -1 :
            
            intervalo = intervalo.replace("-"," ").split()
            scan_intervalo(ip,intervalo)
        else:
            tk.messagebox.showerror(
                title="ERRO!!", message="Por favor Digite um intervalo valido como o exemplo (0-100)!!!")
            return
    if choice == "portas":
        if portas != "" or portas != " ":
            scan_portas(ip, portas)
        else:
            tk.messagebox.showerror(
                title="ERRO!!", message="Por favor Digite uma porta!!!")
            return


def clear_text():
    text_box.config(state="normal")
    text_box.delete(1.0, tk.END)
    text_box.config(state="disabled")

def on_text_change(*args):
    text_box.see(tk.END)

def handle_radio_selection():
    choice = vl.get()
    if choice == "serviço":
        label4.grid_forget()
        entry4.grid_forget()
        label5.grid_forget()
        entry5.grid_forget()
        label2.grid(row=5, column=0, padx=10, pady=(10, 5), sticky="w")
        entry2.grid(row=6, column=0, padx=10, pady=(10, 5), sticky="we")
    elif choice == "intervalo":
        label2.grid_forget()
        entry2.grid_forget()
        label5.grid_forget()
        entry5.grid_forget()
        label4.grid(row=5, column=0, padx=10, pady=(10, 5), sticky="w")
        entry4.grid(row=6, column=0, padx=10, pady=(10, 5), sticky="we")
    elif choice == "portas":
        label2.grid_forget()
        entry2.grid_forget()
        label4.grid_forget()
        entry4.grid_forget()
        label5.grid(row=5, column=0, padx=10, pady=(10, 5), sticky="w")
        entry5.grid(row=6, column=0, padx=10, pady=(10, 5), sticky="we")
        

valida = False

root = tk.Tk()
root.title("Nmap Com Python")

# Label e Caixa de entrada de dados 1
label1 = tk.Label(root, text="IP:")
label1.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")
entry1 = tk.Entry(root)
entry1.grid(row=1, column=0, padx=10, pady=(10, 5), sticky="we")



# Label e Caixa de entrada de dados 2
label2 = tk.Label(root, text='Nome do "Programa" que deseja buscar o fingerprint: ')
entry2 = ttk.Combobox(root, values=select(), width=27)

label4 = tk.Label(root, text='Digte o intervalo de portas ex (10-1000) ')
entry4 = ttk.Entry(root, width=27)

label5 = tk.Label(root, text='Digte as portas ')
entry5 = ttk.Entry(root, width=27)



#label escolha de nome de programa ou número de porta
label3 = tk.Label(root, text="Escolha uma das opções:")
label3.grid(row=3, column=0, padx=10, pady=(5, 0), sticky="w")

radio_frame = tk.Frame(root)
radio_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=(5, 0), sticky="we")

vl = tk.StringVar()
vl.set(None)

vl1 = tk.Radiobutton(radio_frame, text="Informar nome do serviço", variable=vl, value="serviço", command=handle_radio_selection)
vl1.grid(row=0, column=0, padx=5, pady=(5, 0))

vl2 = tk.Radiobutton(radio_frame, text="Informar o intervalo de Portas", variable=vl, value="intervalo", command=handle_radio_selection)
vl2.grid(row=0, column=1, padx=5, pady=(5, 0))

vl3 = tk.Radiobutton(radio_frame, text="Informar as Portas", variable=vl, value="portas", command=handle_radio_selection)
vl3.grid(row=0, column=2, padx=5, pady=(5, 0))


# Frame para os botões
button_frame = tk.Frame(root)
button_frame.grid(row=7, column=0, columnspan=2, pady=(10, 0))

# Botões para enviar mensagem, limpar e refresh
send_button = tk.Button(button_frame, text="Buscar", command=send_message)
send_button.pack(side=tk.LEFT, padx=5)
clear_button = tk.Button(button_frame, text="Limpar", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=5)
refresh_button = tk.Button(button_frame, text="Refresh", command=update_combobox)
refresh_button.pack(padx=10)


# Widget de texto com scroll
text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled")
text_box.grid(row=8, column=0, columnspan=1, padx=10, pady=(0, 10), sticky="we")
text_box.bind("<KeyRelease>", on_text_change)


# Iniciar a interface
root.mainloop()
