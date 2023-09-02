# Importação	das bibliotecas 

import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox as mb
import nmap

# função responsavel pelo scan das portas e validação do fingerprint.
def scan(ip,programa): 
    
    target = ip 
    nm = nmap.PortScanner()
    dados = []
    programa_nmap = []
    validator = []
    path = "FINGERPRINT/Database.txt"
    programa_name = programa

    #abertura do arquivo que contem a base de dados para poder pegar o preset dos fingerprints
    with open(f"{path}","r") as texto:
        dados = texto.read().replace(";","").lower().split()

    #Laço responsavel por pegar as portas do programa selecioonado
    for palavras in dados:
        if programa in palavras:
            programa_nmap = palavras
            programa_nmap = programa_nmap.replace(","," ").split()
            programa_nmap.remove(f"{programa_name}")
            break
    #laço responsavel por fazer a varredura das pontas para validação do fingerprint
    for x in programa_nmap:
        res = nm.scan(target,str(x)) 
        res = res['scan'][target]['tcp'][int(x)]['state']
        validator.append(res)
        text_box.config(state="normal",foreground="black")
        text_box.insert(tk.END, f'port {x} is {res}.\n')
        text_box.config(state="disabled")
        text_box.update()

    #laço responsavel por validar se tem ou nao uma porta fechada dentre as portas varridas 
    for x in validator:
        if x == "closed":
            text_box.config(state="normal",foreground="red")
            text_box.insert(tk.END, f'FINGERPRINT NÃO ENCONTRADO.\n')
            text_box.config(state="disabled")
            text_box.update()
            tk.messagebox.showerror(
            title="ATENÇÃO!", message="FINGERPRINT NÃO ENCONTRADO")
            break
        else:
            text_box.config(state="normal",foreground="green")
            text_box.insert(tk.END, f'FINGERPRINT ENCONTRADO.\n')
            text_box.config(state="disabled")
            text_box.update()
            tk.messagebox.showwarning(title="ATENÇÃO!", message="FINGERPRINT ENCONTRADO")
            break

# funçao que valida os valores preenchidos nos entrys e inicia a funcão de scan
def send_message():
    clear_text()
    ip = entry1.get()
    programa = entry2.get()
    if ip == "":
        tk.messagebox.showerror(
            title="IP não preenchido", message="Por favor Digite um IP")
        return
    if programa == "":
        tk.messagebox.showerror(
            title="Nome do programa não preenchido", message="Por favor Digite um programa")
        return
    else:
        programa = programa.lower()
        scan(ip,programa)

#Função para limpar a text_box
def clear_text():
    text_box.config(state="normal")
    text_box.delete(1.0, tk.END)
    text_box.config(state="disabled")

def on_text_change(*args):
    text_box.see(tk.END)


# inicio da interface grafica
valida = False
root = tk.Tk()
root.title("Nmap Com Python") 

try: 
	root.iconbitmap('CONFIG/icon.ico')
	
except:
	pass

# Label e Caixa de entrada do IP

label1 = tk.Label(root, text="IP:")
target = label1.pack(padx=10, pady=5, anchor="w")
entry1 = tk.Entry(root)
entry1.pack(padx=10, pady=5, fill=tk.X)

# Label e Caixa de entrada do Programa

label2 = tk.Label(root, text='Nome do "Programa" que deseja buscar o fingerprint: ')
label2.pack(padx=10, pady=5, anchor="w")
entry2 = tk.Entry(root)
entry2.pack(padx=10, pady=5, fill=tk.X)


# Frame para os botões
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Botões para enviar mensagem e limpar

send_button = tk.Button(button_frame, text="Buscar", command=send_message)
send_button.pack(side=tk.LEFT, padx=5)
clear_button = tk.Button(button_frame, text="Limpar", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=5)

# Widget de texto com scroll

text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled")
text_box.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
text_box.bind("<KeyRelease>", on_text_change)
window_width = 400
window_height = 500
root.geometry(f"{window_width}x{window_height}")
root.resizable(False, False)


root.mainloop()

