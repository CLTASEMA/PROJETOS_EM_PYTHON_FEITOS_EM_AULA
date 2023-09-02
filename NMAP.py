import nmap
nm = nmap.PortScanner()
dados = []
programa_nmap = []
validator = []
target = '10.0.2.15'
path = "FINGERPRINT/Database.txt"
programa = input('Informe o "Programa" que deseja saber se esta rodando: ').lower()


with open(f"{path}","r") as texto:
    dados = texto.read().replace(";","").lower().split()

for palavras in dados:
    
    if programa in palavras:
        programa_nmap = palavras
        programa_nmap = programa_nmap.replace(","," ").split()
        programa_nmap.remove(f"{programa}")
        break
    
for x in programa_nmap:
    res = nm.scan(target,str(x)) 
    res = res['scan'][target]['tcp'][int(x)]['state'] 
    validator.append(res)
    print(f'port {x} is {res}.')
    


for x in validator:
    if x == "closed":
        print("fingerprint not found")
        break
    else:
        print("FINGER PRINT ENCONTRADO")