escolha_menu = 1
cadastro_realizado = False
possuir_acess = False
plano_selecionado = False
linha = "=" * 61
tipo_acess = []
marca_acess = []
modelo_acess = []
valor_acess = []
dados_pessoal_bike = ""
tipo_plano = ""


# SUBALGORITMOS
def menu() -> int:
    global escolha_menu
    print(f"""
    {linha}
    ||                       M E N U                           ||
    {linha}
    || 1................................: Realize o cadastro   ||
    || 2.............................: Selecione o seu plano   ||
    || 3................: Envio das imagens (Em construção!)   ||
    || 4......: Análise dos dados e imagens (Em construção!)   ||
    || 5..............................: Perguntas frequentes   ||
    || 0.................................: Fechar o programa   ||
    {linha}
    """)
    escolha_menu = int(input("---> Escolha uma opção: "))
    return escolha_menu


def cadastro() -> str:
    valor = 0
    quant_acess = 0
    global possuir_acess
    print("Primeiro, precisamos que nos forneça alguns dados pessoais.")
    nome = input("Informe seu nome: ")
    email = input("Informe seu email: ")
    tel = input("Informe seu número de celular: ")
    cpf = input("Informe seu CPF: ")
    cep = input("Informe seu CEP: ")
    print("Agora, os dados de sua bike")
    marca = input("Informe a marca da bike: ")
    modelo = input("Informe o modelo da bike: ")
    chassi = input("Informe o chassi da bike: ")
    while True:
        try:
            valor = float(input("Informe o valor da bike (sem acessórios): "))
            if valor > 2000:
                break
            else:
                print("O valor mínimo de uma bike para que seja assegurada é de R$2000.00...
        except ValueError:
            print("Digite um valor válido...")
            continue
    acessorio = input("Sua bike possui algum acessório adicional? [S/N]: ")
    if acessorio.upper() == "S" or acessorio.upper() == "SIM":
        possuir_acess = True
        while True:
            try:
                quant_acess = int(input("Quantos?: "))
                break
            except ValueError:
                print("Digite um valor válido...")
                continue
        for i in range(0, quant_acess, 1):
            print(f"Acessório {i + 1}")
            tipo_acess.append(input("Informe o tipo do acessório: "))
            marca_acess.append(input("Informe a marca do acessório: "))
            modelo_acess.append(input("Informe o modelo do acessório: "))
            while True:
                try:
                    valor_acess.append(float(input("Informe o valor do acessório: ")))
                    break
                except ValueError:
                    print("Digite um valor válido...")
                    continue
    print(f"""
    {linha}
    ---> CADASTRO FINALIZADO!!!...
    {linha}
    """)

    print_dados = (f"""
    {linha}
    || Dados Pessoais                                          ||
    || Nome: {nome:50}||
    || Email: {email:49}||
    || Telefone: {tel:46}||
    || CPF: {cpf:51}||
    || CEP: {cep:51}||
    
    {linha}
    || Dados da Bike                                           ||
    || Marca: {marca:49}||
    || Modelo: {modelo:48}||
    || Chassi: {chassi:48}||
    || Valor: R${valor:<47.2f}||""")
    return print_dados


def selecionar_plano() -> str:
    escolha_plano = 1
    plano = ""
    print(f"""
    {linha}
    ||                    SELECIONE SEU PLANO                  ||
    {linha}
    || 1 --> Pedal essencial: O plano para você experimentar   ||
    || um dos serviços  essenciais oferecidos, de acordo       ||
    || com as suas   necessidades.                             ||
    || ------------------------------------------------------- ||
    || 2 --> Pedal leve: Você gosta de pedalar e está          ||
    || buscando um plano de serviços intermediário? O Pedal    ||
    || leve da Porto é para você.                              || 
    || ------------------------------------------------------- || 
    || 3 --> Pedal elite: Conte com diversos serviços capazes  ||
    || de elevar suas aventuras para o próximo nível.          ||
    || ------------------------------------------------------- ||
    || 4 --> Saiba mais sobre nossos planos.                   ||
    || ------------------------------------------------------- ||
    || 0 --> Voltar.                                           ||
    {linha}
    """)
    while True:
        try:
            escolha_plano = int(input("---> Escolha uma opção: "))
            break
        except ValueError:
            print(f"""
    {linha}
    ---> DIGITE UMA OPÇÃO VÁLIDA!!!...
    {linha}    
            """)
            continue
    match escolha_plano:
        case 0:
            plano = ""
            print(f"""
    {linha}
    ---> Voltando...
    {linha}    
            """)
        case 1:
            plano = "Pedal essencial"
            print(f"""
    {linha}
    ---> Pedal essencial selecionado!!!...
    {linha}    
            """)
        case 2:
            plano = "Pedal leve"
            print(f"""
    {linha}
    ---> Pedal leve selecionado!!!...
    {linha}    
            """)
        case 3:
            plano = "Pedal elite"
            print(f"""
    {linha}
    ---> Pedal elite selecionado!!!...
    {linha}    
            """)
        case 4:
            print(f"""
    {linha}==============================
    ||=================================== | Pedal essencial|   Pedal leve   |   Pedal elite  ||
    ||                                    |                |                |                ||
    || Reparo de câmaras de ar            |      SIM       |      SIM       |      SIM       ||
    ||                                    |                |                |                ||
    ||------------------------------------|----------------|----------------|----------------||
    ||                                    |                |                |                ||
    || Reparo ou troca de correntes       |      SIM       |      SIM       |      SIM       ||
    ||                                    |                |                |                ||
    ||------------------------------------|----------------|----------------|----------------||
    || Substituição ou regulagem de       |                |                |                ||
    || selim e canote de selim            |      SIM       |      SIM       |      SIM       ||
    ||                                    |                |                |                ||
    ||------------------------------------|----------------|----------------|----------------||
    || Substituição e regulagem           |                |                |                ||
    || manetes de freios e cabo de aço    |      SIM       |      SIM       |      SIM       ||
    ||                                    |                |                |                ||
    ||------------------------------------|----------------|----------------|----------------||
    || Substituição ou regulagem          |                |                |                ||
    || de freio dianteiro e traseiro      |      SIM       |      SIM       |      SIM       ||
    ||                                    |                |                |                ||
    ||------------------------------------|----------------|----------------|----------------||
    ||                                    |                |                |                ||
    || Lubrificação de correntes e coroas |       X        |      SIM       |      SIM       ||
    ||                                    |                |                |                ||
    ||------------------------------------|----------------|----------------|----------------|| 
    || Transporte do segurado e Bike      |                |                |                ||
    || (limite de 50km, em caso de        |       X        |      SIM       |      SIM       ||
    || quebra ou acidente)                |                |                |                ||
    ||------------------------------------|----------------|----------------|----------------|| 
    || Transporte do segurado e Bike      |                |                |                ||
    || (limite de 150km, em caso de       |       X        |       X        |      SIM       ||
    || quebra ou acidente)                |                |                |                ||
    ||------------------------------------|----------------|----------------|----------------||
    || Instalação de suporte de           |                |                |                ||
    || parede e chão para bike            |       X        |       X        |      SIM       ||
    ||                                    |                |                |                ||
    ||------------------------------------|----------------|----------------|----------------||
    || Serviço de Leva e Traz,            |                |                |                ||
    || com limite de 50km, mediante       |       X        |       X        |      SIM       ||
    || agendamento prévio                 |                |                |                ||
    {linha}==============================
""")
            x = input("Pessione ENTER para voltar à escolha do plano")
            selecionar_plano()
        case _:
            print(f"""
    {linha}
    ---> DIGITE UMA OPÇÃO VÁLIDA!!!...
    {linha}    
            """)
    return plano

def perguntas() -> None:
     escolha_pergunta = 1
     print(f"""
    {linha}
    ||                   Perguntas Frequentes                  ||
    {linha}
    || 1 --> Quanto custa o seguro de uma bike?                ||
    || ------------------------------------------------------- ||
    || 2 --> Qual é o valor da franquia do Seguro Bike         ||
    || da Porto?                                               ||
    || ------------------------------------------------------- || 
    || 3 --> O seguro bike tem cobertura para terceiros?       ||
    || ------------------------------------------------------- ||
    || 4 --> O que devo fazer em uma situação de sinistro/dano ||
    || no bem coberto pelo seguro?                             ||
    || ------------------------------------------------------- ||
    || 5 --> O Seguro Bike da Porto oferece cobertura para     ||
    || acessórios?                                             ||
    || ------------------------------------------------------- ||
    || 6 --> O seguro bike oferece cobertura para furto?       ||
    || ------------------------------------------------------- ||
    || 7 --> Qual é o valor mínimo da bicicleta para que eu    ||
    || possa contratar o Seguro Bike da Porto?                 ||
    || ------------------------------------------------------- ||
    || 8 --> Nenhuma das anteriores.                           ||
    || ------------------------------------------------------- ||
    || 0 --> Voltar.                                           ||
    {linha}
    """)
    escolha_pergunta = int(input("Digite a opção que pode corresponder a sua pergunta: "))
    while escolha_pergunta != 0:                  
        match escolha_pergunta:
            case 1:
                print(f"""
    {linha}
    ---> Pergunta cadastrada com sucesso!!!...
    {linha}    
                """)       
            case 2:
                print(f"""
    {linha}
    ---> Pergunta cadastrada com sucesso!!!...
    {linha}    
                """)
            case 3:
                print(f"""
    {linha}
    ---> Pergunta cadastrada com sucesso!!!...
    {linha}    
                """)
            case 4:
                print(f"""
    {linha}
    ---> Pergunta cadastrada com sucesso!!!...
    {linha}    
                """)
            case 5:
                print(f"""
    {linha}
    ---> Pergunta cadastrada com sucesso!!!...
    {linha}    
                """)
            case 6:
                print(f"""
    {linha}
    ---> Pergunta cadastrada com sucesso!!!...
    {linha}    
                """)
            case 7:
                print(f"""
    {linha}
    ---> Pergunta cadastrada com sucesso!!!...
    {linha}    
                """)
            case 8:
                 
            case _:
                print(f"""
    {linha}
    ---> DIGITE UMA OPÇÃO VÁLIDA!!!...
    {linha}    
                """)
    print(f"""
    {linha}
    ---> Voltando...
    {linha}    
    """)
                      
# ALGORITMO PRINCIPAL
print(f"""
    {linha}
    || Bem-vindo ao programa responsável pela contratação do   ||
    || seguro de bikes via Porto Seguro.                       || 
    || Desenvolvido por: CycleX                                || 
    {linha}
    """)
while escolha_menu != 0:
    match menu():
        case 1:
            if cadastro_realizado:
                print(f"""
    {linha}
    ---> Cadastro já realizado selecionado!!!...
    {linha}    
                        """)
            else:
                dados_pessoal_bike = cadastro()
                cadastro_realizado = True
        case 2:
            if not cadastro_realizado:
                print(f"""
    {linha}
    ---> Para selecionar seu plano, precisamos que realize 
    o cadastro primeiro...
    {linha}    
                """)
            elif plano_selecionado:
                print(f"""
    {linha}
    ---> Plano já selecionado!!!...
    {linha}    
                """)
            else:
                tipo_plano = selecionar_plano()
                plano_selecionado = True
        case 3:
            print(f"""
    {linha}
    --> O cliente irá enviar as imagens necessárias da bike 
    por meio de um chatbot interativo, sem a necessidade de 
    um atendente.
    EM CONSTRUÇÃO!!!...
    {linha}
            """)
        case 4:
            print(f"""
    {linha}
    --> As imagens serão analisadas por meio de uma API que 
    informará se as peças estão em um bom estado e se suas 
    características coincidem com os dados apresentados pelo 
    cliente.
    EM CONSTRUÇÃO!!!...
    {linha}
            """)
        case 5:
            perguntas()
        case 0:
            print(f"""
    {linha}
    ---> FECHANDO O PROGRAMA!!!...
    {linha}
            """)
            break
        case _:
            print(f"""
    {linha}
    ---> DIGITE UMA OPÇÃO VÁLIDA!!!...
    {linha}    
            """)
if cadastro_realizado:
    print(dados_pessoal_bike)
    if possuir_acess:
        for i in range(0, len(tipo_acess), 1):
            print(f"""
    {linha}
    || Acessório {i + 1:<46d}||   
    || Tipo: {tipo_acess[i]:50}||
    || Marca: {marca_acess[i]:49}||
    || Modelo: {modelo_acess[i]:48}||
    || Valor: R${valor_acess[i]:<47.2f}||""")
        print("   ", linha)
    if plano_selecionado:
        print(f"""
    {linha}
    ---> {tipo_plano} selecionado!!!...
    {linha}    
        """)

