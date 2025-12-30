import getpass

#1 Coletando os dados do usuário
usuario = input("\nDigite o nome certo: ").strip() #Remove espaços em branco
senha = getpass.getpass("""\n Coloque o código:""")

#2 Verificando as credenciais
if usuario.lower() == "zoye" and senha == "451":
    print(f"\n Mais um membro no jogo!")
    print("Isso está ficando cada vez mais interessante!")

else:
    print("""\n 
▄▀█ █▀▀ █▀▀ █▀ █▀ █▀█   █▄░█ █▀▀ █▀▀ ▄▀█ █▀▄ █▀█
█▀█ █▄▄ ██▄ ▄█ ▄█ █▄█   █░▀█ ██▄ █▄█ █▀█ █▄▀ █▄█.
         
 Nome de usuário ou senha incorretos.\n""")