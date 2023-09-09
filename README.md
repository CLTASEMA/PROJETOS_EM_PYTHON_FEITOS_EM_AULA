# 🚀 Bem-Vindo ao PROJETO PORTSCAN COM PYTHON-NMAP! 🌐🔍

Seja bem-vindo ao nosso incrível projeto de escaneamento de portas e busca por fingerprints em máquinas-alvo. Este aplicativo Python-Nmap é uma ferramenta versátil que coloca o poder da análise de rede em suas mãos.

## Principais Funcionalidades 🛠️

O nosso programa oferece várias funcionalidades incríveis:

1. 🔎 **Busca por Fingerprint**: Identifique e rastreie informações específicas em uma máquina-alvo com facilidade.

2. 🎯 **Escaneamento de Range de Portas**: Realize varreduras em um intervalo de portas para descobrir serviços disponíveis.

3. 🚀 **Escaneamento de Portas Específicas**: Selecione portas específicas para verificar a disponibilidade de serviços.

4. 📋 **Alimentação de Base de Dados**: Mantenha uma base de dados atualizada com os fingerprints que deseja para futuras análises.

5. 📅 **Registro de Atividades Diárias**: Cada operação executada no aplicativo gera um log de registro, organizado por dia, para um acompanhamento completo das atividades.

## Mais Ferramentas 🛠️📁

Além das funcionalidades principais, nosso programa oferece duas ferramentas poderosas para melhorar sua experiência de análise de rede:

1. 📜 **Arquivo Database**: Dentro da pasta "Fingerprint", você encontrará o arquivo "database.txt". Este arquivo é uma base de dados que permite que você gerencie e personalize os predefinidos de fingerprints do programa. Para adicionar ou remover um fingerprint, siga estas regras:
   - Primeiro, insira o nome do programa.
   - Em seguida, separe-o das portas por vírgula.
   - Termine com um ponto e vírgula (`;`).
   - Cada fingerprint deve ser colocado em uma linha separada no documento. Isso permite que você adapte o programa às suas necessidades específicas de análise.

2. 📋 **Arquivo de Logs**: Cada vez que você abre o programa, ele gera automaticamente um arquivo de logs. Esse arquivo é separado por dia e contém um registro completo de todas as saídas e tentativas de busca realizadas no programa. É uma ferramenta valiosa para rastrear suas atividades e garantir a transparência em suas análises de rede.

Essas ferramentas adicionais proporcionam mais controle e rastreamento em suas operações de escaneamento de rede, permitindo uma análise mais precisa e eficaz. Utilize-as para personalizar o programa de acordo com suas necessidades e manter um registro detalhado de suas atividades. 🚀📁


Siga as instruções abaixo para instalar o programa e comece a explorar todas essas funcionalidades incríveis. 

Divirta-se explorando o mundo da segurança de rede com o PROJETO PORTSCAN COM PYTHON-NMAP! 🔒🌐



## Instruções de instalação da ferramenta. 📝

1. Git clone do projeto: `git clone https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/`
2. Navegue até a pasta do projeto: `cd PROJETOS_EM_PYTHON_FEITOS_EM_AULA`
3. Instale as dependências: `pip3 install -r requirements.txt`
4. Execute o script portescan.py: `python3 PROGRAMA_V2.py`


## Exemplo de execução dos passos a cima:
Após baixar o repositório, acesse a pasta FINGERPRINT e siga as instruções acima. 🔍🚀


1º Etapa: Git clone do projeto: `git clone https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/`


![image (9)](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/036ddef1-36f3-4238-b67e-cd8c0249be09)
<hr>

2º Etapa: Navegue até a pasta do projeto: `cd PROJETOS_EM_PYTHON_FEITOS_EM_AULA`


<img width="368" alt="image (8)" src="https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/19c95360-c0ee-4a6e-8677-c570c3fb55e1"><br>


<hr>

3º Instale as dependências: pip3 install -r requirements.txt

![pip](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/995994a0-952d-4ad0-9feb-c591475f48dd)


<hr>

4º Execute o script portescan.py: `python3 PROGRAMA_V2.py`

![image (11)](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/ba27619c-0b7e-4875-810c-a942b82c9cf7)



## Instruções basicas de uso do programa: 📋🔍

O programa oferece três botões essenciais para facilitar a sua experiência:

1. 🚀 **Buscar**: Clique neste botão sempre que preencher todas as informações necessárias em cada opção. Ele iniciará a busca por fingerprint na máquina-alvo e apresentará os resultados de forma clara e organizada.

2. 🧹 **Limpar**: Se desejar limpar os resultados de saída de uma busca anterior e começar uma nova análise, clique neste botão. Isso garante que você tenha uma tela limpa para visualizar os resultados da próxima busca.

3. 🔄 **Refresh**: Às vezes, você pode querer atualizar os dados de fingerprints inseridos no arquivo database sem reiniciar o programa. Clique neste botão para recarregar as informações, permitindo que você adicione ou remova dados sem interromper o fluxo de trabalho.

Esses botões são projetados para tornar a sua experiência com o PROJETO PORTSCAN COM PYTHON-NMAP mais intuitiva e eficiente. Use-os conforme necessário para otimizar suas análises de rede! 🌐🔒


![foto 4](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/f9bccd61-dffc-43a9-ae74-46554b0860eb)


<hr>

## Como Usar o Programa com a opção nome de serviço 📋🔍

1. 🔸 **Selecione a Opção "Escolha o Nome do Serviço"**: No menu principal, escolha esta opção para iniciar o processo de busca por fingerprint.

2. 🌐 **Informe o IP da Máquina Alvo**: Insira o endereço IP da máquina que você deseja analisar. Certifique-se de fornecer um IP válido para a busca.

3. 💼 **Informe o Nome do Programa**: Você pode informar o nome do programa de duas maneiras:
   - 📝 **Digitando no Campo**: Digite manualmente o nome do programa na caixa de texto apropriada.
   - 🔄 **Selecionando no Menu**: Se preferir, você pode escolher o nome do programa a partir de uma lista suspensa para maior comodidade.

4. 🚀 **Clique em "Buscar"**: Depois de inserir todas as informações necessárias, clique no botão "Buscar" para iniciar o processo de busca por fingerprint. O programa irá analisar a máquina-alvo e fornecer resultados valiosos.

1º Saida do programa caso não encontre o fingerprint:

![image](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/ccbbb7ac-3e4e-4a7b-8385-0d3f2eab2cff)


2º Saida do programa caso encontre o fingerprint:

![image (7)](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/16fb1ae9-f565-46e6-9666-8fc2683866f1)


<hr>



## Como Usar o Programa com a opção Intervalo de portas 📋🔍

1. 🌐 **Selecione a Opção "Intervalo de Portas"**: No menu principal, escolha esta opção para iniciar a busca por serviços em um intervalo específico de portas.

2. 🌐 **Informe o IP da Máquina Alvo**: Insira o endereço IP da máquina que deseja analisar. Certifique-se de fornecer um IP válido para a busca.

3. 🔢 **Informe o Intervalo de Portas**: Especifique o intervalo de portas que deseja escanear. Você pode inserir o intervalo no formato "porta inicial - porta final", por exemplo, "80-1000".

4. 🚀 **Clique em "Buscar"**: Após preencher todas as informações necessárias, clique no botão "Buscar" para iniciar o escaneamento do intervalo de portas especificado. O programa fornecerá os resultados detalhados para as portas dentro do intervalo selecionado.

Utilize a opção "Intervalo de Portas" para uma análise precisa e eficaz das portas em sua máquina-alvo. Mantenha sua rede segura e protegida! 🚀🔒
Exemplo no programa (Caso tenha alguma porta aberta no intervalo informado o programa ira retornar com open):

![image (10)](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/c700ab53-191c-42e8-8ed5-186c76d60ea8)

<hr>

## Como Usar o Programa com a opção Informar Portas 📋🔍

Explore a terceira opção do programa, "Informar as Portas", para escanear portas específicas em uma máquina-alvo:

1. 🌐 **Selecione a Opção "Informar as Portas"**: No menu principal, escolha esta opção para iniciar o escaneamento de portas especificadas manualmente.

2. 🌐 **Informe o IP da Máquina Alvo**: Insira o endereço IP da máquina que deseja analisar. Certifique-se de fornecer um IP válido para a busca.

3. 🔢 **Informe as Portas**: Digite as portas que deseja escanear, separadas por espaços. Por exemplo, "80 443 22" para escanear as portas 80, 443 e 22.

4. 🚀 **Clique em "Buscar"**: Após inserir todas as informações necessárias, clique no botão "Buscar" para iniciar o escaneamento das portas especificadas. O programa fornecerá resultados detalhados para as portas informadas.

Utilize a opção "Informar as Portas" quando precisar escanear portas específicas em sua máquina-alvo. Essa funcionalidade oferece controle total sobre quais portas serão analisadas. 🚀🔒

Exemplo no programa: 

![Sem título](https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/a6f356ee-7cf0-4867-8a20-966e5f632cde)



## Saiba Mais e Veja a Ferramenta em Ação! 📺👀

Gostaria de conhecer mais sobre o PROJETO PORTSCAN COM PYTHON-NMAP em ação? Você pode assistir a demonstração completa da ferramenta em nosso vídeo no YouTube!

🎥 **Assista ao Vídeo Tutorial**: [Clique aqui para assistir ao vídeo no Youtube](https://www.youtube.com/watch?v=9hCbX9Sjb-k&feature=youtu.be)



https://github.com/CLTASEMA/PROJETOS_EM_PYTHON_FEITOS_EM_AULA/assets/143286412/9b0d2749-69c6-4671-978a-b509ccd63668



Neste vídeo, você encontrará uma apresentação detalhada das funcionalidades da ferramenta, passo a passo de como usá-la e exemplos práticos de análises de rede. É uma maneira perfeita de se familiarizar com o programa e ver como ele pode ser uma adição valiosa às suas ferramentas de segurança e análise de rede.

Assista ao vídeo, explore as funcionalidades e comece a utilizar o programa já!! 🚀📺

