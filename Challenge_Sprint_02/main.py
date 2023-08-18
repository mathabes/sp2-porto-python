import sub
tipo_plano = ""

print(f"""
    {sub.linha}
    || Bem-vindo ao programa responsável pela contratação do   ||
    || seguro de bikes via Porto Seguro.                       ||
    || Desenvolvido por: CycleX                                ||
    {sub.linha}
    """)
while sub.escolha_menu != 0:
    match sub.menu():
        case 1:
            if sub.cadastro_realizado:
                print(f"""
    {sub.linha}
    ---> Cadastro já realizado!!!...
    {sub.linha}    
                """)
            else:
                sub.dados_pessoal_bike = sub.cadastro()
        case 2:
            if sub.plano_selecionado:
                print(f"""
    {sub.linha}
    ---> Plano já selecionado!!!...
    {sub.linha}    
                """)
            else:
                tipo_plano = sub.selecionar_plano()
        case 3:
            print(f"""
    {sub.linha}
    --> O cliente irá enviar as imagens necessárias da bike 
    por meio de um chatbot interativo, sem a necessidade de 
    um atendente.
    Em construção!!!...
    {sub.linha}
            """)
        case 4:
            print(f"""
    {sub.linha}
    --> As imagens serão analisadas por meio de uma API que 
    informará se as peças estão em um bom estado e se suas 
    características coincidem com os dados apresentados pelo 
    cliente.
    Em construção!!!...
    {sub.linha}
            """)
        case 5:
            sub.perguntas()
        case 0:
            if sub.cadastro_realizado:
                print(sub.dados_pessoal_bike)
            if sub.possuir_acess:
                for i in range(0, len(sub.tipo_acess), 1):
                    print(f"""
    {sub.linha}
    || Acessório {i + 1:<46d}||   
    || Tipo: {sub.tipo_acess[i]:50}||
    || Marca: {sub.marca_acess[i]:49}||
    || Modelo: {sub.modelo_acess[i]:48}||
    || Valor: R${sub.valor_acess[i]:<47.2f}||""")
                    print("   ", sub.linha)
            if sub.plano_selecionado:
                print(f"""
    {sub.linha}
    ---> {tipo_plano} selecionado!!!...
    {sub.linha}    
                """)
            if sub.possuir_pergunta_nova:
                print(f"""
    {sub.linha}
    ---> Nova pergunta cadastrada: "{sub.pergunta_nova}"
    {sub.linha}    
                """)
            print(f"""
    {sub.linha}
    ---> Fechando o programa!!!...
    {sub.linha}
            """)
            break
        case _:
            print(f"""
   {sub.linha}
   ---> DIGITE UMA OPÇÃO VÁLIDA!!!...
   {sub.linha}  
            """)
