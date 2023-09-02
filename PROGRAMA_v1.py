import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox as mb
import nmap

global dados
global valor_resp

valor_resp = ""
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



#Função para analize das portas fiware,27017,1026,8666,1883,9001,4041;
def scan(ip,programa): #entrada do ip que sera varido e do nome do programa que deseja ver se existe.
    global dados
    target = ip
    nm = nmap.PortScanner()
    validator = []
   
    programa_name = programa
    
    for palavras in dados:
        
        if programa in palavras:
            programa_nmap = palavras
            programa_nmap = programa_nmap.replace(","," ").split()
            programa_nmap.remove(f"{programa_name}")
            break
        
    for x in programa_nmap:
        res = nm.scan(target,str(x)) 
        res = res['scan'][target]['tcp'][int(x)]['state']
        validator.append(res)
        text_box.config(state="normal",foreground="black")
        text_box.insert(tk.END, f'port {x} is {res}.\n')
        text_box.config(state="disabled")
        text_box.update()



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
            tk.messagebox.showwarning(
            title="ATENÇÃO!", message="FINGERPRINT ENCONTRADO")

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
            


def clear_text():
    text_box.config(state="normal")
    text_box.delete(1.0, tk.END)
    text_box.config(state="disabled")

def on_text_change(*args):
    text_box.see(tk.END)


valida = False
root = tk.Tk()
root.title("Nmap Com Python") 

# Label e Caixa de entrada de dados 1
label1 = tk.Label(root, text="IP:")
target = label1.pack(padx=10, pady=5, anchor="w")
entry1 = tk.Entry(root)
entry1.pack(padx=10, pady=5, fill=tk.X)

#label escolha de nome de programa ou numerod e porta
label3 = tk.Label(root, text="Escolha uma das opções:")
check_box = label3.pack(padx=10, pady=5, anchor="w")


radio_frame = tk.Frame(root)
radio_frame.pack(pady=10)

vl = tk.StringVar()
vl.set(None)

vl1 = tk.Radiobutton(radio_frame, text="Informar nome do serviço", variable=vl,value="serviço")
vl1.pack(side=tk.LEFT, padx=5)

vl2 = tk.Radiobutton(radio_frame, text="Informar Portas",variable=vl,value="portas")
vl2.pack(side=tk.LEFT, padx=5)

# Label e Caixa de entrada de dados 2
label2 = tk.Label(root, text='Nome do "Programa" que deseja buscar o fingerprint: ')
label2.pack(padx=10, pady=5, anchor="w")

entry2 = ttk.Combobox(root,values=select(),width = 27)
entry2.pack(padx=10, pady=5, fill=tk.X)


# Frame para os botões
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Botões para enviar mensagem, limpar e refresh
send_button = tk.Button(button_frame, text="Buscar", command=send_message)
send_button.pack(side=tk.LEFT, padx=5)
clear_button = tk.Button(button_frame, text="Limpar", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=5)
refresh_button = tk.Button(button_frame, text="Refresh", command=update_combobox)
refresh_button.pack(padx=10)


# Widget de texto com scroll
text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled")
text_box.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

text_box.bind("<KeyRelease>", on_text_change)

window_width = 400
window_height = 500
root.geometry(f"{window_width}x{window_height}")
root.resizable(False, False)


# Iniciar a interface
root.mainloop()
