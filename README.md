# PROJETOS PORTSCAN COM PYTHON-NMAP 🌐🔍

## Instruções de uso pela opção 1 (busca por fingerprint) 📝

1. Git clone do projeto: `git clone https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/`
2. Navegue até a pasta do projeto: `cd PROJETOS_EM_PYTHON_FEITOS_EM_AULA`
3. Instale as dependências: `pip3 install -r requirements.txt`
4. Alimente o arquivo Database.txt com as informações referentes ao fingerprint que deseja procurar:
   - Modelo de entrada: `{nome do "programa"},{porta}{porta};`
   - Coloque o nome do programa e as portas separando por vírgula e no final `";"`
5. Execute o script portescan.py: `python3 PROGRAMA_V2.py`
6. Escolha a opção "Informar nome do serviço"
7. Insira o IP da máquina-alvo
8. Digite ou selecione o nome do programa

## Exemplo de execução do programa:
Após baixar o repositório, acesse a pasta FINGERPRINT e siga as instruções acima. 🔍🚀




<hr>

2 -  Entre no arquivo "Database.txt":

![FOTO2.png](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/blob/main/FOTO2.png)

<hr>

3  - Preencha a linha seguindo a instrução 4 : 

![FOTO3](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/aa52d99e-31f5-4571-b2c4-b83adde6dfd3)

<hr>

4 - Execute o programa no terminal dentro da pasta:

![FOTO6](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/b76eec82-4e92-4151-8e5c-81bb9184388c)


<hr>


5 - Preencha o campo de IP com o Ip que deseja escanear:

![FOTO4](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/3209fd87-405f-440b-886d-5c41205ebbdb)

<hr>

6 - Preencha o campo de NOME DO PROGRAMA com o NOME DO PROGRAMA que deseja ver se está rodando na maquina (o nome do programa é o mesmo nome colocado antes das postas no documento "Database.txt"):


![FOTO5](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/bcb91ff3-e3b2-41be-8aa2-5d006efeb1e6)


<hr>

7 -  Após a busca do programa caso não esteja rodando na maquina o app ira informar que o fingerprint não foi encontrado:


![FOTO8](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/fe127e8f-26f7-4e8b-8622-fb1af6b908a1)                          ![FOTO7](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/1bfd36c3-ee6d-4ae5-a7f3-9f76051f7c95) 



<hr>

8 -  Caso o fingerprint seja encontrado o programa ira retornar:

![Captura de tela 2023-08-26 163959](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/732d10b5-58e9-41db-a51f-9b61da7773e3)       ![Captura de tela 2023-08-26 163947](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/4caa55f3-e4e4-4044-bf45-24a195b3857f)







