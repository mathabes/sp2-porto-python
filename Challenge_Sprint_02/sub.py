# Subalgoritmos para o programa principal
escolha_menu = 1
linha = "=" * 61
tipo_acess = []
marca_acess = []
modelo_acess = []
valor_acess = []
dados_pessoal_bike = ""
pergunta_nova = ""
possuir_acess = False
possuir_pergunta_nova = False
plano_selecionado = False
cadastro_realizado = False


def menu() -> int:
    global escolha_menu
    print(f"""
    {linha}
    ||                         M E N U                         ||
    {linha}
    || 1................................: Realize o cadastro   ||
    || 2...............................: Ver/Selecioar plano   ||
    || 3................: Envio das imagens (Em construção!)   ||
    || 4......: Análise dos dados e imagens (Em construção!)   ||
    || 5..............................: Perguntas frequentes   ||
    || 0.................................: Fechar o programa   ||
    {linha}
    """)
    while True:
        try:
            escolha_menu = int(input("---> Escolha uma opção: "))
            break
        except ValueError:
            print(f"""
    {linha}
    --> DIGITE UMA OPÇÃO VÁLIDA!!!...
    {linha}    
            """)
            continue

    return escolha_menu


def cadastro() -> str:
    valor = 0
    quant_acess = 0
    global possuir_acess
    global cadastro_realizado
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
            if valor > 2000 or valor == 2000:
                break
            else:
                print("O valor mínimo de uma bike para que seja assegurada é de R$2000.00...")
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
    cadastro_realizado = True

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
    || Valor: R${valor:<47.2f}||
    {linha}""")
    return print_dados


def selecionar_plano() -> str:
    global plano_selecionado
    global cadastro_realizado
    global dados_pessoal_bike
    escolha_plano = 4
    plano = ""
    while escolha_plano == 4:
        print(f"""
    {linha}
    ||                    SELECIONE SEU PLANO                  ||
    {linha}
    || 1 --> Pedal essencial: O plano para você experimentar   ||
    || um dos serviços essenciais oferecidos, de acordo        ||
    || com as suas necessidades.                               ||
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
                if not cadastro_realizado:
                    print(f"""
    {linha}
    ---> Para selecionar seu plano, precisamos que realize 
    o cadastro primeiro...
    {linha}    
                    """)
                    dados_pessoal_bike = cadastro()
                plano = "Pedal essencial"
                print(f"""
    {linha}
    ---> Pedal essencial selecionado!!!...
    {linha}    
                """)
                plano_selecionado = True
            case 2:
                if not cadastro_realizado:
                    print(f"""
    {linha}
    ---> Para selecionar seu plano, precisamos que realize 
    o cadastro primeiro...
    {linha}    
                    """)
                    dados_pessoal_bike = cadastro()
                plano = "Pedal leve"
                print(f"""
    {linha}
    ---> Pedal leve selecionado!!!...
    {linha}    
                """)
                plano_selecionado = True
            case 3:
                if not cadastro_realizado:
                    print(f"""
    {linha}
    ---> Para selecionar seu plano, precisamos que realize 
    o cadastro primeiro...
    {linha}    
                """)
                    dados_pessoal_bike = cadastro()

                plano = "Pedal elite"
                print(f"""
    {linha}
    ---> Pedal elite selecionado!!!...
    {linha}    
                """)
                plano_selecionado = True
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
            case _:
                print(f"""
    {linha}
    ---> DIGITE UMA OPÇÃO VÁLIDA!!!...
    {linha}    
                """)
    return plano


def perguntas() -> None:
    escolha_pergunta = 1
    global possuir_pergunta_nova
    global pergunta_nova
    while escolha_pergunta != 0:
        print(f"""
    {linha}
    ||                   Perguntas Frequentes                  ||
    {linha}
    || 1 --> Quanto custa o seguro de uma bike?                ||
    || ------------------------------------------------------- || 
    || 2 --> O seguro bike tem cobertura para terceiros?       ||
    || ------------------------------------------------------- ||
    || 3 --> O que devo fazer em uma situação de sinistro/dano ||
    || no bem coberto pelo seguro?                             ||
    || ------------------------------------------------------- ||
    || 4 --> O Seguro Bike da Porto oferece cobertura para     ||
    || acessórios?                                             ||
    || ------------------------------------------------------- ||
    || 5 --> O seguro bike oferece cobertura para furto?       ||
    || ------------------------------------------------------- ||
    || 6 --> Qual é o valor mínimo da bicicleta para que eu    ||
    || possa contratar o Seguro Bike da Porto?                 ||
    || ------------------------------------------------------- ||
    || 7 --> Nenhuma das anteriores.                           ||
    || ------------------------------------------------------- ||
    || 0 --> Voltar.                                           ||
    {linha}
        """)
        while True:
            try:
                escolha_pergunta = int(input("Digite a opção que pode corresponder a sua pergunta: "))
                break
            except ValueError:
                print(f"""
    {linha}
    ---> DIGITE UMA OPÇÃO VÁLIDA!!!...
    {linha}    
                """)
                continue
        match escolha_pergunta:
            case 0:
                print(f"""
    {linha}
    ---> Voltando...
    {linha}    
                """)
            case 1:
                print(f"""
    {linha}
    ---> Para calcular o valor, precisamos de alguns dados da 
    pessoa e da bike. Informações como idade da   bicicleta, 
    modelo, forma de uso (lazer, esporte, trabalho) são 
    essenciais para a precificação, por isso, o valor do seguro 
    varia de acordo com cada perfil e tipo de bike.
    {linha}    
                """)
            case 2:
                print(f"""
    {linha}
    ---> Sim, de forma opcional. Chamamos de cobertura de 
    Responsabilidade Civil, que oferece amparo  para  danos 
    materiais ou corporais causados a terceiros durante o uso 
    da bicicleta. Ex.: a bike atingiu uma pessoa ou veículo de 
    alguém, a cobertura ampara essas situações, desde que a 
    pessoa atingida não seja alguém da sua família.
    {linha}    
                """)
            case 3:
                print(f"""
    {linha}
    ---> É importante nos comunicar sobre a ocorrência 
    imediatamente ou assim que possível. O aviso de sinistro 
    pode ser feito pelo WhatsApp 11 3003 9303 ou pelo site Porto 
    Seguro. A partir do aviso, damos início ao processo de análise 
    e indenização.
    {linha}    
                """)
            case 4:
                print(f"""
    {linha}
    ---> Tem cobertura: ciclocomputadores, GPS e velocímetros. 
    Não tem cobertura: acessórios de uso pessoal não acoplados 
    à bicicleta, como capacetes, luvas, squeezes, mochilas, 
    roupas e ferramentas.
    {linha}    
                """)
            case 5:
                print(f"""
    {linha}
    ---> Furtos simples, como o desaparecimento da bicicleta ou 
    roubo sem vestígios, não são cobertos pelo seguro bike.
    {linha}    
                """)
            case 6:
                print(f"""
    {linha}
    ---> Você pode contratar o seguro para bicicletas com 
    valores a partir de R$ 2.000,00
    {linha}    
                """)
            case 7:
                pergunta_nova = input("Digite sua pergunta: ")
                possuir_pergunta_nova = True
                print(f"""
    {linha}
    ---> Pergunta cadastrada. Responderemos o mais rápido 
    possível!!!...
    {linha}    
                """)
            case _:
                print(f"""
    {linha}
    ---> DIGITE UMA OPÇÃO VÁLIDA!!!...
    {linha}    
                """)
